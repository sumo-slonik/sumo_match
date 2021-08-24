import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

from DataStructures import personal_competitor


class RaportGenerator:
    def __init__(self, competitors, category_name):
        self.competitors = competitors
        self.category_name = category_name

    def generate_pdf(self):
        path = os.getcwd() + "\\User_Files\\Reports\\Results\\"
        path = r"{}".format(path)

        pdfmetrics.registerFont(TTFont('polishFont', 'Bookmarks\\AbhayaLibre-Regular.ttf'))

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RegularDownloaded', alignment=TA_JUSTIFY, fontName='polishFont', fontSize=12,
                                  borderWidth=0.5))
        styles.add(
            ParagraphStyle(name='CategoryName', alignment=TA_CENTER, fontName='polishFont', fontSize=17, borderWidth=3))

        pdf = SimpleDocTemplate(
            path + self.category_name + ".pdf", pagesize=letter,
            rightMargin=72, leftMargin=72,
            topMargin=72, bottomMargin=18)

        body = [Paragraph('<b> %s </b>' % ('Kategoria: ' + self.category_name),
                          styles["CategoryName"]), Spacer(1, 20)]

        data = [["Nr.", "Imię i nazwisko", "Klub", "Numer licencji"]]

        for idx, competitor in enumerate(self.competitors):
            if idx in [2, 3]:
                idx = 2
            elif idx in [4, 5]:
                idx = 4
            elif idx in [6, 7]:
                idx = 6
            elif idx in [8, 9]:
                idx = 8
            elif idx in [8, 9]:
                idx = 10
            elif idx in [10, 11]:
                idx = 12
            elif idx in [12, 13]:
                idx = 14

            data.append(
                [str(idx + 1), competitor.get_first_name() + " " + competitor.get_surname(), competitor.get_club(),
                 competitor.get_licence_no()])

        t = Table(data)
        t.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONT', (0, 0), (-1, -1), 'polishFont'),
            ('BACKGROUND', (0, 1), (3, 1), colors.gold),
            ('BACKGROUND', (0, 2), (3, 2), colors.lightgrey),
            ('BACKGROUND', (0, 3), (3, 4), colors.Color(red=(179.0 / 255), green=(140.0 / 255), blue=(82.0 / 255)))
        ]))

        body.append(t)
        pdf.build(body)


# if __name__ == "__main__":
#     Competitors = [personal_competitor.PersonalCompetitor("Kuba1 N"), personal_competitor.PersonalCompetitor("Kuba2 N"),
#                    personal_competitor.PersonalCompetitor("Marcin1 W"),
#                    personal_competitor.PersonalCompetitor("Marcin2 W"),
#                    personal_competitor.PersonalCompetitor("pojedynczy1 X"),
#                    personal_competitor.PersonalCompetitor("pojedynczy2 X")]
#
#     raport = RaportGenerator(Competitors, "kategoria próbna")
#     raport.generate_pdf()
