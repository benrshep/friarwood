#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from reportlab.lib.styles import ParagraphStyle, StyleSheet1
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer, PageBreak, Image, Table, TableStyle

styles= StyleSheet1()

# Title Page
styles.add(ParagraphStyle(
  name='Title',
  fontName='Castellar',
  fontSize=20,
))

styles.add(ParagraphStyle(
  name='sTitle',
  fontName='Times-Roman',
  fontSize=10,
))

# Wine
styles.add(ParagraphStyle(
  name='Body',
  fontName='Times-Roman',
  fontSize=9,
  leading=12
))

styles.add(ParagraphStyle(
  name='BodyWine',
  fontName='Times-Roman',
  fontSize=9,
  leading=12
))

# Price Group
styles.add(ParagraphStyle(
  name='Heading1',
  parent=styles['Body'],
  fontName='Castellar',
  alignment=TA_CENTER,
  fontSize=18,
  leading=22,
  spaceAfter=6
),alias='h1')

styles.add(ParagraphStyle(
  name='nHeading1',
  parent=styles['Body'],
  fontName='Castellar',
  alignment=TA_CENTER,
  fontSize=16,
  leading=22,
  spaceAfter=6
),alias='nh1')

# Appellation
styles.add(ParagraphStyle(
  name='Heading2',
  fontName='Times-Roman',
  fontSize=9,
),alias='h2')

# Producer
styles.add(ParagraphStyle(
  name='Heading3',
  fontName='Times-Roman',
  fontSize=9,
),alias='h3')

tstyles = { 
  'theader' : 
  TableStyle([
    ('FONT', (0,0), (-1,-1), 'Times-Roman'),
    ('SIZE', (0,0), (-1,-1), 9),
    ('LINEBELOW', (-3,0), (-1,0), 1, colors.black),
    ('ALIGN', (-3,0), (-1,-1), 'CENTER'),
    #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
  ]),
  'tnormal' : 
  TableStyle([
    ('FONT', (0,0), (-1,-1), 'Times-Roman'),
    ('SIZE', (0,0), (-1,-1), 9),
    #('LINEBELOW', (-3,0), (-1,0), 1, colors.black),
    ('ALIGN', (-3,0), (-1,-1), 'CENTER'),
    #('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
  ])
}

