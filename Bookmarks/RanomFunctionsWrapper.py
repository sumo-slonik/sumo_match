import os

import pdfplumber
from PySide2.QtWidgets import QFileDialog


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

        actual_category = None

        for line in lines:
            if line.split()[0] == 'Kobiety' or line.split()[0] == 'Mężczyźni':
                gender = line.split()[0]
                age = line.split()[1:-2]
                weight = line.split()[-2:]
