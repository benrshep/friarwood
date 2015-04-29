from reportlab.platypus.doctemplate import NextPageTemplate
from reportlab.platypus import Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.platypus.tableofcontents import TableOfContents

from reportlab.pdfgen import canvas

from reportlab.lib.units import cm
from reportlab.lib import colors

from itertools import groupby

from inventory.models import Wine, PriceGroup

from .template import MyDocTemplate, addFontFile, wineTable
from .stylesheet import styles, tstyles 

from reportlab.lib.colors import CMYKColor, PCMYKColor

title = styles['Title']
subtitle = styles['sTitle']
body = styles['Body']
bodyin = styles['BodyIn']
bodyWine = styles['BodyWine']
h1 = styles['h1']
h2 = styles['h2']
h3 = styles['h3']
nh1 = styles['nh1']
colW = (10.75*cm,1.75*cm,1.75*cm,1.75*cm)
fullW = sum(colW)
rowH = 17

def createPriceList(response, wine, mode = 'wholesale'):

	def addTableTitle(title, style):
		data=[[title]]
		story.append(Spacer(1, 0.5*cm))
		story.append(Table(data, colWidths=fullW, style=tstyles[style], rowHeights=rowH))
	
	addFontFile()
	story = []

	# TITLE PAGE 
	story.append(NextPageTemplate(['toc']))
	story.append(PageBreak())

	# TABLE OF CONTENTS
	toc = TableOfContents()
	toc.levelStyles = [body, bodyin]
	story.append(Spacer(1, 2.5*cm))
	story.append(Paragraph('<b>CONTENTS</b>', body))
	story.append(Spacer(1, 0.5*cm))
	story.append(toc)
	story.append(NextPageTemplate(['normal']))
	story.append(PageBreak())

	# GET ALL WINE OBJECTS
	if mode == 'retail':
		wines=wine.objects.filter(
			retail=True, price_group__isnull=False).order_by(
			'price_group__my_order', 'appellation__my_order', 'producer__name')
	else:
		wines=wine.objects.filter(
			wholesale=True, price_group__isnull=False).order_by(
			'price_group__my_order', 'appellation__my_order', 'producer__name')

	## PRICE GROUP START
	price_groups=groupby(wines, lambda wine: wine.price_group)	
	for pg, w in price_groups:
		story.append(Paragraph(pg.name.upper(), h1))
		# Set header row -> Wine, Vintage, Bottle, Case
		data=[[ '', 'Vintage', 'Bottle', 'Case']]
		story.append(Spacer(1, 1*cm))
		story.append(Table(
			data, 
			colWidths=colW, 
			style=tstyles['theader'], 
			rowHeights=rowH
		))

	## PRICE GROUP END
		# APPELLATION GROUP START	
		appellation_groups=groupby(w, lambda wine: wine.appellation)
		for a, w in appellation_groups:

			if a.retail_list or a.wholesale_list:
				data=[[a.name.upper()]]
				story.append(Spacer(1, 0.5*cm))
				t = wineTable(data, colWidths=fullW, style=tstyles['tappellation'], rowHeights=rowH)
				t.name = a.name.upper()
				story.append(t)

		# APPELLATION GROUP END
			# PRODUCER GROUP START			
			producer_groups=groupby(w, lambda wine: wine.producer)
			for p, wines in producer_groups:
				addTableTitle(p.name.upper(), 'tproducer')

				#w = sorted(w, key=lambda wine: wine.vintage)
				#w = sorted(w, key=lambda wine: wine.size.size)
				#w = sorted(w, key=lambda wine: wine.wine)
				data = []
				row = 0
				wine_colours = []
				for w in wines:	
					datarow = []
					if w.size.name == 'Bottle':
						wine_name = w.wine
					else:
						wine_name = "%s - %s" % (w.wine, w.size)
					
					colour = {
						None : PCMYKColor(0,0,0,100),
						'' : PCMYKColor(0,0,0,100),
						'Ro' : PCMYKColor(0,76,23,9),
						'W' : PCMYKColor(84,0,100,42),
						'R' : PCMYKColor(0,89,100,9)
					}
					wine_colour = w.colour

					#Set wine colour
					wine_colours.append(('TEXTCOLOR',(0,row),(0,row), colour[wine_colour]))
					datarow.append( "%s" % (wine_name))
					#set default colour
						
					datarow.append(w.vintage)
					try:
						whole_price = w.wholesale_price
					except ValueError:
						whole_price = 0.0
					datarow.append("%s%.2f" % (u"\u00A3" , whole_price))
					datarow.append("%s%.2f" % (u"\u00A3" , w.wholesale_case_price))
					data.append(datarow)
					row += 1
				t = Table(data, colWidths = colW, style=tstyles['tnormal'], rowHeights=rowH)
				t.setStyle(TableStyle(wine_colours))
				story.append(t)

			# PRODUCER GROUP END

		story.append(PageBreak())

	doc = MyDocTemplate(response)
	doc.multiBuild(story)
