from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Wine, PriceGroup
import time

from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.platypus.tables import TableStyle

from reportlab.lib.units import cm

from reportlab.lib import colors

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics

from .pdf import getWineListStyleSheet

from itertools import groupby

from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame



def pdf_creator(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="WineList.pdf"'

	afmFile = 'castellar.afm'
	pfbFile = 'castellar.pfb'

	justFace = pdfmetrics.EmbeddedType1Face(afmFile, pfbFile)
	faceName = 'Castellar' # pulled from AFM file
	pdfmetrics.registerTypeFace(justFace)
	justFont = pdfmetrics.Font('Castellar',faceName,'WinAnsiEncoding')
	pdfmetrics.registerFont(justFont)

	PAGE_WIDTH, PAGE_HEIGHT = A4
	styles = getWineListStyleSheet()

	Title = "Friarwood Fine Wines Ltd."
	pageinfo = "Wine List"
	address = "26 New Kings Road, LONDON SW6 4ST"
	phone = "T:+44 (0) 20 7736 2628  F:+44 (0) 20 7731 0411"
	
	#Templates
	def myFirstPage(canvas, doc):

		canvas.saveState()
		canvas.setFont('Castellar',16)
		canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-40, Title)
		#210*297
		canvas.setLineWidth(0.1*cm)
		canvas.rect(x=0.6*cm , y=0.6*cm , width=19.8*cm , height=28.5*cm , stroke=1)
		canvas.setLineWidth(0.01*cm)
		canvas.rect(x=0.7*cm , y=0.7*cm , width=19.6*cm , height=28.3*cm , stroke=1)

		canvas.setFont('Times-Roman',9)
		canvas.drawCentredString(PAGE_WIDTH/2.0, 55, Title.upper())
		canvas.drawCentredString(PAGE_WIDTH/2.0, 43, address)
		canvas.drawCentredString(PAGE_WIDTH/2.0, 31, phone)
		canvas.restoreState()

	def myLaterPages(canvas, doc):
		

		canvas.saveState()
		canvas.setFont('Castellar',16)
		canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-40, Title)
		#210*297
		canvas.setLineWidth(0.1*cm)
		canvas.rect(x=0.6*cm , y=0.6*cm , width=19.8*cm , height=28.5*cm , stroke=1)
		canvas.setLineWidth(0.01*cm)
		canvas.rect(x=0.7*cm , y=0.7*cm , width=19.6*cm , height=28.3*cm , stroke=1)
		canvas.setFont('Times-Roman',9)
		canvas.drawCentredString(PAGE_WIDTH/2.0, 55, Title.upper())
		canvas.drawCentredString(PAGE_WIDTH/2.0, 43, address)
		canvas.drawCentredString(PAGE_WIDTH/2.0, 31, phone)
		#canvas.drawString(cm, 0.75 * cm, "Page %d %s" % (doc.page, pageinfo))
		canvas.restoreState()

	doc = SimpleDocTemplate(response)
	story = []
	tableIn = styles["TableIn"]
	tableH = styles["TableH"]
	tableH1 = styles["TableH1"]
	style = styles["Normal"]
	styleH = styles['h1']

	for group in PriceGroup.objects.all():

		story.append(PageBreak())
		story.append(Spacer(1,1*cm))
		story.append(Paragraph("%s" % group.name.upper(), styleH))

		wines = group.wine_set.all().order_by('appellation__name')

		appellation_groups = groupby(wines, lambda wine: wine.appellation)

		data = [[ '', 'Vintage', 'Bottle', 'Case']]

		for appellation, wines in appellation_groups:
			try: 
				datarow = ['']
				data.append(datarow)
				datarow = []
				datarow.append(Paragraph(appellation.name.upper() ,tableH1))
				data.append(datarow)
			except:
				pass
			
			producer_groups = groupby(wines, lambda wine: wine.producer)

			for producer, wines in producer_groups:
				datarow = ['']
				data.append(datarow)
				datarow = []
				datarow.append(Paragraph(producer.name.upper() ,tableH))
				data.append(datarow)

				for wine in sorted(wines, key=lambda wine: wine.wine):
					datarow = []
					datarow.append(Paragraph(wine.wine, tableIn))
					datarow.append(wine.vintage)
					try:
						whole_price = float(wine.wholesale_price_s)
					except ValueError:
						whole_price = "0.0"
					datarow.append("%s%.2f" % ('\u00A3' , float(whole_price)))
					datarow.append("%s%.2f" % ('\u00A3' , float(wine.wholesale_case_price)))
					data.append(datarow)

		t = Table(data, colWidths = (300,50,50,50), style=None, rowHeights=20)
		t.setStyle(TableStyle([
			('FONT', (-3,0), (-1,0), 'Times-Roman'),
			('LINEBELOW', (-3,0), (-1,0), 1, colors.black),
			('ALIGN', (-3,0), (-1,-1), 'CENTER'),
			#('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
			])
		)
		story.append(t)
		#story.append(Paragraph("%s" % wine.short_name , style))




	story.append(Spacer(1,0.2*cm))

	doc.build(story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

	#response.write(doc)
	return response


