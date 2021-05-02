import sys
from PySide2 import QtCore, QtGui
from PySide2.QtCore import (QPropertyAnimation)
from PySide2.QtGui import (QColor)
# Import user interface file
from Program_GUI.ui_main_window import *
from match_under_16 import *
from Program_GUI.functionality.GUI_manipulation import *
from competitors_txt_input import personal_competitor_txt_input, divide_competitors_to_teams
from random_functions import random_function_16
from all_match_engine import AllMatchEngine
from match_under_5 import MatchUnder5 as Under5
from category_opener import Opener
from category_adder import CategoryAdder

WINDOW_SIZE = 0


# Main class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.leftMenuAnimation = None
        self.topMenuAnimation = None
        self.rightMenuAnimation = None
        self.SecondLeftMenuAnimation = None
        self.categories_adder = CategoryAdder(self)
        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Button click events to our top bar buttons
        #
        # Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        # Close window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())

        # left menu buttons
        self.ui.Top_menu_slide_button.clicked.connect(lambda: self.slide_upper_menu())
        self.ui.left_menu_toggle_button.clicked.connect(lambda: self.slide_left_menu())
        self.ui.HomeButton.clicked.connect(lambda: self.menu_button_function("HomePage"))
        self.ui.AccountButton.clicked.connect(lambda: self.menu_button_function("AccountPage"))
        self.ui.SettingsButton.clicked.connect(lambda: self.menu_button_function("SettingsPage"))
        self.ui.InfoButton.clicked.connect(lambda: self.slide_communicate())
        self.ui.AddCategoriesButton.clicked.connect(lambda: self.menu_button_function("CompetitorInputPage"))

        # close communicate
        self.ui.CloseCommunicateButton.clicked.connect(lambda: self.slide_communicate())

        # top menu buttons
        self.ui.HalfFinal_button.clicked.connect(lambda: self.top_menu_function("HalfFinals"))
        self.ui.Eliminations_button.clicked.connect(lambda: self.top_menu_function("Eliminations"))
        self.ui.Final_button.clicked.connect(lambda: self.top_menu_function("Finals"))
        self.ui.Repechage_button.clicked.connect(lambda: self.top_menu_function("Repechage"))

        # category_menu
        self.ui.Hide_category_menu.clicked.connect(lambda: self.slide_second_left_menu())
        self.ui.Button_16_competitors.clicked.connect(lambda: self.category_menu_button_function("16"))
        self.ui.Button_5_competitors.clicked.connect(lambda: self.category_menu_button_function("5"))
        self.ui.Button_4_competitors.clicked.connect(lambda: self.category_menu_button_function("4"))
        self.ui.Button_3_competitors.clicked.connect(lambda: self.category_menu_button_function("3"))
        self.ui.Button_2_competitors.clicked.connect(lambda: self.category_menu_button_function("2"))

        # adding_competitor
        self.ui.CategoriesBrowseButton.clicked.connect(lambda: self.categories_adder.add_category())
        self.ui.AddCategoriesButton_2.clicked.connect(lambda: self.categories_adder.confirm_categories())

        # Show window
        self.showFullScreen()
        self.show()

    # Restore or maximize your window
    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE
        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            self.showMaximized()
            # Update button icon
            self.ui.restoreButton.setIcon(QtGui.QIcon(u":/Icons/icons/cil-window-maximize.png"))  # Show maximized icon
        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()
            # Update button icon
            self.ui.restoreButton.setIcon(QtGui.QIcon(u":/Icons/icons/cil-window-restore.png"))  # Show minized icon

    def slide_upper_menu(self):
        actual_menu_size = self.ui.Top_menu.height()
        if actual_menu_size == 0:
            self.ui.Top_menu_slide_button.setIcon(QtGui.QIcon(u":/Icons/icons/cil-arrow-top.png"))
            new_menu_size = 60
        else:
            self.ui.Top_menu_slide_button.setIcon(QtGui.QIcon(u":/Icons/icons/cil-arrow-bottom.png"))
            new_menu_size = 0
        self.topMenuAnimation = QPropertyAnimation(self.ui.Top_menu, b"maximumHeight")
        self.topMenuAnimation.setDuration(350)
        self.topMenuAnimation.setStartValue(actual_menu_size)
        self.topMenuAnimation.setEndValue(new_menu_size)
        self.topMenuAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.topMenuAnimation.start()

    def slide_left_menu(self):
        actual_menu_size = self.ui.left_menu.width()
        new_menu_size = 0
        if actual_menu_size == 50:
            new_menu_size = 225
        else:
            new_menu_size = 50
        self.leftMenuAnimation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.leftMenuAnimation.setDuration(450)
        self.leftMenuAnimation.setStartValue(actual_menu_size)
        self.leftMenuAnimation.setEndValue(new_menu_size)
        self.leftMenuAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.leftMenuAnimation.start()

    def slide_communicate(self):
        actual_size = self.ui.right_menu.width()
        if actual_size == 0:
            new_size = 250
        else:
            new_size = 0
        self.rightMenuAnimation = QPropertyAnimation(self.ui.right_menu, b"minimumWidth")
        self.rightMenuAnimation.setDuration(450)
        self.rightMenuAnimation.setStartValue(actual_size)
        self.rightMenuAnimation.setEndValue(new_size)
        self.rightMenuAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.rightMenuAnimation.start()

    def slide_second_left_menu(self):
        actual_menu_size = self.ui.Second_left_menu.width()
        new_menu_size = 0
        if actual_menu_size == 0:
            new_menu_size = 60
        else:
            new_menu_size = 0
        self.SecondLeftMenuAnimation = QPropertyAnimation(self.ui.Second_left_menu, b"minimumWidth")
        self.SecondLeftMenuAnimation.setDuration(450)
        self.SecondLeftMenuAnimation.setStartValue(actual_menu_size)
        self.SecondLeftMenuAnimation.setEndValue(new_menu_size)
        self.SecondLeftMenuAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.SecondLeftMenuAnimation.start()

    def menu_button_function(self, go_to):
        if go_to == "HomePage":
            self.ui.stackedWidget.setCurrentWidget(self.ui.HomePage)
        if go_to == "SettingsPage":
            self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)
        if go_to == "AccountPage":
            self.ui.stackedWidget.setCurrentWidget(self.ui.AcountPage)
            self.slide_second_left_menu()
        if go_to == 'CompetitorInputPage':
            self.ui.stackedWidget.setCurrentWidget(self.ui.CompetitorInputPage)

    def top_menu_function(self, go_to):
        if go_to == "Eliminations":
            self.ui.match_16.setCurrentWidget(self.ui.Eliminations)
        if go_to == "HalfFinals":
            self.ui.match_16.setCurrentWidget(self.ui.HalfFinals)
        if go_to == "Finals":
            self.ui.match_16.setCurrentWidget(self.ui.Finals)
        if go_to == "Repechage":
            self.ui.match_16.setCurrentWidget(self.ui.Repechage)

    def category_menu_button_function(self, go_to):
        if go_to == "16":
            self.ui.AllMatchesWraper.setCurrentWidget(self.ui.MatchUnder16)
            self.ui.match_16.setCurrentWidget(self.ui.Eliminations)
        if go_to == "5":
            self.ui.AllMatchesWraper.setCurrentWidget(self.ui.MatchUnder5)
            self.ui.match_5.setCurrentWidget(self.ui.under_5)
        if go_to == "4":
            self.ui.AllMatchesWraper.setCurrentWidget(self.ui.MatchUnder5)
            self.ui.match_5.setCurrentWidget(self.ui.under_4)
        if go_to == "3":
            self.ui.AllMatchesWraper.setCurrentWidget(self.ui.MatchUnder5)
            self.ui.match_5.setCurrentWidget(self.ui.under_3)
        if go_to == "2":
            self.ui.AllMatchesWraper.setCurrentWidget(self.ui.MatchUnder5)
            self.ui.match_5.setCurrentWidget(self.ui.Under2)


