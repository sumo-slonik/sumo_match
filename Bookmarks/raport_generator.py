from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


class RaportGenerator:
    def __init__(self, competitors):
        self.competitors = competitors

    def generate_pdf(self):
        pdfmetrics.registerFont(TTFont('polishFont', 'AbhayaLibre-Regular.ttf'))

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RegularDownloaded', alignment=TA_JUSTIFY, fontName='polishFont', fontSize=12))
        styles.add(ParagraphStyle(name='WeightName', alignment=TA_JUSTIFY, fontName='polishFont', fontSize=17))
