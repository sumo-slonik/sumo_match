import sys
import os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import itertools
# Import user interface file
from GUI_test.test_kuba.ui_main_window import *
from match_under_16 import *
from GUI_test.test_kuba.functionality.GUI_manipulation import *

WINDOW_SIZE = 0


# Main class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.animation = None
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

        self.ui.left_menu_toggle_button.clicked.connect(lambda: self.slide_left_menu())
        self.ui.HomeButton.clicked.connect(lambda: self.menu_button_function("HomePage"))
        self.ui.AccountButton.clicked.connect(lambda: self.menu_button_function("AccountPage"))
        self.ui.SettingsButton.clicked.connect(lambda: self.menu_button_function("SettingsPage"))
        # Show window
        self.showFullScreen();
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

    def slide_left_menu(self):
        actual_menu_size = self.ui.left_menu.width()
        new_menu_size = 0
        if actual_menu_size == 50:
            new_menu_size = 125
        else:
            new_menu_size = 50
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(actual_menu_size)
        self.animation.setEndValue(new_menu_size)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def menu_button_function(self, go_to):
        if go_to == "HomePage":
            self.ui.stackedWidget.setCurrentWidget(self.ui.HomePage)
        if go_to == "SettingsPage":
            self.ui.stackedWidget.setCurrentWidget(self.ui.SettingsPage)
        if go_to == "AccountPage":
            self.ui.stackedWidget.setCurrentWidget(self.ui.AcountPage)


# Execute app

def make_match_16(main_window):
    # main_window = MainWindow()
    competitors = [PersonalCompetitor(name="Kuba Nowakowski" + str(x),
                                      club="LUKS Lubzina",
                                      weight=105,
                                      is_free_fight=False,
                                      category=100,
                                      birth_year=2000) for x in range(0, 16)]
    matches = Eliminations(competitors)
    all_nodes = ["el_16_node_" + str(x) for x in range(4, 32)]
    v_lvl_nodes = ["el_16_node_" + str(x) for x in range(16, 32)]
    print_eliminations_16(matches, main_window)
    # load_competitors_to_nodes(v_lvl_nodes,competitors,main_window)
    main_window.ui.next_match.clicked.connect(lambda: go_to_next_round(all_nodes, matches, main_window))
    main_window.ui.prev_match.clicked.connect(lambda: matches.go_to_prev_round())
    main_window.ui.win_left.clicked.connect(lambda: make_match(True, matches, main_window))
    main_window.ui.win_right.clicked.connect(lambda: make_match(False, matches, main_window))


def make_match(left_child_win, matches, main_window):
    matches.make_match(left_child_win)
    print_eliminations_16(matches, main_window)


def go_to_next_round(all_nodes, matches, main_window):
    matches.go_to_next_round()
    print_eliminations_16(matches, main_window)
    #colorNodeBorder(matches.actualMatchId, main_window)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    make_match_16(window)
    sys.exit(app.exec_())
else:
    print(__name__, "hh")
# press ctrl+b in sublime to run
