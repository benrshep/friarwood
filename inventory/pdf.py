#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from reportlab.platypus.doctemplate import _doNothing
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.platypus.frames import Frame
from reportlab.platypus.tableofcontents import TableOfContents

from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle, StyleSheet1
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase import pdfmetrics

from itertools import groupby

from .models import Wine, PriceGroup

def getWineListStyleSheet():
    """Returns a stylesheet object"""
    stylesheet = StyleSheet1()

    stylesheet.add(ParagraphStyle(name='Normal',
                                  fontName='Times-Roman',
                                  fontSize=10,
                                  leading=12 )
                   )

    stylesheet.add(ParagraphStyle(name='Heading1',
                                  parent=stylesheet['Normal'],
                                  fontName='Times-Roman',
                                  fontSize=14,
                                  leading=22,
                                  spaceAfter=6),alias='h1')

    stylesheet.add(ParagraphStyle(name='TableH',
                                  fontName='Helvetica-Bold',
                                  fontSize=9,
                                  )
                   )

    stylesheet.add(ParagraphStyle(name='TableIn',
                                  fontName='Helvetica',
                                  fontSize=9,
                                  )
    				)

    stylesheet.add(ParagraphStyle(name='TableH1',
                                  fontName='Times-Bold',
                                  fontSize=12,
                                  )
                   )

    return stylesheet


def addFontFile(font='castellar'):

  afmFile = '%s.afm' % font.lower()
  pfbFile = '%s.pfb' % font.lower()
  justFace = pdfmetrics.EmbeddedType1Face(afmFile, pfbFile)
  faceName = font.title() # pulled from AFM file
  pdfmetrics.registerTypeFace(justFace)
  justFont = pdfmetrics.Font(font.title(),faceName,'WinAnsiEncoding')
  pdfmetrics.registerFont(justFont)


