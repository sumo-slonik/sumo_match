import pdfplumber
from PyQt5.uic.properties import QtGui
from PySide2.QtWidgets import QFileDialog
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from DataStructures.personal_competitor import PersonalCompetitor, Category

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER, letter
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

import Program_GUI.gui_theme


def create_pdf_repr(Form, name):
    wrapper = QFrame(Form)
    wrapper.setObjectName(u"frame")
    wrapper.setMinimumSize(QSize(180, 60))
    wrapper.setMaximumSize(QSize(180, 60))
    wrapper.setFrameShape(QFrame.StyledPanel)
    wrapper.setFrameShadow(QFrame.Raised)
    wrapperLayout = QHBoxLayout(wrapper)
    wrapperLayout.setSpacing(0)
    wrapperLayout.setObjectName(u"horizontalLayout")
    wrapperLayout.setContentsMargins(0, 0, 0, 0)
    icon_pdf = QPushButton(wrapper)
    icon_pdf.setObjectName(u"pushButton")
    icon_pdf.setEnabled(False)
    icon_pdf.setMinimumSize(QSize(40, 40))
    icon_pdf.setMaximumSize(QSize(40, 40))
    icon_pdf.setStyleSheet(u"background-color: rgb(85, 85, 127);")
    icon = QIcon()
    icon.addFile(u":/Icons/icons/cil-description.png", QSize(), QIcon.Normal, QIcon.Off)
    icon_pdf.setIcon(icon)
    wrapperLayout.addWidget(icon_pdf)

    PdfName = QTextEdit(wrapper)
    PdfName.setObjectName(u"PdfName")
    PdfName.setMinimumSize(QSize(90, 40))
    PdfName.setMaximumSize(QSize(90, 40))
    PdfName.setText(name)

    wrapperLayout.addWidget(PdfName)

    DelPdf = QPushButton(wrapper)
    DelPdf.setObjectName(u"DelPdf")
    DelPdf.setMinimumSize(QSize(40, 40))
    DelPdf.setMaximumSize(QSize(40, 40))
    DelPdf.setStyleSheet(u"background-color: rgb(85, 85, 127);")
    icon1 = QIcon()
    icon1.addFile(u":/Icons/icons/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
    DelPdf.setIcon(icon1)

    wrapperLayout.addWidget(DelPdf)
    return wrapper


class CategoryAdder:

    def __init__(self, window, settings):
        self.settings = settings
        self.added_categories = []
        self.competitors_list = []
        self.to_add = []
        self.window = window
        self.actual_competitor = None
        self.available_categories = []
        self.available_clubs = set()
        self.category_repr = dict()

    def add_category(self):
        files = QFileDialog.getOpenFileNames(self.window, "Dodaj kategorię", os.getcwd(), "Plik PDF (*.pdf)")
        self.to_add = files[0]
        self.window.ui.CategoriesToAdd.setText(str(files[0]))

    def confirm_categories(self):
        self.window.ui.CategoriesToAdd.setText("")

        for name in self.to_add:
            category_name = ''
            print("nazwa pliku:", name)
            with pdfplumber.open(name) as pdf:
                category_name = self.parse_pdf(pdf)
            new_repr = create_pdf_repr(self.window.ui.AddedCategoriesContents, category_name)
            new_repr.setObjectName(name + "repr")
            self.window.ui.verticalLayout_93.addWidget(new_repr)
            new_repr.show()
        self.show_in_table(self.competitors_list)

    def parse_pdf(self, pdf):
        lines = []
        for page in pdf.pages:
            lines += page.extract_text(x_tolerance=3, y_tolerance=3).split('\n')

        title = lines[0].split('-')
        weight = lines[2].split(':')[-1].split()[0]
        category_name = lines[0] + " " + lines[2].split()[-3:][0] + lines[2].split()[-3:][1]
        lines = list(filter(lambda x: x.split()[0] != 'Strona', lines))
        print(category_name)
        age_category = title[-1]
        weight_category = weight
        gender = title[1]
        actual_category = Category(weight_category, gender, age_category)
        self.available_categories.append(actual_category)
        for line in lines[4:]:
            print(line)
            name = line.split()[1] + ' ' + line.split()[2]
            club_tmp = line.split()[3: -2]
            club = ''
            for i in club_tmp:
                club += i + ' '
            self.available_clubs.add(club)
            licence_no = line.split()[-1]
            birth_year = line.split()[-2]
            actual_competitor = PersonalCompetitor(name, club, "", actual_category, birth_year, licence_no)
            if actual_competitor in self.competitors_list:
                index = self.competitors_list.index(actual_competitor)
                self.competitors_list[index].add_category(actual_category)
            else:
                self.competitors_list.append(actual_competitor)
        for i in self.competitors_list:
            print(i.custom_string_repr(True, True, True, True, False))
        self.actualise_combo_boxes()
        return category_name

    def show_in_table(self, competitors):

        table = self.window.ui.CompetitorsTable
        table.setRowCount(0)
        table_width = table.width()
        table.setColumnWidth(0, table_width / 4)
        table.setColumnWidth(1, table_width / 4)
        table.setColumnWidth(2, table_width / 4)
        table.setColumnWidth(3, table_width / 4)

        table.setRowCount(len(competitors))
        row = 0
        for competitor in competitors:
            table.setItem(row, 0, QTableWidgetItem(competitor.get_first_name()))
            table.setItem(row, 1, QTableWidgetItem(competitor.get_surname()))
            table.setItem(row, 2, QTableWidgetItem(competitor.get_club()))
            table.setItem(row, 3, QTableWidgetItem(competitor.get_licence_no()))
            row += 1
        table.installEventFilter(self.window)

    def create_combo_box(self, parent, values, start_value):
        class Combo(QComboBox):
            def __init__(self, parent, values, start_value):
                super().__init__(parent)
                self.addItems(values)
                self.setCurrentText(start_value)
                self.currentIndexChanged.connect(self.getComboValue)

            def getComboValue(self):
                return self.currentText()

        return Combo(parent, values, start_value)

    def process_competitor(self, licence_no):
        competitor = list(filter(lambda x: x.get_licence_no() == licence_no, self.competitors_list))[0]
        self.actual_competitor = competitor
        self.window.ui.ComprtitorName.setText("Imię:" + competitor.get_first_name())
        self.window.ui.CompetitorSurname.setText("Nazwisko:" + competitor.get_surname())
        self.window.ui.CompetitorClub.setText("Klub:" + competitor.get_club())
        self.window.ui.CompetitorBornDate.setText("Rok urodzenia:" + competitor.get_birth_year())
        self.window.ui.CompetitorLicenceNo.setText("Nr licencji:" + competitor.get_licence_no())
        self.window.ui.CompetitorWeightInput.setText(competitor.get_weight())
        table = self.window.ui.CompetitorCategories
        # table.clear()
        table.setRowCount(0)
        table.setRowCount(len(competitor.get_category()))
        row = 0
        ages = {x.age for x in self.available_categories}
        genders = {x.gender for x in self.available_categories}
        categories = {x.category for x in self.available_categories}
        for category in competitor.get_category():
            print(category)
            age_box = self.create_combo_box(table, ages, category.get_age())
            gender_box = self.create_combo_box(table, genders, category.get_gender())
            category_box = self.create_combo_box(table, categories, category.get_category())
            table.setCellWidget(row, 0, age_box)
            table.setCellWidget(row, 1, gender_box)
            table.setCellWidget(row, 2, category_box)
            if not self.check_age(competitor, category):
                table.cellWidget(row, 0).setStyleSheet("background-color: red;")
            row += 1

    def filter_competitors(self):
        def check_gender(competitor, gender):
            for i in competitor.category:
                print(i.gender)
                if gender == i.gender:
                    print('pass')
                    return True
            print('no pass')
            return False

        def check_age(competitor, age):
            for i in competitor.category:
                if age == i.age:
                    return True
            return False

        def check_club(competitor, club):
            return competitor.get_club() == club

        def check_category(competitor, category):
            for i in competitor.category:
                if category == i.category:
                    return True
            return False

        gender = self.window.ui.GenderComboBox.currentText()
        age = self.window.ui.AgeComboBox.currentText()
        category = self.window.ui.CategoryComboBox.currentText()
        club = self.window.ui.ClubComboBox.currentText()
        result = self.competitors_list[:]
        print(gender, age, category, club)
        if gender != "Wszystko":
            result = filter(lambda x: check_gender(x, gender), result)
        if age != "Wszystko":
            result = filter(lambda x: check_age(x, age), result)
        if category != "Wszystko":
            result = filter(lambda x: check_category(x, category), result)
        if club != "Wszystko":
            result = filter(lambda x: check_club(x, club), result)
        result = list(result)

        for i in result:
            print(i.name)
        return result

    def show_filter(self):
        self.show_in_table(self.filter_competitors())

    def check_age(self, competitor, category):

        def contains_digit(string):
            for i in string:
                if i.isdigit():
                    return True
            return False

        def category_number(string):
            result = ''
            for i in string:
                if i.isdigit():
                    result += i
            return int(result)

        age_range = [0, 0]
        if contains_digit(category.get_age()):
            age = category_number(category.get_age())

            if age == 14:
                age_range = self.settings.get_range('u14')
            if age == 16:
                age_range = self.settings.get_range('u16')
            if age == 18:
                age_range = self.settings.get_range('u18')
            if age == 21:
                age_range = self.settings.get_range('u21')
            if age == 23:
                age_range = self.settings.get_range('u23')
        else:
            if 'SENIOR' in category.get_age().upper():
                age_range = self.settings.get_range('senior')

        return age_range[0] <= int(competitor.get_birth_year()) <= age_range[1]

    def remove_category_from_competitor(self):
        table = self.window.ui.CompetitorCategories
        index = (table.selectionModel().currentIndex())
        table.removeRow(index.row())

    def add_category_to_competitor(self):
        table = self.window.ui.CompetitorCategories
        ages = {x.age for x in self.available_categories}
        genders = {x.gender for x in self.available_categories}
        categories = {x.category for x in self.available_categories}
        table.setRowCount(table.rowCount() + 1)
        idndex = table.rowCount()
        age_box = self.create_combo_box(table, ages, list(ages)[0])
        gender_box = self.create_combo_box(table, genders, list(genders)[0])
        category_box = self.create_combo_box(table, categories, list(categories)[0])
        table.setCellWidget(idndex - 1, 0, age_box)
        table.setCellWidget(idndex - 1, 1, gender_box)
        table.setCellWidget(idndex - 1, 2, category_box)

    def save_competitor_changes(self):
        weight = self.window.ui.CompetitorWeightInput.toPlainText()
        categories = set()

        table = self.window.ui.CompetitorCategories
        print("wiersze", table.rowCount())

        for i in range(table.rowCount()):
            a = table.cellWidget(i, 2).getComboValue()
            b = table.cellWidget(i, 1).getComboValue()
            c = table.cellWidget(i, 0).getComboValue()
            actual_cat = Category(a, b, c)
            categories.add(actual_cat)
        self.actual_competitor.category = categories
        self.actual_competitor.weight = weight

    def filter(self):
        pass

    def actualise_combo_boxes(self):
        GenderComboBox = self.window.ui.GenderComboBox
        AgeComboBox = self.window.ui.AgeComboBox
        CategoryComboBox = self.window.ui.CategoryComboBox
        ClubComboBox = self.window.ui.ClubComboBox
        genders = ["Wszystko"] + [x.gender for x in self.available_categories]
        ages = ["Wszystko"] + [x.age for x in self.available_categories]
        categories = ["Wszystko"] + [x.category for x in self.available_categories]
        clubs = ["Wszystko"] + list(self.available_clubs)
        genders = set(genders) - {GenderComboBox.itemText(i) for i in range(GenderComboBox.count())}
        ages = set(ages) - {AgeComboBox.itemText(i) for i in range(AgeComboBox.count())}
        categories = set(categories) - {CategoryComboBox.itemText(i) for i in range(CategoryComboBox.count())}
        clubs = set(clubs) - {ClubComboBox.itemText(i) for i in range(ClubComboBox.count())}

        self.window.ui.GenderComboBox.addItems(genders)
        self.window.ui.AgeComboBox.addItems(ages)
        self.window.ui.CategoryComboBox.addItems(categories)
        self.window.ui.ClubComboBox.addItems(clubs)
        self.window.ui.GenderComboBox.setCurrentText("Wszystko")
        self.window.ui.AgeComboBox.setCurrentText("Wszystko")
        self.window.ui.CategoryComboBox.setCurrentText("Wszystko")
        self.window.ui.ClubComboBox.setCurrentText("Wszystko")

    def categories_to_txt(self):
        categories_dict = {key: [] for key in self.available_categories}
        for competitor in self.competitors_list:
            for category in competitor.get_category():
                categories_dict[category].append(competitor)
        for key in categories_dict:
            with open('Categories/' + key.file_name() + '.txt', 'w', encoding="utf-8") as category_file:
                for competitor in categories_dict[key]:
                    category_file.write(
                        competitor.get_surname() + ' ' + competitor.get_first_name() + ';' + competitor.get_club() + ';\n')

    def prepare_categories_to_pdf(self):
        categories_dict = {key: [] for key in self.available_categories}
        for competitor in self.competitors_list:
            for category in competitor.get_category():
                categories_dict[category].append(competitor)

        categories_for_pdf = dict()

        for category in categories_dict:
            if categories_for_pdf.get((category.gender, category.age), None) is None:
                categories_for_pdf[(category.gender, category.age)] = dict()

            categories_for_pdf[(category.gender, category.age)][category] = categories_dict[category]

        return categories_for_pdf

    def create_pdfs(self):
        # ??????????????????????????????????????
        #  ??????????????????????????????????????
        # zmienić ścieżkę
        #  ??????????????????????????????????????
        #  ??????????????????????????????????????
        #  ??????????????????????????????????????
        pdfmetrics.registerFont(TTFont('polishFont', 'Bookmarks/AbhayaLibre-Regular.ttf'))

        categories_for_pdf = self.prepare_categories_to_pdf()

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RegularDownloaded', alignment=TA_JUSTIFY, fontName='polishFont', fontSize=12))
        styles.add(ParagraphStyle(name='WeightName', alignment=TA_JUSTIFY, fontName='polishFont', fontSize=17))

        path = os.getcwd() + "\\Reports\\"
        path = r"{}".format(path)

        for pdf_data in categories_for_pdf:

            pdf = SimpleDocTemplate(
                path + pdf_data[0] + "_" + pdf_data[1] + ".pdf", pagesize=letter,
                rightMargin=72, leftMargin=72,
                topMargin=72, bottomMargin=18)

            body = []

            for category in categories_for_pdf[pdf_data]:
                body.append(Paragraph('<font size="17"> %s </font>' % ('Kategoria: '+category.gender + "-" + category.age + "-" +
                                                                       category.category + " kg"),
                                      styles["WeightName"]))
                body.append(Spacer(1, 10))

                for competitor in categories_for_pdf[pdf_data][category]:
                    body.append(Paragraph(competitor.get_surname() + " " + competitor.get_first_name() + "  |  "
                                          + competitor.get_club()+'|'+competitor.get_licence_no(), styles["RegularDownloaded"]))

                body.append(Spacer(1, 10))

            # Save the PDF file
            pdf.build(body)
        print("Zakończono generowanie pdfów")


if __name__ == '__main__':
    path = os.getcwd() + "\\Reports\\"
    path = r"{}".format(path)

    print(path)
