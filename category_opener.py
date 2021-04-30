import os

from PySide2.QtCore import QCoreApplication
from PySide2.QtWidgets import QPushButton


class Opener():
    def __init__(self, path, window):
        self.window = window
        self.path = path
        self.category_files = os.walk(self.path, False).__next__()[2]
        print(self.category_files)

    def add_category_buttons(self):
        for file_name in self.category_files:
            new_button = QPushButton(self.window.ui.Second_left_menu)
            new_button.setObjectName(file_name)
            self.window.ui.verticalLayout_41.addWidget(new_button)
            new_button.setText(QCoreApplication.translate("MainWindow", file_name, None))
            new_button.show()

if __name__ == '__main__':
    a = Opener("Categories", None)
    a.add_category_buttons()
