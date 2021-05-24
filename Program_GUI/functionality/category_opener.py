import os

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QPushButton
from DataStructures.SupportingFunctions.competitors_txt_input import personal_competitor_txt_input, \
    club_competitor_txt_input
from Matches.all_match_engine import AllMatchEngine
from Program_GUI.functionality.ConnectGuiToEngine import connect_gui_to_engine
from functools import partial
from copy import copy


class Opener:
    def __init__(self, path, window):
        self.window = window
        self.path = path
        self.category_files = os.walk(self.path, False).__next__()[2]
        self.used = []

        print(self.category_files)

    def open_category(self, patch):
        print('____________', patch)
        with open('Categories/'+patch, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                line = line.split()
                if line[0] == 'klub':
                    competitors = club_competitor_txt_input('Categories/' + patch)
                else:
                    competitors = personal_competitor_txt_input('Categories/' + patch)
                break
        engine = AllMatchEngine(competitors,self.window,patch[:-4])
        self.window.AllMatchEngine = engine
        # connect_gui_to_engine(self.window, engine)

    def add_category_buttons(self):
        for file_name in self.category_files:
            if file_name not in self.used:
                new_button = QPushButton(self.window.ui.Second_left_menu)
                new_button.setObjectName(file_name)
                self.window.ui.verticalLayout_41.addWidget(new_button)
                new_button.setText(QCoreApplication.translate("MainWindow", file_name, None))
                new_button.show()
                new_button.clicked.connect(partial(lambda file_name : self.open_category(file_name),file_name = file_name))
                self.used.append(file_name)
                print(file_name)
        # self.buttons[-1].clicked.connect(lambda: print('xd'))
        # self.buttons[-2].clicked.connect(lambda: print('no'))


if __name__ == '__main__':
    a = Opener("Categories", None)
    a.add_category_buttons()
