import os

import pdfplumber
from PySide2.QtWidgets import QTableWidgetItem

from DataStructures.personal_competitor import PersonalCompetitor, Category


class RapportBrowser:
    def __init__(self, window):
        self.rapport_set = set()
        self.category_files = os.walk('Reports/Results', False).__next__()[2]
        print(self.category_files)
        self.window = window
        self.window.ui.ResultsBox.clear()
        self.window.ui.ResultsBox.addItems(self.category_files)
        self.table = self.window.ui.ResultsTable


    def open_pdf(self):
        name = 'Reports/Results/' + self.window.ui.ResultsBox.currentText()
        self.print_competitors_in_table(self.parse_pdf(name))

    def print_competitors_in_table(self, competitors):
        table = self.table
        table.setRowCount(0)
        table_width = table.width()
        table.setColumnWidth(0, (table_width) / 4)
        table.setColumnWidth(1, (table_width) / 4)
        table.setColumnWidth(2, (table_width) / 4)
        table.setColumnWidth(3, (table_width) / 4)
        table.setRowCount(len(competitors))
        row = 0
        for competitor in competitors:
            table.setItem(row, 0, QTableWidgetItem(competitor.get_first_name()))
            table.setItem(row, 1, QTableWidgetItem(competitor.get_surname()))
            table.setItem(row, 2, QTableWidgetItem(competitor.get_club()))
            table.setItem(row, 3, QTableWidgetItem(competitor.get_licence_no()))
            row += 1

    def parse_pdf(self, name):
        lines = []
        results = []
        with pdfplumber.open(name) as pdf:
            for page in pdf.pages:
                lines += page.extract_text(x_tolerance=3, y_tolerance=3).split('\n')
            actual_category = ''
            for line in lines:
                if 'Kategoria:' in line:
                    pass
                else:
                    competitor = line.strip().split('.')[1]
                    competitor = competitor.strip().split('|')
                    name = competitor[0].split(' ')
                    name = name[1]+' '+name[0]
                    club = competitor[1]
                    licence_no = competitor[2]
                    competitor = PersonalCompetitor(name=name, club=club, licence_no=licence_no,
                                                    category=actual_category)
                    results.append(competitor)
            return results


if __name__ == '__main__':
    pass
    # RapportBrowser()