# # Execute app
#
# def make_match_16(main_window):
#     competitors = personal_competitor_txt_input("Competitors.txt")
#
#     # test funkcji losującej
#     teams = divide_competitors_to_teams(competitors)
#     contestants = random_function_16.random_function_16(teams, len(competitors) - 4)
#
#     # matches = Eliminations(competitors)
#     matches = MatchUnder16(contestants)
#     # print_eliminations_16(matches, main_window)
#     print_match_under_16(matches, main_window)


def connect_gui_to_engine(main_window, all_match_engine):
    def make_match(left_child_win, engine, window):
        engine.print_match(window)
        engine.make_match(left_child_win)
        engine.print_match(window)

    def go_to_next_round(engine, window):
        engine.go_to_next_round()
        engine.print_match(window)

    main_window.ui.next_match.clicked.connect(lambda: go_to_next_round(all_match_engine, main_window))
    main_window.ui.prev_match.clicked.connect(lambda: all_match_engine.go_to_prev_round())
    main_window.ui.win_left.clicked.connect(lambda: make_match(True, all_match_engine, main_window))
    main_window.ui.win_right.clicked.connect(lambda: make_match(False, all_match_engine, main_window))
    engine.print_match(window)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    # competitors = personal_competitor_txt_input("Competitors.txt")
    # teams = divide_competitors_to_teams(competitors)
    # competitors = random_function_16.random_function_16(teams, len(competitors) - 4)
    competitors = [PersonalCompetitor("Kuba " + str(x)) for x in range(4)]
    window = MainWindow()
    adder = CategoryAdder(window)
    Opener("Categories", window).add_category_buttons()
    engine = AllMatchEngine(competitors)
    connect_gui_to_engine(window, engine)
    sys.exit(app.exec_())

else:
    print(__name__, "hh")
