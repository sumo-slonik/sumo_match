import pdfplumber
from PySide2.QtWidgets import QFileDialog
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from personal_competitor import PersonalCompetitor, Category

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
    print("zwracam")
    return wrapper


class CategoryAdder:
    def __init__(self, window):
        self.added_categories = []
        self.competitors_list = []
        self.to_add = []
        self.window = window
        self.actual_competitor = None

    def add_category(self):
        files = QFileDialog.getOpenFileNames(self.window, "Dodaj kategorię", os.getcwd(), "Plik PDF (*.pdf)")
        self.to_add = files[0]
        self.window.ui.CategoriesToAdd.setText(str(files[0]))

    def confirm_categories(self):
        print("tuaj")
        self.window.ui.CategoriesToAdd.setText("")

        for name in self.to_add:
            category_name = ''
            with pdfplumber.open(name) as pdf:
                category_name = self.parse_pdf(pdf)
            new_repr = create_pdf_repr(self.window.ui.AddedCategoriesContents, category_name)
            new_repr.setObjectName(name + "repr")
            self.window.ui.verticalLayout_93.addWidget(new_repr)
            new_repr.show()
        self.show_in_table()

    def parse_pdf(self, pdf):
        lines = []
        for page in pdf.pages:
            lines += page.extract_text(x_tolerance=3, y_tolerance=3).split('\n')

        category_name = lines[0] + " " + lines[2].split()[-3:][0] + lines[2].split()[-3:][1]
        lines = list(filter(lambda x: x.split()[0] != 'Strona', lines))
        print(category_name)
        age_category = category_name.split()[-2]
        weight_category = category_name.split()[-1]
        gender = category_name.split()[-4]
        actual_category = Category(weight_category, gender, age_category)
        for line in lines[4:]:
            print(line)
            name = line.split()[1] + ' ' + line.split()[2]
            club_tmp = line.split()[3: -2]
            club = ''
            for i in club_tmp:
                club += i + ' '
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
        return category_name

    def show_in_table(self):
        a = QTabWidget(None)
        table = self.window.ui.CompetitorsTable
        table_width = table.width()
        table.setColumnWidth(0, table_width / 4)
        table.setColumnWidth(1, table_width / 4)
        table.setColumnWidth(2, table_width / 4)
        table.setColumnWidth(3, table_width / 4)

        table.setRowCount(len(self.competitors_list))
        row = 0
        for competitor in self.competitors_list:
            table.setItem(row, 0, QTableWidgetItem(competitor.get_first_name()))
            table.setItem(row, 1, QTableWidgetItem(competitor.get_surname()))
            table.setItem(row, 2, QTableWidgetItem(competitor.get_club()))
            table.setItem(row, 3, QTableWidgetItem(competitor.get_licence_no()))
            row += 1
        table.installEventFilter(self.window)

    def process_competitor(self, licence_no):
        competitor = list(filter(lambda x: x.get_licence_no() == licence_no, self.competitors_list))[0]
        self.window.ui.ComprtitorName.setText("Imię:" + competitor.get_first_name())
        self.window.ui.CompetitorSurname.setText("Nazwisko:" + competitor.get_surname())
        self.window.ui.CompetitorClub.setText("Klub:" + competitor.get_club())
        self.window.ui.CompetitorBornDate.setText("Rok urodzenia:" + competitor.get_birth_year())
        self.window.ui.CompetitorLicenceNo.setText("Nr licencji:" + competitor.get_licence_no())
        table = self.window.ui.CompetitorCategories
        table.clear()
        table.setRowCount(len(competitor.get_category()))
        row = 0
        for category in competitor.get_category():
            print(category)
            table.setItem(row, 0, QTableWidgetItem(category.get_age()))
            table.setItem(row, 1, QTableWidgetItem(category.get_gender()))
            table.setItem(row, 2, QTableWidgetItem(category.get_category()))
            row += 1


if __name__ == '__main__':
    op = CategoryAdder(None)
    with pdfplumber.open("1.pdf") as pdf:
        op.parse_pdf(pdf)