def createWholesalePriceList(response):
  
  addFontFile()

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

  tableIn = styles["TableIn"]
  tableH = styles["TableH"]
  tableH1 = styles["TableH1"]
  style = styles["Normal"]
  styleH = styles['h1']

  story = []
  #toc = TableOfContents()
  #toc.levelStyles = [styleH, tableH1, tableH]
  
  story.append(PageBreak())
  #story.append(toc)
  story.append(PageBreak())
  
  #generatePriceList(PriceGroup.objects.all(), story)
  for group in PriceGroup.objects.all():

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("%s" % group.name.upper(), styleH))
    
    wines = group.wine_set.all().order_by('appellation__my_order')
    appellation_groups = groupby(wines, lambda wine: wine.appellation)

    data = [[ '', 'Vintage', 'Bottle', 'Case']]

    for appellation, wines in appellation_groups:
      try: 
        datarow1 = [Spacer(1, 0.5*cm)]
        datarow = []
        datarow.append(Paragraph(appellation.name.upper() ,tableH1))
        data.append(datarow1)
        data.append(datarow)
      except:
        pass
      try:
        sortedwines = sorted(wines, key=lambda wine: wine.producer.name)
      except AttributeError:
        story.append('Wine missing producer')

      producer_groups = groupby(sortedwines, lambda wine: wine.producer)
      #producer_groups = sorted(producer_groups, key=lambda wine: (producer.name,)

      for producer, wines in producer_groups:
        winelist = sorted(wines, key=lambda wine: wine.wine)
        winelist = [elem for elem in winelist if elem.retail == True]
        if winelist == []:
          pass
        else:
          datarow = [Spacer(1, 0.5*cm)]
          data.append(datarow)
          datarow = []
          datarow.append(Paragraph(producer.name.upper() ,tableH))
          data.append(datarow)
          for wine in winelist:
            datarow = []
            datarow.append(Paragraph(wine.wine, tableIn))
            datarow.append(wine.vintage)
            try:
              whole_price = wine.wholesale_price
            except ValueError:
              whole_price = 0.0
            datarow.append("%s%.2f" % (u"\u00A3" , whole_price))
            datarow.append("%s%.2f" % (u"\u00A3" , wine.wholesale_case_price))
            data.append(datarow)

    t = Table(data, colWidths = (290,50,50,50), style=None, rowHeights=19)
    t.setStyle(TableStyle([
      ('FONT', (-3,0), (-1,0), 'Times-Roman'),
      ('LINEBELOW', (-3,0), (-1,0), 1, colors.black),
      ('ALIGN', (-3,0), (-1,-1), 'CENTER'),
      #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
      ])
    )
    story.append(t)
    story.append(PageBreak())


  story.append(Spacer(1,0.2*cm))

  doc = SimpleDocTemplate(response, pagesize = A4, showBoundary=0)
  #doc = PriceListTemplate(response)
  doc.build(story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
  #doc.multiBuild(story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


def createRetailPriceList(response):
  
  addFontFile()

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

  tableIn = styles["TableIn"]
  tableH = styles["TableH"]
  tableH1 = styles["TableH1"]
  style = styles["Normal"]
  styleH = styles['h1']

  story = []
  #toc = TableOfContents()
  #toc.levelStyles = [styleH, tableH1, tableH]
  
  story.append(PageBreak())
  #story.append(toc)
  story.append(PageBreak())
  
  #generatePriceList(PriceGroup.objects.all(), story)
  for group in PriceGroup.objects.all():

    story.append(Spacer(1, 0.5*cm))
    story.append(Paragraph("%s" % group.name.upper(), styleH))
    
    wines = group.wine_set.all().order_by('appellation__my_order')
    appellation_groups = groupby(wines, lambda wine: wine.appellation)

    data = [[ '', 'Vintage', 'Retail']]

    for appellation, wines in appellation_groups:
      try: 
        datarow1 = [Spacer(1, 0.5*cm)]
        datarow = []
        datarow.append(Paragraph(appellation.name.upper() ,tableH1))
        data.append(datarow1)
        data.append(datarow)
      except:
        pass
      try:
        sortedwines = sorted(wines, key=lambda wine: wine.producer.name)
      except AttributeError:
        story.append('Wine missing producer')

      producer_groups = groupby(sortedwines, lambda wine: wine.producer)
      #producer_groups = sorted(producer_groups, key=lambda wine: (producer.name,)

      for producer, wines in producer_groups:
        winelist = sorted(wines, key=lambda wine: wine.wine)
        winelist = [elem for elem in winelist if elem.retail == True]
        if winelist == []:
          pass
        else:
          datarow = [Spacer(1, 0.5*cm)]
          data.append(datarow)
          datarow = []
          datarow.append(Paragraph(producer.name.upper() ,tableH))
          data.append(datarow)
          
          for wine in [elem for elem in winelist if elem.retail == True]:
            datarow = []
            if wine.wine == '':
              datarow.append(Paragraph(wine.short_name, tableIn))
            else:
              datarow.append(Paragraph(wine.wine, tableIn))
            datarow.append(wine.vintage)
            try:
              price = float(wine.retail_price)
              datarow.append("%s%.2f" % (u"\u00A3" , price))
            except:
              price = 0.0
              datarow.append('N/A')
            data.append(datarow)

    t = Table(data, colWidths = (300,50,50), style=None, rowHeights=19)
    t.setStyle(TableStyle([
      ('FONT', (-2,0), (-1,0), 'Times-Roman'),
      ('LINEBELOW', (-2,0), (-1,0), 1, colors.black),
      ('ALIGN', (-2,0), (-1,-1), 'CENTER'),
      #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
      ])
    )
    story.append(t)
    story.append(PageBreak())


  story.append(Spacer(1,0.2*cm))

  doc = SimpleDocTemplate(response, pagesize = A4, showBoundary=0)
  #doc = PriceListTemplate(response)
  doc.build(story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
  #doc.multiBuild(story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


class PriceListTemplate(BaseDocTemplate):
    def __init__(self, filename, **kw):
      self.allowSplitting = 0
      BaseDocTemplate.__init__(self, filename, **kw)
      template = PageTemplate('normal', [Frame(2.5*cm, 2.5*cm, 15*cm, 25*cm, id='F1')])
      self.addPageTemplates(template)
    def afterFlowable(self, flowable):
      "Registers TOC entries."
      if flowable.__class__.__name__ == 'Paragraph':
        text = flowable.getPlainText()
        style = flowable.style.name
        if style == 'h1':
          self.notify('TOCEntry', (0, text, self.page))
        if style == 'tableH1':
          self.notify('TOCEntry', (1, text, self.page))
        if style == 'tableH':
          self.notify('TOCEntry', (2, text, self.page))

    def multiBuild(self,flowables,onFirstPage=_doNothing, onLaterPages=_doNothing, canvasmaker=canvas.Canvas): 
      '''build the document using the flowables. Annotate the first page using the onFirstPage 
      function and later pages using the onLaterPages function. The onXXX pages should follow 
      the signature 

      def myOnFirstPage(canvas, document): 
        # do annotations and modify the document 
        ... 

        The functions can do things like draw logos, page numbers, footers, etcetera. They can use 
        external variables to vary the look (for example providing page numbering or section names). 
        '''

      self._calc() #in case we changed margins sizes etc 

      frameT = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id='normal') 

      self.addPageTemplates([
        PageTemplate (
          id='First',
          frames=frameT, 
          onPage=onFirstPage,
          pagesize=self.pagesize), 
        PageTemplate(
          id='Later',
          frames=frameT, 
          onPage=onLaterPages,
          pagesize=self.pagesize)
        ]
      ) 
      if onFirstPage is _doNothing and hasattr(self,'onFirstPage'): 
        self.pageTemplates[0].beforeDrawPage = self.onFirstPage 
      if onLaterPages is _doNothing and hasattr(self,'onLaterPages'): 
        self.pageTemplates[1].beforeDrawPage = self.onLaterPages 

      BaseDocTemplate.multiBuild(self,flowables, canvasmaker=canvasmaker)

