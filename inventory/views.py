from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Wine

import time

from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize


def pdf_creator(request):
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

	PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
	styles = getSampleStyleSheet()

	Title = "Friarwood Wine List"
	pageinfo = "Wine List"
	
	#Templates
	def myFirstPage(canvas, doc):
		canvas.saveState()
		canvas.setFont('Times-Bold',16)
		canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
		canvas.setFont('Times-Roman',9)
		canvas.drawString(cm, 0.75 * cm, "First Page / %s" % pageinfo)
		canvas.restoreState()

	def myLaterPages(canvas, doc):
		canvas.saveState()
		canvas.setFont('Times-Roman',9)
		canvas.drawString(cm, 0.75 * cm, "Page %d %s" % (doc.page, pageinfo))
		canvas.restoreState()


	doc = SimpleDocTemplate(response)
	Story = [Spacer(1,2*cm)]
	style = styles["Normal"]
	data = [['Wine', 'Retail', 'Cost']]
	for wine in Wine.objects.all()[:100]:
		datarow = []
		datarow.append(wine.short_name)
		datarow.append(wine.retail_price_s)
		datarow.append(wine.cost_price_s)
		data.append(datarow)
		
	t = Table(data)
	Story.append(t)
	Story.append(Spacer(1,0.2*cm))

	doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)

	#response.write(doc)
	return response


