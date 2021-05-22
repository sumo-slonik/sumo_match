import os

import pdfplumber
from PySide2.QtWidgets import QFileDialog, QTableWidgetItem

from DataStructures.personal_competitor import Category, PersonalCompetitor
from Matches.types_of_matches import TypeOFMatch, correctTypeFromLength
# from Program_GUI.functionality.GUI_manipulation import print_randomisation_results
from Program_GUI.functionality.GUI_manipulation import print_randomisation_results
from random_functions.random_function_10 import random_function_10
from random_functions.random_function_16 import random_function_16
from DataStructures.SupportingFunctions.competitors_txt_input import divide_competitors_to_teams


class RandomFunctionWrapper():
    def __init__(self, window):
        self.categories = dict()
        self.window = window
        self.to_add = []
        self.actual_category = {'master': None, 'runner_up': None, 'Category': None}
        self.actual_competitor = None
        self.actual_results = None
        self.actual_name = None

    def add_category(self):
        files = QFileDialog.getOpenFileNames(self.window, "Dodaj kategorię", os.getcwd(), "Plik PDF (*.pdf)")
        self.to_add = files[0]
        self.window.ui.CategoriesToAdd_2.setText(str(files[0]))

    def select_competitor(self, licence_no):
        self.actual_competitor = \
            list(filter(lambda x: x.get_licence_no() == licence_no, self.actual_category['Category']))[0]
        print(self.actual_competitor)

    def make_master(self):
        self.actual_category['master'] = self.actual_competitor
        if self.actual_category['runner_up'] == self.actual_competitor:
            self.actual_category['runner_up'] = None

    def make_runner_up(self):
        self.actual_category['runner_up'] = self.actual_competitor
        if self.actual_category['master'] == self.actual_competitor:
            self.actual_category['master'] = None

    def print_categories(self):
        table = self.window.ui.CategoriesTable
        table.setRowCount(0)
        table_width = table.width()
        table.setColumnWidth(0, (table_width - 25) / 3)
        table.setColumnWidth(1, (table_width - 25) / 3)
        table.setColumnWidth(2, (table_width - 25) / 3)

        table.setRowCount(len(self.categories))
        row = 0
        for category in self.categories:
            table.setItem(row, 0, QTableWidgetItem(category.get_gender()))
            table.setItem(row, 1, QTableWidgetItem(category.get_age()))
            table.setItem(row, 2, QTableWidgetItem(category.get_category()))
            row += 1

    def confirm_categories(self):
        self.window.ui.CategoriesToAdd_2.setText("")
        for name in self.to_add:
            print("nazwa pliku:", name)
            with pdfplumber.open(name) as pdf:
                self.categories.update(self.parse_pdf(pdf))

        # ///////////////////
        # to del
        self.actual_category['Category'] = next(iter(self.categories.values()))
        self.print_actual_category()
        # ///////////////////

        self.print_categories()

    def make_randomization(self):
        print("ranomization")

        counter = 0
        result = []
        runnerUp = self.actual_category['runner_up']
        master = self.actual_category['master']
        competitors = [i for i in self.actual_category['Category']]
        print(competitors)
        print(master)
        print(runnerUp)
        print('__________________')
        for i in competitors:
            print(i)
        print('__________________')

        if master:
            competitors.remove(master)
            counter += 1
        if runnerUp:
            competitors.remove(runnerUp)
            counter += 1
        counter += len(competitors)
        print(counter)
        type_of_match = correctTypeFromLength(counter)
        print('cosik')
        print(competitors)
        teams = divide_competitors_to_teams(competitors)
        if type_of_match == TypeOFMatch.Under5:
            print("under_5")
            if master:
                result.append(master)
            if runnerUp:
                result.append(runnerUp)
            while competitors:
                print(1)
                result.append(competitors.pop())
        elif type_of_match == TypeOFMatch.Under10:
            print("under_10")
            result = random_function_10(teams, len(competitors), master, runnerUp)
            print("wycodzę z 10")
        elif type_of_match == TypeOFMatch.Under16:
            print("under_16")
            result = random_function_16(teams, len(competitors), master, runnerUp)
            print("wycodzę z 16")

        print_randomisation_results(self.window, result, type_of_match)
        self.actual_results = result
        for i in result:
            print(i)

    def save_to_txt(self):
        if self.actual_results is not None:
            with open('Categories/'+self.actual_name + '.txt', "w",encoding="utf-8") as file:
                to_print = []
                if isinstance(self.actual_results[0], list):
                    to_print = self.actual_results[0] + self.actual_results[1]
                else:
                    to_print = self.actual_results
                for competitor in to_print:
                    file.write(
                        competitor.get_surname() + ' ' + competitor.get_first_name() + ';' + competitor.get_club() + ';\n')

    def select_category(self, category):
        self.actual_name = category.gender[0] + category.age + category.category
        self.actual_category['Category'] = self.categories[category]
        self.actual_category['runner_up'] = None
        self.actual_category['master'] = None
        self.print_actual_category()

    def print_actual_category(self):
        competitors = self.actual_category['Category']
        print(competitors)
        print("powinno być ", len(self.actual_category['Category']))
        table = self.window.ui.Competitors_table

        table.setRowCount(0)
        table_width = table.width()
        table.setColumnWidth(0, table_width / 3)
        table.setColumnWidth(1, table_width / 3)
        table.setColumnWidth(2, table_width / 3)

        table.setRowCount(len(competitors))
        row = 0
        for competitor in competitors:
            table.setItem(row, 0, QTableWidgetItem(competitor.get_first_name()))
            table.setItem(row, 1, QTableWidgetItem(competitor.get_surname()))
            table.setItem(row, 2, QTableWidgetItem(competitor.get_licence_no()))
            row += 1

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
                if result.get(actual_category, 0) == 0:
                    result[actual_category] = (competitor,)
                else:
                    result[actual_category] = result[actual_category] + (competitor,)
        return result


if __name__ == '__main__':
    a = RandomFunctionWrapper(None)
    with pdfplumber.open('D:\sumo_match\Reports\ Mężczyźni _ Kadet (16).pdf') as file:
        res = a.parse_pdf(file)
    for competitor in res:
        print(competitor, len(res[competitor]))
