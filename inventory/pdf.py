
from reportlab.lib.styles import ParagraphStyle, StyleSheet1
from reportlab.platypus.tables import TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER


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
                                  fontSize=16,
                                  leading=22,
                                  spaceAfter=6),alias='h1')

    stylesheet.add(ParagraphStyle(name='TableH',
                                  fontName='Helvetica-Bold',
                                  fontSize=10,
                                  )
                   )

    stylesheet.add(ParagraphStyle(name='TableIn',
                                  fontName='Helvetica',
                                  fontSize=10,
                                  )
    				)

    stylesheet.add(ParagraphStyle(name='TableH1',
                                  fontName='Times-Bold',
                                  fontSize=12,
                                  )
                   )

    return stylesheet

    