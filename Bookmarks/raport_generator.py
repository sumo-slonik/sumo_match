import os

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from DataStructures import personal_competitor


class RaportGenerator:
    def __init__(self, competitors, category_name):
        self.competitors = competitors
        self.category_name = category_name

    def generate_pdf(self):
        path = os.getcwd() + "\\User_Files\\Reports\\Results\\"
        path = r"{}".format(path)

        print(path)

        pdfmetrics.registerFont(TTFont('polishFont', 'Bookmarks\\AbhayaLibre-Regular.ttf'))

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RegularDownloaded', alignment=TA_JUSTIFY, fontName='polishFont', fontSize=12))
        styles.add(ParagraphStyle(name='WeightName', alignment=TA_JUSTIFY, fontName='polishFont', fontSize=17))

        pdf = SimpleDocTemplate(
            path + self.category_name + ".pdf", pagesize=letter,
            rightMargin=72, leftMargin=72,
            topMargin=72, bottomMargin=18)

        body = [Paragraph('<font size="17"> %s </font>' % ('Kategoria: ' + self.category_name),
                          styles["WeightName"]), Spacer(1, 10)]

        for idx, competitor in enumerate(self.competitors):
            if idx in [2,3]:
                idx = 2
            if idx in [4,5]:
                idx = 4
            if idx in [6,7]:
                idx = 6
            if idx in [8,9]:
                idx = 8
            if idx in [8,9]:
                idx = 10
            if idx in [10,11]:
                idx = 12
            if idx in [12,13]:
                idx = 14
            body.append(Paragraph(str(idx+1) + ". " + competitor.get_first_name() + " " + competitor.get_surname() + "  |  "
                                  + competitor.get_club() + '|' + competitor.get_licence_no(),
                                  styles["RegularDownloaded"]))

        pdf.build(body)


# if __name__ == "__main__":
    # Competitors = [personal_competitor.PersonalCompetitor("Kuba1 N"), personal_competitor.PersonalCompetitor("Kuba2 N"),
    #                personal_competitor.PersonalCompetitor("Marcin1 W"), personal_competitor.PersonalCompetitor("Marcin2 W"),
    #                personal_competitor.PersonalCompetitor("pojedynczy1 X"),
    #                personal_competitor.PersonalCompetitor("pojedynczy2 X")]
    #
    # raport = RaportGenerator(Competitors, "kategoria próbna")
    # raport.generate_pdf()
