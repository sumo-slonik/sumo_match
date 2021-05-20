import os

import pdfplumber
from PySide2.QtWidgets import QFileDialog

from DataStructures.personal_competitor import Category, PersonalCompetitor


class RandomFunctionWrapper():
    def __init__(self, window):
        self.categories = []
        self.competitors = []
        self.window = window
        self.to_add = []

    def add_category(self):
        files = QFileDialog.getOpenFileNames(self.window, "Dodaj kategorię", os.getcwd(), "Plik PDF (*.pdf)")
        self.to_add = files[0]
        self.window.ui.CategoriesToAdd_2.setText(str(files[0]))

    def confirm_categories(self):
        self.window.ui.CategoriesToAdd_2.setText("")

        for name in self.to_add:
            print("nazwa pliku:", name)
            with pdfplumber.open(name) as pdf:
                self.parse_pdf(pdf)

    def parse_pdf(self, pdf):
        lines = []
        for page in pdf.pages:
            lines += page.extract_text(x_tolerance=3, y_tolerance=3).split('\n')
        actual_category = ''
        result = dict()
        for line in lines:
            if 'Kategoria:' in line:
                category = line[10:].strip().split('-')
                gender = category[0]
                age = category[1]
                weight = category[2]
                actual_category = Category(weight, gender, age)
            else:
                competitor = line.strip().split('|')
                name = competitor[0]
                club = competitor[1]
                licence_no = competitor[2]
                competitor = PersonalCompetitor(name=name, club=club, licence_no=licence_no, category=actual_category)
                if result.get(actual_category,0) == 0:
                    result[actual_category] = (competitor,)
                else:
                    result[actual_category] = result[actual_category] + (competitor,)
        return result


if __name__ == '__main__':
    a = RandomFunctionWrapper(None)
    with pdfplumber.open('D:\sumo_match\Reports\ Mężczyźni _ Kadet (16).pdf') as file:
        res = a.parse_pdf(file)
    for competitor in res:
        print(competitor,res[competitor])
