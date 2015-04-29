from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import PageBreak
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.platypus.frames import Frame
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import cm

from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

from reportlab.lib.colors import gray

Title = "Friarwood Fine Wines Ltd."
pageinfo = "Wine List"
address = "26 New Kings Road, LONDON SW6 4ST"
phone = "T:+44 (0) 20 7736 2628  F:+44 (0) 20 7731 0411"
PAGE_WIDTH, PAGE_HEIGHT = A4

def addFontFile(font='castellar'):

	pdfmetrics.registerFont(TTFont('Castellar', 'castellar.ttf'))
	registerFontFamily('Castellar',normal='Castellar',bold='Castellar',italic='Castellar',boldItalic='Castellar')

def drawBorder(canvas):
	canvas.setStrokeColorCMYK(0, 0, 0, 20)
	canvas.setStrokeColor(gray)
	# Bottom left location of border
	bx = 0.6*cm
	# Border padding top and bottom
	bpt = 2*cm
	bpb = 2*cm
	# Spacing between double border
	bs = 0.07*cm
	# Width of border box
	bw = PAGE_WIDTH-(bx*2)
	# Height of border box
	bh = PAGE_HEIGHT-bpt-bpb
	# Set outer border width
	canvas.setLineWidth(0.01*cm)
	canvas.rect(x=bx , y=bpb , width=bw , height=bh , stroke=1)
	# Set inner border width
	canvas.setLineWidth(0.06*cm)
	canvas.rect(x=(bx+bs) , y=(bpb+bs) , width=(bw-(bs*2)) , height=(bh-(bs*2)) , stroke=1)

def drawFooter(canvas):
	canvas.setFont('Times-Roman',9)
	bh = 20
	canvas.drawCentredString(PAGE_WIDTH/2.0, bh+12+12, Title.upper())
	canvas.drawCentredString(PAGE_WIDTH/2.0, bh+12, address)
	canvas.drawCentredString(PAGE_WIDTH/2.0, bh, phone)
	canvas.setAuthor("Friarwood Fine Wines")
	canvas.setTitle("Wholesale Pricelist")
	canvas.setSubject("Current Wholesale Pricelist for --date--")
	#canvas.drawString(cm, 0.75 * cm, "Page %d %s" % (doc.page, pageinfo))

def titlePage(canvas, doc):
	''' A4 Size 210*297 '''
	canvas.saveState()
	canvas.setFont('Castellar',34)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-350, 'Friarwood'.upper())
	canvas.setFont('Times-Roman',18)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-390, 'Fine Wine'.upper())
	canvas.drawCentredString(PAGE_WIDTH/2.0, 200, 'Price List'.upper())
	canvas.restoreState()

def tocPage(canvas, doc):
	canvas.saveState()
	canvas.setFont('Castellar',20)
	canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-40, 'Wholesale Price List'.upper())
	drawBorder(canvas)
	drawFooter(canvas)
	canvas.restoreState()

def defaultPage(canvas, doc):
	canvas.saveState()
	canvas.setFont('Castellar',16)
	drawBorder(canvas)
	drawFooter(canvas)
	canvas.restoreState()

class MyDocTemplate(BaseDocTemplate):
	'''
	(self, filename,
	pagesize=defaultPageSize,
	pageTemplates=[],
	showBoundary=0,
	leftMargin=inch,
	rightMargin=inch,
	topMargin=inch,
	bottomMargin=inch,
	allowSplitting=1,
	title=None,
	author=None,
	_pageBreakQuick=1,
	encrypt=None)
	'''

	def __init__(self, filename, **kw):
		
		self.allowSplitting = 0
		BaseDocTemplate.__init__(self, filename, **kw)

		self.pagesize = A4
		self.topMargin = 0.5*cm
		self.bottomMargin = 2*cm
		self.leftMargin = 1*cm
		self.rightMargin = 1*cm
		self._calc()

		frameT = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, 
			id='normal', showBoundary=1)
		# Table of contents padding
		tocP = 3*cm
		frameTOC = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, 
			leftPadding=tocP, rightPadding=tocP, id='toc', showBoundary=1)

		titleTemplate = PageTemplate('title', frames=frameT, onPage=titlePage)
		tocTemplate =PageTemplate('toc', frames=frameTOC, onPage=tocPage)
		template = PageTemplate('normal', frames=frameT, onPage=defaultPage)
		
		self.addPageTemplates([titleTemplate, tocTemplate, template])

		#Frame(x1, y1, width,height, leftPadding=6, bottomPadding=6, rightPadding=6, topPadding=6, id=None, showBoundary=0)
		#BaseDocTemplate.addPageTemplates(self,pageTemplates)

	def afterFlowable(self, flowable):
		"Registers TOC entries."
		if flowable.__class__.__name__ == 'Paragraph':
			text = flowable.getPlainText()
			style = flowable.style.name
			if style == 'Heading1':
				self.notify('TOCEntry', (0, text, self.page))
			if style == 'Heading2':
				self.notify('TOCEntry', (1, text, self.page))


