from reportlab.platypus.doctemplate import _doNothing
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate, NextPageTemplate
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.platypus.frames import Frame
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle as PS

from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase import pdfmetrics

from itertools import groupby

from inventory.models import Wine, PriceGroup

from .template import MyDocTemplate, addFontFile

from .stylesheet import styles, tstyles 


def createWholesalePriceList(response, priceGroup):

	addFontFile()

	story = []
	toc = TableOfContents()

	title = styles['Title']
	subtitle = styles['sTitle']
	body = styles['Body']
	bodyWine = styles['BodyWine']
	h1 = styles['h1']
	h2 = styles['h2']
	h3 = styles['h3']
	nh1 = styles['nh1']
	colW = (290,50,50,50)
	fullW = sum(colW)
	rowH = 19

	toc.levelStyles = [body, body]

	story.append(NextPageTemplate(['toc']))
	story.append(PageBreak())
	story.append(Spacer(1, 2.5*cm))
	story.append(Paragraph('<b>CONTENTS</b>', body))
	story.append(Spacer(1, 0.5*cm))
	story.append(toc)
	story.append(NextPageTemplate(['normal']))
	story.append(PageBreak())
	

	for group in priceGroup.objects.all():
		story.append(Paragraph(group.name.upper(), h1))

		wines = group.wine_set.all().order_by('appellation__my_order')
		appellation_groups = groupby(wines, lambda wine: wine.appellation)

		# Set header row -> Wine, Vintage, Bottle, Case
		data = [[ '', '', 'Bottle', 'Case']]
		t = Table(data, colWidths = colW, style=None, rowHeights=rowH)
		t.setStyle(tstyles['theader'])
		story.append(Spacer(1, 1*cm))
		story.append(t)
		
		# Add headers for Appelations if activated in Admin
		for appellation, wines in appellation_groups:
			if appellation.wholesale_list:
				story.append(Paragraph(appellation.name.upper(), h2))
			try:
				sortedwines = sorted(wines, key=lambda wine: wine.producer.name)
			except AttributeError:
				story.append('Wine missing producer')
			
			producer_groups = groupby(sortedwines, lambda wine: wine.producer)

			# Add headers for producers if wines exist
			for producer, wines in producer_groups:
				#winelist = sorted(wines, key=lambda wine: wine.vintage)
				winelist = sorted(wines, key=lambda wine: wine.wine)
				winelist = [elem for elem in winelist if elem.wholesale == True]
				if winelist == []:
					#story.append(Paragraph('<b>NO WINES</b>', body))
					pass
				else:
					data = []
					datarow = [Paragraph(producer.name.upper() ,h3)]
					data.append(datarow)
					t = Table(data, colWidths = fullW, style=None, rowHeights=rowH)
					#t.setStyle(tstyles['tnormal'])
					story.append(Spacer(1, 1*cm))
					story.append(t)

					# Add wines for producer
					data = []
					for wine in winelist:
						datarow = []

						if wine.size.name == 'Bottle':
							wine_name = wine.wine
						else:
							wine_name = "%s - %s" % (wine.wine, wine.size)
						datarow.append(Paragraph( "<font color=\"black\">%s</font>" % (wine_name), bodyWine))
						datarow.append(wine.vintage)
						try:
							whole_price = wine.wholesale_price
						except ValueError:
							whole_price = 0.0
						datarow.append("%s%.2f" % (u"\u00A3" , whole_price))
						datarow.append("%s%.2f" % (u"\u00A3" , wine.wholesale_case_price))
						data.append(datarow)

					t = Table(data, colWidths = colW, style=tstyles['tnormal'], rowHeights=rowH)
					story.append(t)

		story.append(PageBreak())

	doc = MyDocTemplate(response)
	doc.multiBuild(story)
