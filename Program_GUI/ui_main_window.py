# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowdAqNdS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 831)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(47, 47, 47);\n"
"}")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setMaximumSize(QSize(16777215, 50))
        self.title_bar_container.setStyleSheet(u"")
        self.title_bar_container.setFrameShape(QFrame.StyledPanel)
        self.title_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.title_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.title_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet(u"\n"
"QPushButton{\n"
"	padding: 5px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(47, 47, 47);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}\n"
"QFrame\n"
"{\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"")
        self.left_menu_toggle.setFrameShape(QFrame.NoFrame)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle_button = QPushButton(self.left_menu_toggle)
        self.left_menu_toggle_button.setObjectName(u"left_menu_toggle_button")
        self.left_menu_toggle_button.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/Icons/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.left_menu_toggle_button.setIcon(icon)
        self.left_menu_toggle_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.left_menu_toggle_button)


        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.title_bar = QFrame(self.title_bar_container)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.title_bar)


        self.horizontalLayout_2.addWidget(self.title_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(100, 16777215))
        self.top_right_btns.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.top_right_btns.setFrameShape(QFrame.WinPanel)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_right_btns)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setStyleSheet(u"QPushButton{\n"
"border-radius 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/icons/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.top_right_btns)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setStyleSheet(u"QPushButton{\n"
"border-radius 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/icons/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon2)
        self.restoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.top_right_btns)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setStyleSheet(u"QPushButton{\n"
"border-radius 5px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/icons/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon3)
        self.closeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setEnabled(True)
        self.main_body.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(47, 47, 47);\n"
"}")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(50, 16777215))
        self.left_menu.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	padding: 25px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(47, 47, 47);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, -1, -1, -1)
        self.HomeButton = QPushButton(self.frame)
        self.HomeButton.setObjectName(u"HomeButton")
        self.HomeButton.setMinimumSize(QSize(100, 0))
        self.HomeButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-home.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"padding-left: 50px;\n"
"\n"
"")

        self.verticalLayout_42.addWidget(self.HomeButton)

        self.AccountButton = QPushButton(self.frame)
        self.AccountButton.setObjectName(u"AccountButton")
        self.AccountButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-folder-open.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"")

        self.verticalLayout_42.addWidget(self.AccountButton)

        self.AddCategoriesButton = QPushButton(self.frame)
        self.AddCategoriesButton.setObjectName(u"AddCategoriesButton")
        self.AddCategoriesButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-user-follow.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"")

        self.verticalLayout_42.addWidget(self.AddCategoriesButton)

        self.AccountButton_3 = QPushButton(self.frame)
        self.AccountButton_3.setObjectName(u"AccountButton_3")
        self.AccountButton_3.setStyleSheet(u"background-image: url(:/Icons/icons/cil-description.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"")

        self.verticalLayout_42.addWidget(self.AccountButton_3)

        self.RandomFunctionsButton = QPushButton(self.frame)
        self.RandomFunctionsButton.setObjectName(u"RandomFunctionsButton")
        self.RandomFunctionsButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-reload.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"")

        self.verticalLayout_42.addWidget(self.RandomFunctionsButton)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.InfoButton = QPushButton(self.left_menu)
        self.InfoButton.setObjectName(u"InfoButton")
        self.InfoButton.setMinimumSize(QSize(100, 0))
        self.InfoButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-comment-square.png);\n"
"background-repeat:none;\n"
"padding-left: 50px;\n"
"background-position: center left;\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.InfoButton)

        self.SettingsButton = QPushButton(self.left_menu)
        self.SettingsButton.setObjectName(u"SettingsButton")
        self.SettingsButton.setMinimumSize(QSize(100, 0))
        self.SettingsButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-settings.png);\n"
"background-repeat:none;\n"
"padding-left: 50px;\n"
"background-position: center left;\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.SettingsButton)


        self.horizontalLayout.addWidget(self.left_menu)

        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setMinimumSize(QSize(0, 0))
        self.center_main_items.setStyleSheet(u"background-color: \n"
"\n"
"\n"
"\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(83, 83, 83, 255), stop:0.9801 rgba(32, 32, 32, 255))\n"
"\n"
"\n"
"\n"
"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.center_main_items)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Second_left_menu = QFrame(self.center_main_items)
        self.Second_left_menu.setObjectName(u"Second_left_menu")
        self.Second_left_menu.setMinimumSize(QSize(0, 0))
        self.Second_left_menu.setMaximumSize(QSize(0, 16777215))
        self.Second_left_menu.setStyleSheet(u"QFrame {\n"
"	background:transparent;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"\n"
"	background-color: rgb(98, 98, 98);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
" 	border-radius: 2px;\n"
"	border-color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}")
        self.Second_left_menu.setFrameShape(QFrame.StyledPanel)
        self.Second_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.Second_left_menu)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.Hide_category_menu = QPushButton(self.Second_left_menu)
        self.Hide_category_menu.setObjectName(u"Hide_category_menu")
        self.Hide_category_menu.setMinimumSize(QSize(0, 50))
        self.Hide_category_menu.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/cil-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Hide_category_menu.setIcon(icon4)

        self.verticalLayout_41.addWidget(self.Hide_category_menu)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_41.addItem(self.verticalSpacer)

        self.Button_16_competitors = QPushButton(self.Second_left_menu)
        self.Button_16_competitors.setObjectName(u"Button_16_competitors")

        self.verticalLayout_41.addWidget(self.Button_16_competitors)

        self.Button_10_competitors = QPushButton(self.Second_left_menu)
        self.Button_10_competitors.setObjectName(u"Button_10_competitors")

        self.verticalLayout_41.addWidget(self.Button_10_competitors)

        self.Button_5_competitors = QPushButton(self.Second_left_menu)
        self.Button_5_competitors.setObjectName(u"Button_5_competitors")

        self.verticalLayout_41.addWidget(self.Button_5_competitors)

        self.Button_4_competitors = QPushButton(self.Second_left_menu)
        self.Button_4_competitors.setObjectName(u"Button_4_competitors")

        self.verticalLayout_41.addWidget(self.Button_4_competitors)

        self.Button_3_competitors = QPushButton(self.Second_left_menu)
        self.Button_3_competitors.setObjectName(u"Button_3_competitors")

        self.verticalLayout_41.addWidget(self.Button_3_competitors)

        self.Button_2_competitors = QPushButton(self.Second_left_menu)
        self.Button_2_competitors.setObjectName(u"Button_2_competitors")

        self.verticalLayout_41.addWidget(self.Button_2_competitors)

        self.pushButton_7 = QPushButton(self.Second_left_menu)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_41.addWidget(self.pushButton_7)

        self.verticalSpacer_2 = QSpacerItem(20, 486, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_2)


        self.gridLayout.addWidget(self.Second_left_menu, 0, 0, 1, 1, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 50))
        self.stackedWidget.setStyleSheet(u"QFrame {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTextEdit {\n"
"   \n"
"	background-color: rgb(217, 217, 217);\n"
" 	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(30, 30, 30);\n"
" 	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	color: rgb(185, 185, 185);\n"
"	font: 75 26pt \"Calibri\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(47, 47, 47);\n"
"	font: 255 8pt \"Calibri\";\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(150, 150, 150);\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QTableWidget {\n"
"	background-color: rgb(100, 100, 100);\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"	font: 255 8pt \"Calibri\";\n"
""
                        "	color: white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(99, 99, 99);\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color:rgb(150, 150, 150);\n"
"}\n"
"")
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.HomePage.setStyleSheet(u"")
        self.stackedWidget.addWidget(self.HomePage)
        self.RandomCompetitors = QWidget()
        self.RandomCompetitors.setObjectName(u"RandomCompetitors")
        self.RandomCompetitors.setStyleSheet(u"QPushButton{	\n"
"\n"
"	font: 75 11pt \"Calibri\";\n"
"	color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QWidget{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QTextEdit {\n"
"   \n"
"	background-color: rgb(217, 217, 217);\n"
" 	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	background-color: rgb(30, 30, 30);\n"
" 	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(157, 157, 157);\n"
"	color: rgb(0, 0, 0,)\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	color: rgb(185, 185, 185);\n"
"	font: 75 26pt \"Calibri\";\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(47, 47, 47);\n"
"	font: 255 8pt \"Calibri\";\n"
"	color: white;\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(150, 150, 150);\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QTableWidget {\n"
"	background-color: rgb(100, 100, 100);\n"
""
                        "	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"	font: 255 8pt \"Calibri\";\n"
"	color: white;\n"
"	\n"
"}")
        self.horizontalLayout_13 = QHBoxLayout(self.RandomCompetitors)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_132 = QFrame(self.RandomCompetitors)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMaximumSize(QSize(300, 16777215))
        self.frame_132.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(61, 61, 61);\n"
"}")
        self.frame_132.setFrameShape(QFrame.StyledPanel)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_132)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.label_36 = QLabel(self.frame_132)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet(u"font: 75 16pt \"Calibri\";")

        self.verticalLayout_100.addWidget(self.label_36)

        self.frame_223 = QFrame(self.frame_132)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setMinimumSize(QSize(250, 300))
        self.frame_223.setMaximumSize(QSize(16777215, 16777215))
        self.frame_223.setFrameShape(QFrame.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.frame_223)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.frame_224 = QFrame(self.frame_223)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setFrameShape(QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_224)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.CategoriesToAdd_2 = QLineEdit(self.frame_224)
        self.CategoriesToAdd_2.setObjectName(u"CategoriesToAdd_2")

        self.horizontalLayout_83.addWidget(self.CategoriesToAdd_2)

        self.CategoriesBrowseButton_2 = QPushButton(self.frame_224)
        self.CategoriesBrowseButton_2.setObjectName(u"CategoriesBrowseButton_2")

        self.horizontalLayout_83.addWidget(self.CategoriesBrowseButton_2)


        self.verticalLayout_172.addWidget(self.frame_224)

        self.frame_225 = QFrame(self.frame_223)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setFrameShape(QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_225)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.AddCategoriesButton_3 = QPushButton(self.frame_225)
        self.AddCategoriesButton_3.setObjectName(u"AddCategoriesButton_3")

        self.horizontalLayout_84.addWidget(self.AddCategoriesButton_3)


        self.verticalLayout_172.addWidget(self.frame_225)


        self.verticalLayout_100.addWidget(self.frame_223)

        self.frame_271 = QFrame(self.frame_132)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setMinimumSize(QSize(250, 0))
        self.frame_271.setStyleSheet(u"")
        self.frame_271.setFrameShape(QFrame.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Raised)
        self.verticalLayout_212 = QVBoxLayout(self.frame_271)
        self.verticalLayout_212.setObjectName(u"verticalLayout_212")
        self.label_54 = QLabel(self.frame_271)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)
        self.label_54.setStyleSheet(u"font: 75 16pt \"Calibri\";")

        self.verticalLayout_212.addWidget(self.label_54)

        self.CategoriesTable = QTableWidget(self.frame_271)
        if (self.CategoriesTable.columnCount() < 3):
            self.CategoriesTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.CategoriesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.CategoriesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.CategoriesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.CategoriesTable.setObjectName(u"CategoriesTable")
        self.CategoriesTable.setStyleSheet(u"QTableWidget {\n"
"	background-color: rgb(100, 100, 100);\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"	font: 255 8pt \"Calibri\";\n"
"	color: white;\n"
"	\n"
"}")

        self.verticalLayout_212.addWidget(self.CategoriesTable)


        self.verticalLayout_100.addWidget(self.frame_271)


        self.horizontalLayout_13.addWidget(self.frame_132)

        self.frame_272 = QFrame(self.RandomCompetitors)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setFrameShape(QFrame.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Raised)
        self.verticalLayout_214 = QVBoxLayout(self.frame_272)
        self.verticalLayout_214.setObjectName(u"verticalLayout_214")
        self.frame_273 = QFrame(self.frame_272)
        self.frame_273.setObjectName(u"frame_273")
        self.frame_273.setFrameShape(QFrame.StyledPanel)
        self.frame_273.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_273)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.tableWidget_2 = QTableWidget(self.frame_273)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_43.addWidget(self.tableWidget_2)

        self.stackedWidget_2 = QStackedWidget(self.frame_273)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"")
        self.RandomFunctionRes16 = QWidget()
        self.RandomFunctionRes16.setObjectName(u"RandomFunctionRes16")
        self.verticalLayout_213 = QVBoxLayout(self.RandomFunctionRes16)
        self.verticalLayout_213.setObjectName(u"verticalLayout_213")
        self.label_72 = QLabel(self.RandomFunctionRes16)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_213.addWidget(self.label_72)

        self.frame_275 = QFrame(self.RandomFunctionRes16)
        self.frame_275.setObjectName(u"frame_275")
        self.frame_275.setFrameShape(QFrame.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_275)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.frame_277 = QFrame(self.frame_275)
        self.frame_277.setObjectName(u"frame_277")
        self.frame_277.setFrameShape(QFrame.StyledPanel)
        self.frame_277.setFrameShadow(QFrame.Raised)
        self.verticalLayout_216 = QVBoxLayout(self.frame_277)
        self.verticalLayout_216.setObjectName(u"verticalLayout_216")
        self.RandRes16_1 = QTextEdit(self.frame_277)
        self.RandRes16_1.setObjectName(u"RandRes16_1")

        self.verticalLayout_216.addWidget(self.RandRes16_1)

        self.RandRes16_2 = QTextEdit(self.frame_277)
        self.RandRes16_2.setObjectName(u"RandRes16_2")

        self.verticalLayout_216.addWidget(self.RandRes16_2)

        self.RandRes16_3 = QTextEdit(self.frame_277)
        self.RandRes16_3.setObjectName(u"RandRes16_3")

        self.verticalLayout_216.addWidget(self.RandRes16_3)

        self.RandRes16_4 = QTextEdit(self.frame_277)
        self.RandRes16_4.setObjectName(u"RandRes16_4")

        self.verticalLayout_216.addWidget(self.RandRes16_4)


        self.horizontalLayout_90.addWidget(self.frame_277)

        self.frame_279 = QFrame(self.frame_275)
        self.frame_279.setObjectName(u"frame_279")
        self.frame_279.setFrameShape(QFrame.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Raised)
        self.verticalLayout_217 = QVBoxLayout(self.frame_279)
        self.verticalLayout_217.setObjectName(u"verticalLayout_217")
        self.RandRes16_9 = QTextEdit(self.frame_279)
        self.RandRes16_9.setObjectName(u"RandRes16_9")

        self.verticalLayout_217.addWidget(self.RandRes16_9)

        self.RandRes16_10 = QTextEdit(self.frame_279)
        self.RandRes16_10.setObjectName(u"RandRes16_10")

        self.verticalLayout_217.addWidget(self.RandRes16_10)

        self.RandRes16_11 = QTextEdit(self.frame_279)
        self.RandRes16_11.setObjectName(u"RandRes16_11")

        self.verticalLayout_217.addWidget(self.RandRes16_11)

        self.RandRes16_12 = QTextEdit(self.frame_279)
        self.RandRes16_12.setObjectName(u"RandRes16_12")

        self.verticalLayout_217.addWidget(self.RandRes16_12)


        self.horizontalLayout_90.addWidget(self.frame_279)


        self.verticalLayout_213.addWidget(self.frame_275)

        self.frame_276 = QFrame(self.RandomFunctionRes16)
        self.frame_276.setObjectName(u"frame_276")
        self.frame_276.setFrameShape(QFrame.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_276)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.frame_278 = QFrame(self.frame_276)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setFrameShape(QFrame.StyledPanel)
        self.frame_278.setFrameShadow(QFrame.Raised)
        self.verticalLayout_218 = QVBoxLayout(self.frame_278)
        self.verticalLayout_218.setObjectName(u"verticalLayout_218")
        self.RandRes16_5 = QTextEdit(self.frame_278)
        self.RandRes16_5.setObjectName(u"RandRes16_5")

        self.verticalLayout_218.addWidget(self.RandRes16_5)

        self.RandRes16_6 = QTextEdit(self.frame_278)
        self.RandRes16_6.setObjectName(u"RandRes16_6")

        self.verticalLayout_218.addWidget(self.RandRes16_6)

        self.RandRes16_7 = QTextEdit(self.frame_278)
        self.RandRes16_7.setObjectName(u"RandRes16_7")

        self.verticalLayout_218.addWidget(self.RandRes16_7)

        self.RandRes16_8 = QTextEdit(self.frame_278)
        self.RandRes16_8.setObjectName(u"RandRes16_8")

        self.verticalLayout_218.addWidget(self.RandRes16_8)


        self.horizontalLayout_91.addWidget(self.frame_278)

        self.frame_280 = QFrame(self.frame_276)
        self.frame_280.setObjectName(u"frame_280")
        self.frame_280.setFrameShape(QFrame.StyledPanel)
        self.frame_280.setFrameShadow(QFrame.Raised)
        self.verticalLayout_219 = QVBoxLayout(self.frame_280)
        self.verticalLayout_219.setObjectName(u"verticalLayout_219")
        self.RandRes16_13 = QTextEdit(self.frame_280)
        self.RandRes16_13.setObjectName(u"RandRes16_13")

        self.verticalLayout_219.addWidget(self.RandRes16_13)

        self.RandRes16_14 = QTextEdit(self.frame_280)
        self.RandRes16_14.setObjectName(u"RandRes16_14")

        self.verticalLayout_219.addWidget(self.RandRes16_14)

        self.RandRes16_15 = QTextEdit(self.frame_280)
        self.RandRes16_15.setObjectName(u"RandRes16_15")

        self.verticalLayout_219.addWidget(self.RandRes16_15)

        self.RandRes16_16 = QTextEdit(self.frame_280)
        self.RandRes16_16.setObjectName(u"RandRes16_16")

        self.verticalLayout_219.addWidget(self.RandRes16_16)


        self.horizontalLayout_91.addWidget(self.frame_280)


        self.verticalLayout_213.addWidget(self.frame_276)

        self.stackedWidget_2.addWidget(self.RandomFunctionRes16)
        self.RandomFunctionRes10 = QWidget()
        self.RandomFunctionRes10.setObjectName(u"RandomFunctionRes10")
        self.verticalLayout_220 = QVBoxLayout(self.RandomFunctionRes10)
        self.verticalLayout_220.setObjectName(u"verticalLayout_220")
        self.frame_281 = QFrame(self.RandomFunctionRes10)
        self.frame_281.setObjectName(u"frame_281")
        self.frame_281.setFrameShape(QFrame.StyledPanel)
        self.frame_281.setFrameShadow(QFrame.Raised)
        self.verticalLayout_224 = QVBoxLayout(self.frame_281)
        self.verticalLayout_224.setObjectName(u"verticalLayout_224")
        self.label_73 = QLabel(self.frame_281)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout_224.addWidget(self.label_73)

        self.label_55 = QLabel(self.frame_281)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_224.addWidget(self.label_55)

        self.RandRes10_1 = QTextEdit(self.frame_281)
        self.RandRes10_1.setObjectName(u"RandRes10_1")

        self.verticalLayout_224.addWidget(self.RandRes10_1)

        self.RandRes10_2 = QTextEdit(self.frame_281)
        self.RandRes10_2.setObjectName(u"RandRes10_2")

        self.verticalLayout_224.addWidget(self.RandRes10_2)

        self.RandRes10_3 = QTextEdit(self.frame_281)
        self.RandRes10_3.setObjectName(u"RandRes10_3")

        self.verticalLayout_224.addWidget(self.RandRes10_3)

        self.RandRes10_4 = QTextEdit(self.frame_281)
        self.RandRes10_4.setObjectName(u"RandRes10_4")

        self.verticalLayout_224.addWidget(self.RandRes10_4)

        self.RandRes10_5 = QTextEdit(self.frame_281)
        self.RandRes10_5.setObjectName(u"RandRes10_5")

        self.verticalLayout_224.addWidget(self.RandRes10_5)


        self.verticalLayout_220.addWidget(self.frame_281)

        self.frame_282 = QFrame(self.RandomFunctionRes10)
        self.frame_282.setObjectName(u"frame_282")
        self.frame_282.setFrameShape(QFrame.StyledPanel)
        self.frame_282.setFrameShadow(QFrame.Raised)
        self.verticalLayout_225 = QVBoxLayout(self.frame_282)
        self.verticalLayout_225.setObjectName(u"verticalLayout_225")
        self.label_57 = QLabel(self.frame_282)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_225.addWidget(self.label_57)

        self.RandRes10_6 = QTextEdit(self.frame_282)
        self.RandRes10_6.setObjectName(u"RandRes10_6")

        self.verticalLayout_225.addWidget(self.RandRes10_6)

        self.RandRes10_7 = QTextEdit(self.frame_282)
        self.RandRes10_7.setObjectName(u"RandRes10_7")

        self.verticalLayout_225.addWidget(self.RandRes10_7)

        self.RandRes10_8 = QTextEdit(self.frame_282)
        self.RandRes10_8.setObjectName(u"RandRes10_8")

        self.verticalLayout_225.addWidget(self.RandRes10_8)

        self.RandRes10_9 = QTextEdit(self.frame_282)
        self.RandRes10_9.setObjectName(u"RandRes10_9")

        self.verticalLayout_225.addWidget(self.RandRes10_9)

        self.RandRes10_10 = QTextEdit(self.frame_282)
        self.RandRes10_10.setObjectName(u"RandRes10_10")

        self.verticalLayout_225.addWidget(self.RandRes10_10)


        self.verticalLayout_220.addWidget(self.frame_282)

        self.stackedWidget_2.addWidget(self.RandomFunctionRes10)
        self.RandomFunctionRes5 = QWidget()
        self.RandomFunctionRes5.setObjectName(u"RandomFunctionRes5")
        self.verticalLayout_226 = QVBoxLayout(self.RandomFunctionRes5)
        self.verticalLayout_226.setObjectName(u"verticalLayout_226")
        self.label_74 = QLabel(self.RandomFunctionRes5)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_226.addWidget(self.label_74)

        self.RandRes5_1 = QTextEdit(self.RandomFunctionRes5)
        self.RandRes5_1.setObjectName(u"RandRes5_1")

        self.verticalLayout_226.addWidget(self.RandRes5_1)

        self.RandRes5_2 = QTextEdit(self.RandomFunctionRes5)
        self.RandRes5_2.setObjectName(u"RandRes5_2")

        self.verticalLayout_226.addWidget(self.RandRes5_2)

        self.RandRes5_3 = QTextEdit(self.RandomFunctionRes5)
        self.RandRes5_3.setObjectName(u"RandRes5_3")

        self.verticalLayout_226.addWidget(self.RandRes5_3)

        self.RandRes5_4 = QTextEdit(self.RandomFunctionRes5)
        self.RandRes5_4.setObjectName(u"RandRes5_4")

        self.verticalLayout_226.addWidget(self.RandRes5_4)

        self.RandRes5_5 = QTextEdit(self.RandomFunctionRes5)
        self.RandRes5_5.setObjectName(u"RandRes5_5")

        self.verticalLayout_226.addWidget(self.RandRes5_5)

        self.stackedWidget_2.addWidget(self.RandomFunctionRes5)

        self.horizontalLayout_43.addWidget(self.stackedWidget_2)


        self.verticalLayout_214.addWidget(self.frame_273)

        self.frame_274 = QFrame(self.frame_272)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setFrameShape(QFrame.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Raised)
        self.verticalLayout_215 = QVBoxLayout(self.frame_274)
        self.verticalLayout_215.setObjectName(u"verticalLayout_215")
        self.pushButton_5 = QPushButton(self.frame_274)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_215.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_274)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_215.addWidget(self.pushButton_4)


        self.verticalLayout_214.addWidget(self.frame_274)


        self.horizontalLayout_13.addWidget(self.frame_272)

        self.stackedWidget.addWidget(self.RandomCompetitors)
        self.SummaryPage = QWidget()
        self.SummaryPage.setObjectName(u"SummaryPage")
        self.SummaryPage.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(157, 157, 157);\n"
"	color: rgb(0, 0, 0,)\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.SummaryPage)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_58 = QFrame(self.SummaryPage)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_58)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(16777215, 75))
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_11 = QLabel(self.frame_59)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.label_11.setFont(font1)

        self.horizontalLayout_45.addWidget(self.label_11)

        self.comboBox = QComboBox(self.frame_59)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_45.addWidget(self.comboBox)


        self.verticalLayout_44.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)

        self.verticalLayout_44.addWidget(self.frame_60)


        self.horizontalLayout_44.addWidget(self.frame_58)

        self.stackedWidget.addWidget(self.SummaryPage)
        self.CompetitorInputPage = QWidget()
        self.CompetitorInputPage.setObjectName(u"CompetitorInputPage")
        self.CompetitorInputPage.setStyleSheet(u"QPushButton{	\n"
"\n"
"	font: 75 11pt \"Calibri\";\n"
"	color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(157, 157, 157);\n"
"	color: rgb(0, 0, 0,)\n"
"}")
        self.horizontalLayout_46 = QHBoxLayout(self.CompetitorInputPage)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.frame_62 = QFrame(self.CompetitorInputPage)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.frame_112 = QFrame(self.frame_62)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMaximumSize(QSize(300, 16777215))
        self.frame_112.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	color: rgb(185, 185, 185);\n"
"	font: 75 26pt \"Calibri\";\n"
"	font-weight: bold;\n"
"}")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_112)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.label_25 = QLabel(self.frame_112)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 40))
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(u"font: 75 16pt \"Calibri\";")

        self.verticalLayout_88.addWidget(self.label_25)

        self.frame_114 = QFrame(self.frame_112)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setMinimumSize(QSize(250, 300))
        self.frame_114.setMaximumSize(QSize(16777215, 16777215))
        self.frame_114.setFrameShape(QFrame.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_114)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.frame_116 = QFrame(self.frame_114)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.CategoriesToAdd = QLineEdit(self.frame_116)
        self.CategoriesToAdd.setObjectName(u"CategoriesToAdd")

        self.horizontalLayout_48.addWidget(self.CategoriesToAdd)

        self.CategoriesBrowseButton = QPushButton(self.frame_116)
        self.CategoriesBrowseButton.setObjectName(u"CategoriesBrowseButton")

        self.horizontalLayout_48.addWidget(self.CategoriesBrowseButton)


        self.verticalLayout_90.addWidget(self.frame_116)

        self.frame_117 = QFrame(self.frame_114)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_117)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.AddCategoriesButton_2 = QPushButton(self.frame_117)
        self.AddCategoriesButton_2.setObjectName(u"AddCategoriesButton_2")

        self.horizontalLayout_49.addWidget(self.AddCategoriesButton_2)


        self.verticalLayout_90.addWidget(self.frame_117)


        self.verticalLayout_88.addWidget(self.frame_114)

        self.frame_115 = QFrame(self.frame_112)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(250, 0))
        self.frame_115.setStyleSheet(u"")
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_115)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.label_26 = QLabel(self.frame_115)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(u"font: 75 16pt \"Calibri\";")

        self.verticalLayout_89.addWidget(self.label_26)

        self.AddedCategories = QScrollArea(self.frame_115)
        self.AddedCategories.setObjectName(u"AddedCategories")
        self.AddedCategories.setMinimumSize(QSize(250, 0))
        self.AddedCategories.setMaximumSize(QSize(245, 16777215))
        self.AddedCategories.setToolTipDuration(-1)
        self.AddedCategories.setStyleSheet(u"QScrollArea{\n"
"background: transparent;\n"
"}")
        self.AddedCategories.setFrameShape(QFrame.StyledPanel)
        self.AddedCategories.setFrameShadow(QFrame.Raised)
        self.AddedCategories.setLineWidth(0)
        self.AddedCategories.setMidLineWidth(0)
        self.AddedCategories.setWidgetResizable(True)
        self.AddedCategoriesContents = QWidget()
        self.AddedCategoriesContents.setObjectName(u"AddedCategoriesContents")
        self.AddedCategoriesContents.setEnabled(True)
        self.AddedCategoriesContents.setGeometry(QRect(0, 0, 248, 305))
        self.AddedCategoriesContents.setMaximumSize(QSize(16777215, 16777215))
        self.AddedCategoriesContents.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(100, 100, 100);\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"	font: 255 8pt \"Calibri\";\n"
"	color: white;\n"
"}")
        self.verticalLayout_93 = QVBoxLayout(self.AddedCategoriesContents)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.AddedCategories.setWidget(self.AddedCategoriesContents)

        self.verticalLayout_89.addWidget(self.AddedCategories)


        self.verticalLayout_88.addWidget(self.frame_115)


        self.horizontalLayout_47.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_62)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMinimumSize(QSize(500, 0))
        self.frame_113.setMaximumSize(QSize(16777215, 16777215))
        self.frame_113.setStyleSheet(u"")
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_113)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_118 = QFrame(self.frame_113)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMaximumSize(QSize(16777215, 50))
        self.frame_118.setStyleSheet(u"QComboBox {\n"
"	background-color: rgb(30, 30, 30);\n"
"	color: rgb(150, 150, 150);\n"
"	border-style: solid;\n"
"	border-width: 2;\n"
"	border-color: rgb(150, 150, 150);\n"
"}")
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.GenderComboBox = QComboBox(self.frame_118)
        self.GenderComboBox.setObjectName(u"GenderComboBox")

        self.horizontalLayout_50.addWidget(self.GenderComboBox)

        self.AgeComboBox = QComboBox(self.frame_118)
        self.AgeComboBox.setObjectName(u"AgeComboBox")

        self.horizontalLayout_50.addWidget(self.AgeComboBox)

        self.CategoryComboBox = QComboBox(self.frame_118)
        self.CategoryComboBox.setObjectName(u"CategoryComboBox")

        self.horizontalLayout_50.addWidget(self.CategoryComboBox)

        self.ClubComboBox = QComboBox(self.frame_118)
        self.ClubComboBox.setObjectName(u"ClubComboBox")

        self.horizontalLayout_50.addWidget(self.ClubComboBox)

        self.FilterCattegoryButton = QPushButton(self.frame_118)
        self.FilterCattegoryButton.setObjectName(u"FilterCattegoryButton")

        self.horizontalLayout_50.addWidget(self.FilterCattegoryButton)


        self.verticalLayout_91.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.frame_113)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_119)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.frame_131 = QFrame(self.frame_119)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.StyledPanel)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_131)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.CompetitorsTable = QTableWidget(self.frame_131)
        if (self.CompetitorsTable.columnCount() < 4):
            self.CompetitorsTable.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.CompetitorsTable.setObjectName(u"CompetitorsTable")
        self.CompetitorsTable.setMaximumSize(QSize(16777215, 250))
        self.CompetitorsTable.setStyleSheet(u"")

        self.horizontalLayout_56.addWidget(self.CompetitorsTable)


        self.verticalLayout_92.addWidget(self.frame_131)

        self.frame_120 = QFrame(self.frame_119)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setFrameShape(QFrame.StyledPanel)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_120)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.frame_122 = QFrame(self.frame_120)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.frame_121 = QFrame(self.frame_122)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setFrameShape(QFrame.StyledPanel)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_121)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.frame_123 = QFrame(self.frame_121)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMaximumSize(QSize(16777215, 140))
        self.frame_123.setStyleSheet(u"font: 75 10pt \"Calibri\";")
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_123)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.ComprtitorName = QLabel(self.frame_123)
        self.ComprtitorName.setObjectName(u"ComprtitorName")
        self.ComprtitorName.setStyleSheet(u"background:transparent;")

        self.verticalLayout_96.addWidget(self.ComprtitorName)

        self.CompetitorSurname = QLabel(self.frame_123)
        self.CompetitorSurname.setObjectName(u"CompetitorSurname")
        self.CompetitorSurname.setStyleSheet(u"background:transparent;")

        self.verticalLayout_96.addWidget(self.CompetitorSurname)

        self.CompetitorClub = QLabel(self.frame_123)
        self.CompetitorClub.setObjectName(u"CompetitorClub")
        self.CompetitorClub.setStyleSheet(u"background:transparent;")

        self.verticalLayout_96.addWidget(self.CompetitorClub)

        self.CompetitorBornDate = QLabel(self.frame_123)
        self.CompetitorBornDate.setObjectName(u"CompetitorBornDate")
        self.CompetitorBornDate.setStyleSheet(u"background:transparent;")

        self.verticalLayout_96.addWidget(self.CompetitorBornDate)

        self.CompetitorLicenceNo = QLabel(self.frame_123)
        self.CompetitorLicenceNo.setObjectName(u"CompetitorLicenceNo")
        self.CompetitorLicenceNo.setStyleSheet(u"background:transparent;")

        self.verticalLayout_96.addWidget(self.CompetitorLicenceNo)


        self.verticalLayout_94.addWidget(self.frame_123)

        self.frame_124 = QFrame(self.frame_121)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMaximumSize(QSize(16777215, 140))
        self.frame_124.setFrameShape(QFrame.StyledPanel)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_124)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.frame_128 = QFrame(self.frame_124)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setFrameShape(QFrame.StyledPanel)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_27 = QLabel(self.frame_128)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 76 23pt \"Calibri\";")

        self.horizontalLayout_53.addWidget(self.label_27)

        self.CompetitorWeightInput = QTextEdit(self.frame_128)
        self.CompetitorWeightInput.setObjectName(u"CompetitorWeightInput")

        self.horizontalLayout_53.addWidget(self.CompetitorWeightInput)


        self.verticalLayout_95.addWidget(self.frame_128)

        self.frame_129 = QFrame(self.frame_124)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.StyledPanel)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_54 = QHBoxLayout(self.frame_129)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")

        self.verticalLayout_95.addWidget(self.frame_129)


        self.verticalLayout_94.addWidget(self.frame_124)


        self.horizontalLayout_52.addWidget(self.frame_121)

        self.frame_125 = QFrame(self.frame_122)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMinimumSize(QSize(100, 0))
        self.frame_125.setFrameShape(QFrame.StyledPanel)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.frame_125)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.frame_126 = QFrame(self.frame_125)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.StyledPanel)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_126)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.label_32 = QLabel(self.frame_126)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_98.addWidget(self.label_32)


        self.verticalLayout_97.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.frame_125)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setFrameShape(QFrame.StyledPanel)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.CompetitorCategories = QTableWidget(self.frame_127)
        if (self.CompetitorCategories.columnCount() < 3):
            self.CompetitorCategories.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.CompetitorCategories.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.CompetitorCategories.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.CompetitorCategories.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.CompetitorCategories.setObjectName(u"CompetitorCategories")
        self.CompetitorCategories.setFrameShape(QFrame.StyledPanel)
        self.CompetitorCategories.setFrameShadow(QFrame.Sunken)
        self.CompetitorCategories.setAutoScrollMargin(16)
        self.CompetitorCategories.setGridStyle(Qt.SolidLine)
        self.CompetitorCategories.horizontalHeader().setDefaultSectionSize(125)

        self.horizontalLayout_55.addWidget(self.CompetitorCategories)

        self.frame_130 = QFrame(self.frame_127)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setFrameShape(QFrame.StyledPanel)
        self.frame_130.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_130)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.DeleteCompetitorCategoryButton = QPushButton(self.frame_130)
        self.DeleteCompetitorCategoryButton.setObjectName(u"DeleteCompetitorCategoryButton")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DeleteCompetitorCategoryButton.setIcon(icon5)

        self.verticalLayout_99.addWidget(self.DeleteCompetitorCategoryButton)

        self.AddCompetitorCategoryButton = QPushButton(self.frame_130)
        self.AddCompetitorCategoryButton.setObjectName(u"AddCompetitorCategoryButton")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/icons/cil-medical-cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.AddCompetitorCategoryButton.setIcon(icon6)

        self.verticalLayout_99.addWidget(self.AddCompetitorCategoryButton)


        self.horizontalLayout_55.addWidget(self.frame_130)


        self.verticalLayout_97.addWidget(self.frame_127)


        self.horizontalLayout_52.addWidget(self.frame_125)


        self.horizontalLayout_51.addWidget(self.frame_122)


        self.verticalLayout_92.addWidget(self.frame_120)

        self.SaveCompetitorButton = QPushButton(self.frame_119)
        self.SaveCompetitorButton.setObjectName(u"SaveCompetitorButton")
        self.SaveCompetitorButton.setMaximumSize(QSize(16777215, 40))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.SaveCompetitorButton.setIcon(icon7)

        self.verticalLayout_92.addWidget(self.SaveCompetitorButton)

        self.SaveCategoriesToTxt = QPushButton(self.frame_119)
        self.SaveCategoriesToTxt.setObjectName(u"SaveCategoriesToTxt")

        self.verticalLayout_92.addWidget(self.SaveCategoriesToTxt)

        self.SaveCategoriesToPdf = QPushButton(self.frame_119)
        self.SaveCategoriesToPdf.setObjectName(u"SaveCategoriesToPdf")

        self.verticalLayout_92.addWidget(self.SaveCategoriesToPdf)


        self.verticalLayout_91.addWidget(self.frame_119)


        self.horizontalLayout_47.addWidget(self.frame_113)


        self.horizontalLayout_46.addWidget(self.frame_62)

        self.stackedWidget.addWidget(self.CompetitorInputPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.SettingsPage.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(83, 83, 83);\n"
" 	border-radius: 2px;\n"
"	color: rgb(157, 157, 157);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(157, 157, 157);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QSlider {\n"
"	background: transparent;\n"
"}")
        self.verticalLayout_101 = QVBoxLayout(self.SettingsPage)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.frame_133 = QFrame(self.SettingsPage)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.StyledPanel)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_133)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.frame_135 = QFrame(self.frame_133)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setFrameShape(QFrame.StyledPanel)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_135)
        self.verticalLayout_102.setSpacing(0)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_135)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 96))

        self.verticalLayout_102.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_135)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 96))

        self.verticalLayout_102.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_135)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 96))

        self.verticalLayout_102.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame_135)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 96))

        self.verticalLayout_102.addWidget(self.label_31)

        self.label_33 = QLabel(self.frame_135)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 96))

        self.verticalLayout_102.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_135)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(0, 96))

        self.verticalLayout_102.addWidget(self.label_34)

        self.label_35 = QLabel(self.frame_135)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(0, 96))

        self.verticalLayout_102.addWidget(self.label_35)


        self.horizontalLayout_58.addWidget(self.frame_135)

        self.frame_136 = QFrame(self.frame_133)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setFrameShape(QFrame.StyledPanel)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_136)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.frame_151 = QFrame(self.frame_136)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setMaximumSize(QSize(650, 100))
        self.frame_151.setFrameShape(QFrame.StyledPanel)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_151)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.frame_172 = QFrame(self.frame_151)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setMaximumSize(QSize(300, 100))
        self.frame_172.setFrameShape(QFrame.StyledPanel)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_172)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_1 = QTextEdit(self.frame_172)
        self.age_textEdit_1.setObjectName(u"age_textEdit_1")
        self.age_textEdit_1.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_133.addWidget(self.age_textEdit_1)

        self.age_slider_1 = QSlider(self.frame_172)
        self.age_slider_1.setObjectName(u"age_slider_1")
        self.age_slider_1.setOrientation(Qt.Horizontal)

        self.verticalLayout_133.addWidget(self.age_slider_1)


        self.horizontalLayout_67.addWidget(self.frame_172)

        self.frame_173 = QFrame(self.frame_151)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setMaximumSize(QSize(300, 100))
        self.frame_173.setFrameShape(QFrame.StyledPanel)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.verticalLayout_134 = QVBoxLayout(self.frame_173)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_2 = QTextEdit(self.frame_173)
        self.age_textEdit_2.setObjectName(u"age_textEdit_2")
        self.age_textEdit_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_134.addWidget(self.age_textEdit_2)

        self.age_slider_2 = QSlider(self.frame_173)
        self.age_slider_2.setObjectName(u"age_slider_2")
        self.age_slider_2.setOrientation(Qt.Horizontal)

        self.verticalLayout_134.addWidget(self.age_slider_2)


        self.horizontalLayout_67.addWidget(self.frame_173)


        self.verticalLayout_103.addWidget(self.frame_151)

        self.frame_145 = QFrame(self.frame_136)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setMaximumSize(QSize(650, 100))
        self.frame_145.setFrameShape(QFrame.StyledPanel)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.frame_161 = QFrame(self.frame_145)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setMaximumSize(QSize(300, 100))
        self.frame_161.setFrameShape(QFrame.StyledPanel)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.frame_161)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_3 = QTextEdit(self.frame_161)
        self.age_textEdit_3.setObjectName(u"age_textEdit_3")
        self.age_textEdit_3.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_122.addWidget(self.age_textEdit_3)

        self.age_slider_3 = QSlider(self.frame_161)
        self.age_slider_3.setObjectName(u"age_slider_3")
        self.age_slider_3.setOrientation(Qt.Horizontal)

        self.verticalLayout_122.addWidget(self.age_slider_3)


        self.horizontalLayout_61.addWidget(self.frame_161)

        self.frame_160 = QFrame(self.frame_145)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setMaximumSize(QSize(300, 100))
        self.frame_160.setFrameShape(QFrame.StyledPanel)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.verticalLayout_121 = QVBoxLayout(self.frame_160)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_4 = QTextEdit(self.frame_160)
        self.age_textEdit_4.setObjectName(u"age_textEdit_4")
        self.age_textEdit_4.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_121.addWidget(self.age_textEdit_4)

        self.age_slider_4 = QSlider(self.frame_160)
        self.age_slider_4.setObjectName(u"age_slider_4")
        self.age_slider_4.setOrientation(Qt.Horizontal)

        self.verticalLayout_121.addWidget(self.age_slider_4)


        self.horizontalLayout_61.addWidget(self.frame_160)


        self.verticalLayout_103.addWidget(self.frame_145)

        self.frame_150 = QFrame(self.frame_136)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMaximumSize(QSize(650, 100))
        self.frame_150.setFrameShape(QFrame.StyledPanel)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.frame_170 = QFrame(self.frame_150)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setMaximumSize(QSize(300, 100))
        self.frame_170.setFrameShape(QFrame.StyledPanel)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.verticalLayout_131 = QVBoxLayout(self.frame_170)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_5 = QTextEdit(self.frame_170)
        self.age_textEdit_5.setObjectName(u"age_textEdit_5")
        self.age_textEdit_5.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_131.addWidget(self.age_textEdit_5)

        self.age_slider_5 = QSlider(self.frame_170)
        self.age_slider_5.setObjectName(u"age_slider_5")
        self.age_slider_5.setOrientation(Qt.Horizontal)

        self.verticalLayout_131.addWidget(self.age_slider_5)


        self.horizontalLayout_66.addWidget(self.frame_170)

        self.frame_171 = QFrame(self.frame_150)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setMaximumSize(QSize(300, 100))
        self.frame_171.setFrameShape(QFrame.StyledPanel)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.frame_171)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_6 = QTextEdit(self.frame_171)
        self.age_textEdit_6.setObjectName(u"age_textEdit_6")
        self.age_textEdit_6.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_132.addWidget(self.age_textEdit_6)

        self.age_slider_6 = QSlider(self.frame_171)
        self.age_slider_6.setObjectName(u"age_slider_6")
        self.age_slider_6.setOrientation(Qt.Horizontal)

        self.verticalLayout_132.addWidget(self.age_slider_6)


        self.horizontalLayout_66.addWidget(self.frame_171)


        self.verticalLayout_103.addWidget(self.frame_150)

        self.frame_149 = QFrame(self.frame_136)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setMaximumSize(QSize(650, 100))
        self.frame_149.setFrameShape(QFrame.StyledPanel)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.frame_168 = QFrame(self.frame_149)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setMaximumSize(QSize(300, 100))
        self.frame_168.setFrameShape(QFrame.StyledPanel)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.frame_168)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_7 = QTextEdit(self.frame_168)
        self.age_textEdit_7.setObjectName(u"age_textEdit_7")
        self.age_textEdit_7.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_129.addWidget(self.age_textEdit_7)

        self.age_slider_7 = QSlider(self.frame_168)
        self.age_slider_7.setObjectName(u"age_slider_7")
        self.age_slider_7.setOrientation(Qt.Horizontal)

        self.verticalLayout_129.addWidget(self.age_slider_7)


        self.horizontalLayout_65.addWidget(self.frame_168)

        self.frame_169 = QFrame(self.frame_149)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setMaximumSize(QSize(300, 100))
        self.frame_169.setFrameShape(QFrame.StyledPanel)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.frame_169)
        self.verticalLayout_130.setSpacing(0)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.verticalLayout_130.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_8 = QTextEdit(self.frame_169)
        self.age_textEdit_8.setObjectName(u"age_textEdit_8")
        self.age_textEdit_8.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_130.addWidget(self.age_textEdit_8)

        self.age_slider_8 = QSlider(self.frame_169)
        self.age_slider_8.setObjectName(u"age_slider_8")
        self.age_slider_8.setOrientation(Qt.Horizontal)

        self.verticalLayout_130.addWidget(self.age_slider_8)


        self.horizontalLayout_65.addWidget(self.frame_169)


        self.verticalLayout_103.addWidget(self.frame_149)

        self.frame_148 = QFrame(self.frame_136)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setMaximumSize(QSize(650, 100))
        self.frame_148.setFrameShape(QFrame.StyledPanel)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_148)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.frame_166 = QFrame(self.frame_148)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMaximumSize(QSize(300, 100))
        self.frame_166.setFrameShape(QFrame.StyledPanel)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.frame_166)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_9 = QTextEdit(self.frame_166)
        self.age_textEdit_9.setObjectName(u"age_textEdit_9")
        self.age_textEdit_9.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_127.addWidget(self.age_textEdit_9)

        self.age_slider_9 = QSlider(self.frame_166)
        self.age_slider_9.setObjectName(u"age_slider_9")
        self.age_slider_9.setOrientation(Qt.Horizontal)

        self.verticalLayout_127.addWidget(self.age_slider_9)


        self.horizontalLayout_64.addWidget(self.frame_166)

        self.frame_167 = QFrame(self.frame_148)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setMaximumSize(QSize(300, 100))
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)
        self.verticalLayout_128 = QVBoxLayout(self.frame_167)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_10 = QTextEdit(self.frame_167)
        self.age_textEdit_10.setObjectName(u"age_textEdit_10")
        self.age_textEdit_10.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_128.addWidget(self.age_textEdit_10)

        self.age_slider_10 = QSlider(self.frame_167)
        self.age_slider_10.setObjectName(u"age_slider_10")
        self.age_slider_10.setOrientation(Qt.Horizontal)

        self.verticalLayout_128.addWidget(self.age_slider_10)


        self.horizontalLayout_64.addWidget(self.frame_167)


        self.verticalLayout_103.addWidget(self.frame_148)

        self.frame_147 = QFrame(self.frame_136)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMaximumSize(QSize(650, 100))
        self.frame_147.setFrameShape(QFrame.StyledPanel)
        self.frame_147.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_147)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.frame_164 = QFrame(self.frame_147)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setMaximumSize(QSize(300, 100))
        self.frame_164.setFrameShape(QFrame.StyledPanel)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.frame_164)
        self.verticalLayout_125.setSpacing(0)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.verticalLayout_125.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_11 = QTextEdit(self.frame_164)
        self.age_textEdit_11.setObjectName(u"age_textEdit_11")
        self.age_textEdit_11.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_125.addWidget(self.age_textEdit_11)

        self.age_slider_11 = QSlider(self.frame_164)
        self.age_slider_11.setObjectName(u"age_slider_11")
        self.age_slider_11.setOrientation(Qt.Horizontal)

        self.verticalLayout_125.addWidget(self.age_slider_11)


        self.horizontalLayout_63.addWidget(self.frame_164)

        self.frame_165 = QFrame(self.frame_147)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setMaximumSize(QSize(300, 100))
        self.frame_165.setFrameShape(QFrame.StyledPanel)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.frame_165)
        self.verticalLayout_126.setSpacing(0)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.verticalLayout_126.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_12 = QTextEdit(self.frame_165)
        self.age_textEdit_12.setObjectName(u"age_textEdit_12")
        self.age_textEdit_12.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_126.addWidget(self.age_textEdit_12)

        self.age_slider_12 = QSlider(self.frame_165)
        self.age_slider_12.setObjectName(u"age_slider_12")
        self.age_slider_12.setOrientation(Qt.Horizontal)

        self.verticalLayout_126.addWidget(self.age_slider_12)


        self.horizontalLayout_63.addWidget(self.frame_165)


        self.verticalLayout_103.addWidget(self.frame_147)

        self.frame_146 = QFrame(self.frame_136)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setMaximumSize(QSize(650, 100))
        self.frame_146.setFrameShape(QFrame.StyledPanel)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_162 = QFrame(self.frame_146)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setMaximumSize(QSize(300, 100))
        self.frame_162.setFrameShape(QFrame.StyledPanel)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.frame_162)
        self.verticalLayout_123.setSpacing(0)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.verticalLayout_123.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_13 = QTextEdit(self.frame_162)
        self.age_textEdit_13.setObjectName(u"age_textEdit_13")
        self.age_textEdit_13.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_123.addWidget(self.age_textEdit_13)

        self.age_slider_13 = QSlider(self.frame_162)
        self.age_slider_13.setObjectName(u"age_slider_13")
        self.age_slider_13.setOrientation(Qt.Horizontal)

        self.verticalLayout_123.addWidget(self.age_slider_13)


        self.horizontalLayout_62.addWidget(self.frame_162)

        self.frame_163 = QFrame(self.frame_146)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setMaximumSize(QSize(300, 100))
        self.frame_163.setFrameShape(QFrame.StyledPanel)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.frame_163)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(0, 0, 0, 0)
        self.age_textEdit_14 = QTextEdit(self.frame_163)
        self.age_textEdit_14.setObjectName(u"age_textEdit_14")
        self.age_textEdit_14.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_124.addWidget(self.age_textEdit_14)

        self.age_slider_14 = QSlider(self.frame_163)
        self.age_slider_14.setObjectName(u"age_slider_14")
        self.age_slider_14.setOrientation(Qt.Horizontal)

        self.verticalLayout_124.addWidget(self.age_slider_14)


        self.horizontalLayout_62.addWidget(self.frame_163)


        self.verticalLayout_103.addWidget(self.frame_146)


        self.horizontalLayout_58.addWidget(self.frame_136)

        self.frame_137 = QFrame(self.frame_133)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setMinimumSize(QSize(150, 0))
        self.frame_137.setFrameShape(QFrame.StyledPanel)
        self.frame_137.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_58.addWidget(self.frame_137)


        self.verticalLayout_101.addWidget(self.frame_133)

        self.frame_134 = QFrame(self.SettingsPage)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setMaximumSize(QSize(16777215, 50))
        self.frame_134.setFrameShape(QFrame.StyledPanel)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSpacer = QSpacerItem(947, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer)

        self.saveSettingsButton = QPushButton(self.frame_134)
        self.saveSettingsButton.setObjectName(u"saveSettingsButton")
        self.saveSettingsButton.setMinimumSize(QSize(120, 0))
        self.saveSettingsButton.setIcon(icon7)

        self.horizontalLayout_57.addWidget(self.saveSettingsButton)


        self.verticalLayout_101.addWidget(self.frame_134)

        self.stackedWidget.addWidget(self.SettingsPage)
        self.AcountPage = QWidget()
        self.AcountPage.setObjectName(u"AcountPage")
        self.AcountPage.setStyleSheet(u"QWidget {\n"
"	background: transparent; \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(157, 157, 157);\n"
"	color: rgb(0, 0, 0,)\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.AcountPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Content_wraper = QFrame(self.AcountPage)
        self.Content_wraper.setObjectName(u"Content_wraper")
        self.Content_wraper.setStyleSheet(u"QPushButton{	\n"
"\n"
"	font: 75 11pt \"Calibri\";\n"
"	color: rgb(186, 186, 186);\n"
"}\n"
"")
        self.Content_wraper.setFrameShape(QFrame.StyledPanel)
        self.Content_wraper.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.Content_wraper)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.AllMatchesWraper = QStackedWidget(self.Content_wraper)
        self.AllMatchesWraper.setObjectName(u"AllMatchesWraper")
        self.AllMatchesWraper.setStyleSheet(u"QTextEdit {\n"
"    background-color: rgb(217, 217, 217);\n"
"	border-color:rgb(0, 0, 0);\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"}\n"
"\n"
"\n"
" background: transparent;\n"
"\n"
"")
        self.MatchUnder16 = QWidget()
        self.MatchUnder16.setObjectName(u"MatchUnder16")
        self.verticalLayout_118 = QVBoxLayout(self.MatchUnder16)
        self.verticalLayout_118.setObjectName(u"verticalLayout_118")
        self.Top_menu_wraper = QFrame(self.MatchUnder16)
        self.Top_menu_wraper.setObjectName(u"Top_menu_wraper")
        self.Top_menu_wraper.setMaximumSize(QSize(16777215, 100))
        self.Top_menu_wraper.setFrameShape(QFrame.StyledPanel)
        self.Top_menu_wraper.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.Top_menu_wraper)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.Top_menu = QFrame(self.Top_menu_wraper)
        self.Top_menu.setObjectName(u"Top_menu")
        self.Top_menu.setMaximumSize(QSize(16777215, 0))
        self.Top_menu.setFrameShape(QFrame.StyledPanel)
        self.Top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.Top_menu)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Eliminations_button = QPushButton(self.Top_menu)
        self.Eliminations_button.setObjectName(u"Eliminations_button")

        self.horizontalLayout_14.addWidget(self.Eliminations_button)

        self.HalfFinal_button = QPushButton(self.Top_menu)
        self.HalfFinal_button.setObjectName(u"HalfFinal_button")

        self.horizontalLayout_14.addWidget(self.HalfFinal_button)

        self.Repechage_button = QPushButton(self.Top_menu)
        self.Repechage_button.setObjectName(u"Repechage_button")

        self.horizontalLayout_14.addWidget(self.Repechage_button)

        self.Final_button = QPushButton(self.Top_menu)
        self.Final_button.setObjectName(u"Final_button")

        self.horizontalLayout_14.addWidget(self.Final_button)


        self.verticalLayout_21.addWidget(self.Top_menu)

        self.Top_menu_slide_button = QPushButton(self.Top_menu_wraper)
        self.Top_menu_slide_button.setObjectName(u"Top_menu_slide_button")
        self.Top_menu_slide_button.setMinimumSize(QSize(40, 40))
        self.Top_menu_slide_button.setMaximumSize(QSize(40, 40))
        self.Top_menu_slide_button.setStyleSheet(u"background:transparent;")
        icon8 = QIcon()
        icon8.addFile(u":/Icons/icons/cil-arrow-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Top_menu_slide_button.setIcon(icon8)

        self.verticalLayout_21.addWidget(self.Top_menu_slide_button, 0, Qt.AlignHCenter)


        self.verticalLayout_118.addWidget(self.Top_menu_wraper)

        self.match_16 = QStackedWidget(self.MatchUnder16)
        self.match_16.setObjectName(u"match_16")
        self.match_16.setStyleSheet(u"")
        self.Eliminations = QWidget()
        self.Eliminations.setObjectName(u"Eliminations")
        self.verticalLayout_19 = QVBoxLayout(self.Eliminations)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_4 = QFrame(self.Eliminations)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(False)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 250))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(45, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.el_16_node_16 = QTextEdit(self.frame_8)
        self.el_16_node_16.setObjectName(u"el_16_node_16")
        self.el_16_node_16.setEnabled(False)
        self.el_16_node_16.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_16.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.el_16_node_16)

        self.el_16_node_17 = QTextEdit(self.frame_8)
        self.el_16_node_17.setObjectName(u"el_16_node_17")
        self.el_16_node_17.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_17.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_17.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.el_16_node_17)

        self.el_16_node_18 = QTextEdit(self.frame_8)
        self.el_16_node_18.setObjectName(u"el_16_node_18")
        self.el_16_node_18.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_18.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_18.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.el_16_node_18)

        self.el_16_node_19 = QTextEdit(self.frame_8)
        self.el_16_node_19.setObjectName(u"el_16_node_19")
        self.el_16_node_19.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_19.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_19.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_4.addWidget(self.el_16_node_19)


        self.horizontalLayout_8.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(45, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.el_16_node_8 = QTextEdit(self.frame_9)
        self.el_16_node_8.setObjectName(u"el_16_node_8")
        self.el_16_node_8.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_5.addWidget(self.el_16_node_8)

        self.el_16_node_9 = QTextEdit(self.frame_9)
        self.el_16_node_9.setObjectName(u"el_16_node_9")
        self.el_16_node_9.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_5.addWidget(self.el_16_node_9)


        self.horizontalLayout_8.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(45, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.el_16_node_4 = QTextEdit(self.frame_10)
        self.el_16_node_4.setObjectName(u"el_16_node_4")
        self.el_16_node_4.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_6.addWidget(self.el_16_node_4)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 250))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_11 = QFrame(self.frame_7)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(45, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_11)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.el_16_node_20 = QTextEdit(self.frame_11)
        self.el_16_node_20.setObjectName(u"el_16_node_20")
        self.el_16_node_20.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_20.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_20.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.el_16_node_20)

        self.el_16_node_21 = QTextEdit(self.frame_11)
        self.el_16_node_21.setObjectName(u"el_16_node_21")
        self.el_16_node_21.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_21.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_21.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.el_16_node_21)

        self.el_16_node_22 = QTextEdit(self.frame_11)
        self.el_16_node_22.setObjectName(u"el_16_node_22")
        self.el_16_node_22.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_22.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_22.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.el_16_node_22)

        self.el_16_node_23 = QTextEdit(self.frame_11)
        self.el_16_node_23.setObjectName(u"el_16_node_23")
        self.el_16_node_23.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_23.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_23.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.el_16_node_23)


        self.horizontalLayout_9.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(45, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.el_16_node_10 = QTextEdit(self.frame_12)
        self.el_16_node_10.setObjectName(u"el_16_node_10")
        self.el_16_node_10.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_8.addWidget(self.el_16_node_10)

        self.el_16_node_11 = QTextEdit(self.frame_12)
        self.el_16_node_11.setObjectName(u"el_16_node_11")
        self.el_16_node_11.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_8.addWidget(self.el_16_node_11)


        self.horizontalLayout_9.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_7)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(45, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_13)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.el_16_node_5 = QTextEdit(self.frame_13)
        self.el_16_node_5.setObjectName(u"el_16_node_5")
        self.el_16_node_5.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_9.addWidget(self.el_16_node_5)


        self.horizontalLayout_9.addWidget(self.frame_13)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_14 = QFrame(self.frame_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(250, 0))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 250))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(45, 0))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.el_16_node_6 = QTextEdit(self.frame_17)
        self.el_16_node_6.setObjectName(u"el_16_node_6")
        self.el_16_node_6.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_12.addWidget(self.el_16_node_6)


        self.horizontalLayout_10.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(45, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.el_16_node_12 = QTextEdit(self.frame_16)
        self.el_16_node_12.setObjectName(u"el_16_node_12")
        self.el_16_node_12.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_11.addWidget(self.el_16_node_12)

        self.el_16_node_13 = QTextEdit(self.frame_16)
        self.el_16_node_13.setObjectName(u"el_16_node_13")
        self.el_16_node_13.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_11.addWidget(self.el_16_node_13)


        self.horizontalLayout_10.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(45, 0))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_18)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.el_16_node_24 = QTextEdit(self.frame_18)
        self.el_16_node_24.setObjectName(u"el_16_node_24")
        self.el_16_node_24.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_24.setStyleSheet(u"")
        self.el_16_node_24.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_24.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_24.setUndoRedoEnabled(False)

        self.verticalLayout_10.addWidget(self.el_16_node_24)

        self.el_16_node_25 = QTextEdit(self.frame_18)
        self.el_16_node_25.setObjectName(u"el_16_node_25")
        self.el_16_node_25.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_25.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_25.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_10.addWidget(self.el_16_node_25)

        self.el_16_node_26 = QTextEdit(self.frame_18)
        self.el_16_node_26.setObjectName(u"el_16_node_26")
        self.el_16_node_26.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_26.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_26.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_10.addWidget(self.el_16_node_26)

        self.el_16_node_27 = QTextEdit(self.frame_18)
        self.el_16_node_27.setObjectName(u"el_16_node_27")
        self.el_16_node_27.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_27.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_27.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_10.addWidget(self.el_16_node_27)


        self.horizontalLayout_10.addWidget(self.frame_18)


        self.verticalLayout_16.addWidget(self.frame_15)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 250))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(45, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_21)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.el_16_node_7 = QTextEdit(self.frame_21)
        self.el_16_node_7.setObjectName(u"el_16_node_7")
        self.el_16_node_7.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_15.addWidget(self.el_16_node_7)


        self.horizontalLayout_11.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(45, 0))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_20)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.el_16_node_14 = QTextEdit(self.frame_20)
        self.el_16_node_14.setObjectName(u"el_16_node_14")
        self.el_16_node_14.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_14.addWidget(self.el_16_node_14)

        self.el_16_node_15 = QTextEdit(self.frame_20)
        self.el_16_node_15.setObjectName(u"el_16_node_15")
        self.el_16_node_15.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_14.addWidget(self.el_16_node_15)


        self.horizontalLayout_11.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(45, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_22)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.el_16_node_28 = QTextEdit(self.frame_22)
        self.el_16_node_28.setObjectName(u"el_16_node_28")
        self.el_16_node_28.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_28.setStyleSheet(u"")
        self.el_16_node_28.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_28.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_28)

        self.el_16_node_29 = QTextEdit(self.frame_22)
        self.el_16_node_29.setObjectName(u"el_16_node_29")
        self.el_16_node_29.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_29.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_29.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_29)

        self.el_16_node_30 = QTextEdit(self.frame_22)
        self.el_16_node_30.setObjectName(u"el_16_node_30")
        self.el_16_node_30.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_30.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_30.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_30)

        self.el_16_node_31 = QTextEdit(self.frame_22)
        self.el_16_node_31.setObjectName(u"el_16_node_31")
        self.el_16_node_31.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_31.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_31.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_31)


        self.horizontalLayout_11.addWidget(self.frame_22)


        self.verticalLayout_16.addWidget(self.frame_19)


        self.horizontalLayout_7.addWidget(self.frame_14)


        self.verticalLayout_19.addWidget(self.frame_4)

        self.match_16.addWidget(self.Eliminations)
        self.Repechage = QWidget()
        self.Repechage.setObjectName(u"Repechage")
        self.horizontalLayout_22 = QHBoxLayout(self.Repechage)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_33 = QFrame(self.Repechage)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_33)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_36)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.rep_16_node_8 = QTextEdit(self.frame_36)
        self.rep_16_node_8.setObjectName(u"rep_16_node_8")
        self.rep_16_node_8.setMaximumSize(QSize(270, 50))
        self.rep_16_node_8.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_8.setUndoRedoEnabled(False)

        self.verticalLayout_26.addWidget(self.rep_16_node_8)

        self.rep_16_node_9 = QTextEdit(self.frame_36)
        self.rep_16_node_9.setObjectName(u"rep_16_node_9")
        self.rep_16_node_9.setMaximumSize(QSize(270, 50))
        self.rep_16_node_9.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_9.setUndoRedoEnabled(False)

        self.verticalLayout_26.addWidget(self.rep_16_node_9)

        self.rep_16_node_10 = QTextEdit(self.frame_36)
        self.rep_16_node_10.setObjectName(u"rep_16_node_10")
        self.rep_16_node_10.setMaximumSize(QSize(270, 50))
        self.rep_16_node_10.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_10.setUndoRedoEnabled(False)

        self.verticalLayout_26.addWidget(self.rep_16_node_10)

        self.rep_16_node_11 = QTextEdit(self.frame_36)
        self.rep_16_node_11.setObjectName(u"rep_16_node_11")
        self.rep_16_node_11.setMaximumSize(QSize(270, 50))
        self.rep_16_node_11.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_11.setUndoRedoEnabled(False)

        self.verticalLayout_26.addWidget(self.rep_16_node_11)


        self.horizontalLayout_23.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_34)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_37)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.rep_16_node_4 = QTextEdit(self.frame_37)
        self.rep_16_node_4.setObjectName(u"rep_16_node_4")
        self.rep_16_node_4.setMaximumSize(QSize(270, 50))
        self.rep_16_node_4.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_4.setUndoRedoEnabled(False)

        self.verticalLayout_27.addWidget(self.rep_16_node_4)

        self.rep_16_node_5 = QTextEdit(self.frame_37)
        self.rep_16_node_5.setObjectName(u"rep_16_node_5")
        self.rep_16_node_5.setMaximumSize(QSize(270, 50))
        self.rep_16_node_5.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_5.setUndoRedoEnabled(False)

        self.verticalLayout_27.addWidget(self.rep_16_node_5)


        self.horizontalLayout_23.addWidget(self.frame_37)

        self.frame_38 = QFrame(self.frame_34)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_38)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.rep_16_node_2 = QTextEdit(self.frame_38)
        self.rep_16_node_2.setObjectName(u"rep_16_node_2")
        self.rep_16_node_2.setMaximumSize(QSize(270, 50))
        self.rep_16_node_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_2.setUndoRedoEnabled(False)

        self.verticalLayout_28.addWidget(self.rep_16_node_2)


        self.horizontalLayout_23.addWidget(self.frame_38)


        self.verticalLayout_25.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_39 = QFrame(self.frame_35)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_39)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.rep_16_node_12 = QTextEdit(self.frame_39)
        self.rep_16_node_12.setObjectName(u"rep_16_node_12")
        self.rep_16_node_12.setMaximumSize(QSize(270, 50))
        self.rep_16_node_12.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_12.setUndoRedoEnabled(False)

        self.verticalLayout_29.addWidget(self.rep_16_node_12)

        self.rep_16_node_13 = QTextEdit(self.frame_39)
        self.rep_16_node_13.setObjectName(u"rep_16_node_13")
        self.rep_16_node_13.setMaximumSize(QSize(270, 50))
        self.rep_16_node_13.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_13.setUndoRedoEnabled(False)

        self.verticalLayout_29.addWidget(self.rep_16_node_13)

        self.rep_16_node_14 = QTextEdit(self.frame_39)
        self.rep_16_node_14.setObjectName(u"rep_16_node_14")
        self.rep_16_node_14.setMaximumSize(QSize(270, 50))
        self.rep_16_node_14.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_14.setUndoRedoEnabled(False)

        self.verticalLayout_29.addWidget(self.rep_16_node_14)

        self.rep_16_node_15 = QTextEdit(self.frame_39)
        self.rep_16_node_15.setObjectName(u"rep_16_node_15")
        self.rep_16_node_15.setMaximumSize(QSize(270, 50))
        self.rep_16_node_15.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_15.setUndoRedoEnabled(False)

        self.verticalLayout_29.addWidget(self.rep_16_node_15)


        self.horizontalLayout_24.addWidget(self.frame_39)

        self.frame_40 = QFrame(self.frame_35)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_40)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.rep_16_node_6 = QTextEdit(self.frame_40)
        self.rep_16_node_6.setObjectName(u"rep_16_node_6")
        self.rep_16_node_6.setMaximumSize(QSize(270, 50))
        self.rep_16_node_6.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_6.setUndoRedoEnabled(False)

        self.verticalLayout_30.addWidget(self.rep_16_node_6)

        self.rep_16_node_7 = QTextEdit(self.frame_40)
        self.rep_16_node_7.setObjectName(u"rep_16_node_7")
        self.rep_16_node_7.setMaximumSize(QSize(270, 50))
        self.rep_16_node_7.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_7.setUndoRedoEnabled(False)

        self.verticalLayout_30.addWidget(self.rep_16_node_7)


        self.horizontalLayout_24.addWidget(self.frame_40)

        self.frame_41 = QFrame(self.frame_35)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_41)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.rep_16_node_3 = QTextEdit(self.frame_41)
        self.rep_16_node_3.setObjectName(u"rep_16_node_3")
        self.rep_16_node_3.setMaximumSize(QSize(270, 50))
        self.rep_16_node_3.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_3.setUndoRedoEnabled(False)

        self.verticalLayout_31.addWidget(self.rep_16_node_3)


        self.horizontalLayout_24.addWidget(self.frame_41)


        self.verticalLayout_25.addWidget(self.frame_35)


        self.horizontalLayout_22.addWidget(self.frame_33)

        self.match_16.addWidget(self.Repechage)
        self.Finals = QWidget()
        self.Finals.setObjectName(u"Finals")
        self.horizontalLayout_25 = QHBoxLayout(self.Finals)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_42 = QFrame(self.Finals)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_42)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_43)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_46 = QFrame(self.frame_43)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_6 = QLabel(self.frame_46)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.verticalLayout_33.addWidget(self.frame_46)

        self.el_16_node_1 = QTextEdit(self.frame_43)
        self.el_16_node_1.setObjectName(u"el_16_node_1")
        self.el_16_node_1.setMaximumSize(QSize(270, 50))

        self.verticalLayout_33.addWidget(self.el_16_node_1, 0, Qt.AlignHCenter)

        self.frame_47 = QFrame(self.frame_43)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.el_16_node_2_cpy = QTextEdit(self.frame_47)
        self.el_16_node_2_cpy.setObjectName(u"el_16_node_2_cpy")
        self.el_16_node_2_cpy.setMaximumSize(QSize(270, 50))
        self.el_16_node_2_cpy.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.el_16_node_2_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_2_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_2_cpy.setUndoRedoEnabled(False)

        self.horizontalLayout_32.addWidget(self.el_16_node_2_cpy, 0, Qt.AlignHCenter)

        self.el_16_node_3_cpy = QTextEdit(self.frame_47)
        self.el_16_node_3_cpy.setObjectName(u"el_16_node_3_cpy")
        self.el_16_node_3_cpy.setMaximumSize(QSize(270, 50))
        self.el_16_node_3_cpy.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.el_16_node_3_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_3_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_3_cpy.setUndoRedoEnabled(False)

        self.horizontalLayout_32.addWidget(self.el_16_node_3_cpy)


        self.verticalLayout_33.addWidget(self.frame_47)


        self.verticalLayout_32.addWidget(self.frame_43, 0, Qt.AlignHCenter)

        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.frame_48 = QFrame(self.frame_44)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_48)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_53 = QFrame(self.frame_48)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_7 = QLabel(self.frame_53)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"font: 75 18pt \"Calibri\";")

        self.horizontalLayout_29.addWidget(self.label_7, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.frame_53)

        self.textEdit_4 = QTextEdit(self.frame_48)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(270, 50))

        self.verticalLayout_36.addWidget(self.textEdit_4, 0, Qt.AlignHCenter)

        self.frame_54 = QFrame(self.frame_48)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.rep_16_node_2_cpy = QTextEdit(self.frame_54)
        self.rep_16_node_2_cpy.setObjectName(u"rep_16_node_2_cpy")
        self.rep_16_node_2_cpy.setMaximumSize(QSize(270, 50))
        self.rep_16_node_2_cpy.setStyleSheet(u"")
        self.rep_16_node_2_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_2_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_2_cpy.setUndoRedoEnabled(False)

        self.horizontalLayout_35.addWidget(self.rep_16_node_2_cpy)

        self.firstBronzeFinalist_16_node = QTextEdit(self.frame_54)
        self.firstBronzeFinalist_16_node.setObjectName(u"firstBronzeFinalist_16_node")
        self.firstBronzeFinalist_16_node.setMaximumSize(QSize(270, 50))
        self.firstBronzeFinalist_16_node.setStyleSheet(u"")
        self.firstBronzeFinalist_16_node.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.firstBronzeFinalist_16_node.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.firstBronzeFinalist_16_node.setUndoRedoEnabled(False)

        self.horizontalLayout_35.addWidget(self.firstBronzeFinalist_16_node)


        self.verticalLayout_36.addWidget(self.frame_54)


        self.horizontalLayout_30.addWidget(self.frame_48)

        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_45)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.frame_50 = QFrame(self.frame_45)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_5 = QLabel(self.frame_50)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"font: 75 18pt \"Calibri\";")

        self.horizontalLayout_28.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.verticalLayout_35.addWidget(self.frame_50)

        self.textEdit_5 = QTextEdit(self.frame_45)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(270, 50))

        self.verticalLayout_35.addWidget(self.textEdit_5, 0, Qt.AlignHCenter)

        self.frame_51 = QFrame(self.frame_45)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.rep_16_node_3_cpy = QTextEdit(self.frame_51)
        self.rep_16_node_3_cpy.setObjectName(u"rep_16_node_3_cpy")
        self.rep_16_node_3_cpy.setMaximumSize(QSize(270, 50))
        self.rep_16_node_3_cpy.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_3_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_3_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_3_cpy.setUndoRedoEnabled(False)

        self.horizontalLayout_34.addWidget(self.rep_16_node_3_cpy)

        self.secondBronzeFinalist_16_node = QTextEdit(self.frame_51)
        self.secondBronzeFinalist_16_node.setObjectName(u"secondBronzeFinalist_16_node")
        self.secondBronzeFinalist_16_node.setMaximumSize(QSize(270, 50))
        self.secondBronzeFinalist_16_node.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.secondBronzeFinalist_16_node.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.secondBronzeFinalist_16_node.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.secondBronzeFinalist_16_node.setUndoRedoEnabled(False)

        self.horizontalLayout_34.addWidget(self.secondBronzeFinalist_16_node)


        self.verticalLayout_35.addWidget(self.frame_51)


        self.horizontalLayout_30.addWidget(self.frame_45)


        self.verticalLayout_32.addWidget(self.frame_44)


        self.horizontalLayout_25.addWidget(self.frame_42, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.match_16.addWidget(self.Finals)
        self.HalfFinals = QWidget()
        self.HalfFinals.setObjectName(u"HalfFinals")
        self.horizontalLayout_15 = QHBoxLayout(self.HalfFinals)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_24 = QFrame(self.HalfFinals)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_24)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_25)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label = QLabel(self.frame_27)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_23.addWidget(self.frame_27)

        self.frame_31 = QFrame(self.frame_25)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.el_16_node_2 = QTextEdit(self.frame_31)
        self.el_16_node_2.setObjectName(u"el_16_node_2")
        self.el_16_node_2.setMaximumSize(QSize(270, 50))
        self.el_16_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_20.addWidget(self.el_16_node_2)


        self.verticalLayout_23.addWidget(self.frame_31)

        self.frame_28 = QFrame(self.frame_25)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.el_16_node_4_cpy = QTextEdit(self.frame_28)
        self.el_16_node_4_cpy.setObjectName(u"el_16_node_4_cpy")
        self.el_16_node_4_cpy.setMaximumSize(QSize(270, 50))
        self.el_16_node_4_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_4_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_18.addWidget(self.el_16_node_4_cpy)

        self.el_16_node_5_cpy = QTextEdit(self.frame_28)
        self.el_16_node_5_cpy.setObjectName(u"el_16_node_5_cpy")
        self.el_16_node_5_cpy.setMaximumSize(QSize(270, 50))
        self.el_16_node_5_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_5_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_18.addWidget(self.el_16_node_5_cpy)


        self.verticalLayout_23.addWidget(self.frame_28)


        self.verticalLayout_22.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_26)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_29 = QFrame(self.frame_26)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_2 = QLabel(self.frame_29)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_24.addWidget(self.frame_29)

        self.frame_32 = QFrame(self.frame_26)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.el_16_node_3 = QTextEdit(self.frame_32)
        self.el_16_node_3.setObjectName(u"el_16_node_3")
        self.el_16_node_3.setMaximumSize(QSize(270, 50))
        self.el_16_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_21.addWidget(self.el_16_node_3)


        self.verticalLayout_24.addWidget(self.frame_32)

        self.frame_30 = QFrame(self.frame_26)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.el_16_node_6_cpy = QTextEdit(self.frame_30)
        self.el_16_node_6_cpy.setObjectName(u"el_16_node_6_cpy")
        self.el_16_node_6_cpy.setMaximumSize(QSize(270, 50))
        self.el_16_node_6_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_6_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_19.addWidget(self.el_16_node_6_cpy)

        self.el_16_node_7_cpy = QTextEdit(self.frame_30)
        self.el_16_node_7_cpy.setObjectName(u"el_16_node_7_cpy")
        self.el_16_node_7_cpy.setMaximumSize(QSize(270, 50))
        self.el_16_node_7_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_7_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_19.addWidget(self.el_16_node_7_cpy)


        self.verticalLayout_24.addWidget(self.frame_30)


        self.verticalLayout_22.addWidget(self.frame_26)


        self.horizontalLayout_15.addWidget(self.frame_24)

        self.match_16.addWidget(self.HalfFinals)

        self.verticalLayout_118.addWidget(self.match_16)

        self.AllMatchesWraper.addWidget(self.MatchUnder16)
        self.MatchUnder10 = QWidget()
        self.MatchUnder10.setObjectName(u"MatchUnder10")
        self.verticalLayout_149 = QVBoxLayout(self.MatchUnder10)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.Top_menu_under10 = QFrame(self.MatchUnder10)
        self.Top_menu_under10.setObjectName(u"Top_menu_under10")
        self.Top_menu_under10.setMinimumSize(QSize(0, 60))
        self.Top_menu_under10.setMaximumSize(QSize(16777215, 100))
        self.Top_menu_under10.setFrameShape(QFrame.StyledPanel)
        self.Top_menu_under10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.Top_menu_under10)
        self.verticalLayout_164.setSpacing(0)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.verticalLayout_164.setContentsMargins(0, 0, 0, 0)
        self.Under_10_top_menu = QFrame(self.Top_menu_under10)
        self.Under_10_top_menu.setObjectName(u"Under_10_top_menu")
        self.Under_10_top_menu.setMaximumSize(QSize(16777215, 0))
        self.Under_10_top_menu.setFrameShape(QFrame.StyledPanel)
        self.Under_10_top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.Under_10_top_menu)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.Under_10_group_1_button = QPushButton(self.Under_10_top_menu)
        self.Under_10_group_1_button.setObjectName(u"Under_10_group_1_button")

        self.horizontalLayout_59.addWidget(self.Under_10_group_1_button)

        self.Under_10_group_2_button = QPushButton(self.Under_10_top_menu)
        self.Under_10_group_2_button.setObjectName(u"Under_10_group_2_button")

        self.horizontalLayout_59.addWidget(self.Under_10_group_2_button)

        self.Under_10_finals_button = QPushButton(self.Under_10_top_menu)
        self.Under_10_finals_button.setObjectName(u"Under_10_finals_button")

        self.horizontalLayout_59.addWidget(self.Under_10_finals_button)


        self.verticalLayout_164.addWidget(self.Under_10_top_menu)

        self.Top_menu_slide_button_2 = QPushButton(self.Top_menu_under10)
        self.Top_menu_slide_button_2.setObjectName(u"Top_menu_slide_button_2")
        self.Top_menu_slide_button_2.setMinimumSize(QSize(40, 40))
        self.Top_menu_slide_button_2.setMaximumSize(QSize(40, 40))
        self.Top_menu_slide_button_2.setStyleSheet(u"background:transparent;")
        self.Top_menu_slide_button_2.setIcon(icon8)

        self.verticalLayout_164.addWidget(self.Top_menu_slide_button_2, 0, Qt.AlignHCenter)


        self.verticalLayout_149.addWidget(self.Top_menu_under10)

        self.match_10 = QStackedWidget(self.MatchUnder10)
        self.match_10.setObjectName(u"match_10")
        self.match_10.setStyleSheet(u"")
        self.Grup_I_Under10 = QWidget()
        self.Grup_I_Under10.setObjectName(u"Grup_I_Under10")
        self.verticalLayout_221 = QVBoxLayout(self.Grup_I_Under10)
        self.verticalLayout_221.setObjectName(u"verticalLayout_221")
        self.label_76 = QLabel(self.Grup_I_Under10)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font1)

        self.verticalLayout_221.addWidget(self.label_76, 0, Qt.AlignHCenter)

        self.Grup_I_Under10_G1 = QStackedWidget(self.Grup_I_Under10)
        self.Grup_I_Under10_G1.setObjectName(u"Grup_I_Under10_G1")
        self.under_5_g1 = QWidget()
        self.under_5_g1.setObjectName(u"under_5_g1")
        self.horizontalLayout_60 = QHBoxLayout(self.under_5_g1)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.frame_138 = QFrame(self.under_5_g1)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.StyledPanel)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_138)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.frame_139 = QFrame(self.frame_138)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.StyledPanel)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_139)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.label_40 = QLabel(self.frame_139)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font1)

        self.verticalLayout_106.addWidget(self.label_40)


        self.verticalLayout_105.addWidget(self.frame_139)

        self.frame_140 = QFrame(self.frame_138)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.StyledPanel)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_140)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.frame_141 = QFrame(self.frame_140)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setFrameShape(QFrame.StyledPanel)
        self.frame_141.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_141)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.un_10_5_grup_1_competitor_node_1 = QTextEdit(self.frame_141)
        self.un_10_5_grup_1_competitor_node_1.setObjectName(u"un_10_5_grup_1_competitor_node_1")
        self.un_10_5_grup_1_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_107.addWidget(self.un_10_5_grup_1_competitor_node_1)

        self.un_10_5_grup_1_competitor_node_2 = QTextEdit(self.frame_141)
        self.un_10_5_grup_1_competitor_node_2.setObjectName(u"un_10_5_grup_1_competitor_node_2")
        self.un_10_5_grup_1_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_107.addWidget(self.un_10_5_grup_1_competitor_node_2)

        self.un_10_5_grup_1_competitor_node_3 = QTextEdit(self.frame_141)
        self.un_10_5_grup_1_competitor_node_3.setObjectName(u"un_10_5_grup_1_competitor_node_3")
        self.un_10_5_grup_1_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_107.addWidget(self.un_10_5_grup_1_competitor_node_3)

        self.un_10_5_grup_1_competitor_node_4 = QTextEdit(self.frame_141)
        self.un_10_5_grup_1_competitor_node_4.setObjectName(u"un_10_5_grup_1_competitor_node_4")
        self.un_10_5_grup_1_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_107.addWidget(self.un_10_5_grup_1_competitor_node_4)

        self.un_10_5_grup_1_competitor_node_5 = QTextEdit(self.frame_141)
        self.un_10_5_grup_1_competitor_node_5.setObjectName(u"un_10_5_grup_1_competitor_node_5")
        self.un_10_5_grup_1_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_107.addWidget(self.un_10_5_grup_1_competitor_node_5)


        self.horizontalLayout_68.addWidget(self.frame_141)

        self.frame_142 = QFrame(self.frame_140)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setMaximumSize(QSize(50, 16777215))
        self.frame_142.setFrameShape(QFrame.StyledPanel)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_142)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.un_10_5_grup_1_point_node_1 = QTextEdit(self.frame_142)
        self.un_10_5_grup_1_point_node_1.setObjectName(u"un_10_5_grup_1_point_node_1")
        self.un_10_5_grup_1_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_108.addWidget(self.un_10_5_grup_1_point_node_1)

        self.un_10_5_grup_1_point_node_2 = QTextEdit(self.frame_142)
        self.un_10_5_grup_1_point_node_2.setObjectName(u"un_10_5_grup_1_point_node_2")
        self.un_10_5_grup_1_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_108.addWidget(self.un_10_5_grup_1_point_node_2)

        self.un_10_5_grup_1_point_node_3 = QTextEdit(self.frame_142)
        self.un_10_5_grup_1_point_node_3.setObjectName(u"un_10_5_grup_1_point_node_3")
        self.un_10_5_grup_1_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_108.addWidget(self.un_10_5_grup_1_point_node_3)

        self.un_10_5_grup_1_point_node_4 = QTextEdit(self.frame_142)
        self.un_10_5_grup_1_point_node_4.setObjectName(u"un_10_5_grup_1_point_node_4")
        self.un_10_5_grup_1_point_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_point_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_point_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_108.addWidget(self.un_10_5_grup_1_point_node_4)

        self.un_10_5_grup_1_point_node_5 = QTextEdit(self.frame_142)
        self.un_10_5_grup_1_point_node_5.setObjectName(u"un_10_5_grup_1_point_node_5")
        self.un_10_5_grup_1_point_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_point_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_point_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_108.addWidget(self.un_10_5_grup_1_point_node_5)


        self.horizontalLayout_68.addWidget(self.frame_142)


        self.verticalLayout_105.addWidget(self.frame_140)


        self.horizontalLayout_60.addWidget(self.frame_138)

        self.frame_143 = QFrame(self.under_5_g1)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setMinimumSize(QSize(25, 0))
        self.frame_143.setFrameShape(QFrame.StyledPanel)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_143)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.label_41 = QLabel(self.frame_143)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font1)
        self.label_41.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_109.addWidget(self.label_41)

        self.frame_144 = QFrame(self.frame_143)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setEnabled(True)
        self.frame_144.setFrameShape(QFrame.NoFrame)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self._5 = QVBoxLayout(self.frame_144)
        self._5.setSpacing(0)
        self._5.setObjectName(u"_5")
        self._5.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_6 = QTextEdit(self.frame_144)
        self.un_10_5_grup_1_competitor_node_6.setObjectName(u"un_10_5_grup_1_competitor_node_6")
        self.un_10_5_grup_1_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._5.addWidget(self.un_10_5_grup_1_competitor_node_6)

        self.un_10_5_grup_1_competitor_node_7 = QTextEdit(self.frame_144)
        self.un_10_5_grup_1_competitor_node_7.setObjectName(u"un_10_5_grup_1_competitor_node_7")
        self.un_10_5_grup_1_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._5.addWidget(self.un_10_5_grup_1_competitor_node_7)


        self.verticalLayout_109.addWidget(self.frame_144)

        self.frame_152 = QFrame(self.frame_143)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.StyledPanel)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_152)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_8 = QTextEdit(self.frame_152)
        self.un_10_5_grup_1_competitor_node_8.setObjectName(u"un_10_5_grup_1_competitor_node_8")
        self.un_10_5_grup_1_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_110.addWidget(self.un_10_5_grup_1_competitor_node_8)

        self.un_10_5_grup_1_competitor_node_9 = QTextEdit(self.frame_152)
        self.un_10_5_grup_1_competitor_node_9.setObjectName(u"un_10_5_grup_1_competitor_node_9")
        self.un_10_5_grup_1_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_110.addWidget(self.un_10_5_grup_1_competitor_node_9)


        self.verticalLayout_109.addWidget(self.frame_152)


        self.horizontalLayout_60.addWidget(self.frame_143)

        self.frame_153 = QFrame(self.under_5_g1)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(25, 0))
        self.frame_153.setFrameShape(QFrame.StyledPanel)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.verticalLayout_111 = QVBoxLayout(self.frame_153)
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.label_42 = QLabel(self.frame_153)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)
        self.label_42.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_111.addWidget(self.label_42)

        self.frame_154 = QFrame(self.frame_153)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setFrameShape(QFrame.StyledPanel)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_154)
        self.verticalLayout_112.setSpacing(0)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_112.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_10 = QTextEdit(self.frame_154)
        self.un_10_5_grup_1_competitor_node_10.setObjectName(u"un_10_5_grup_1_competitor_node_10")
        self.un_10_5_grup_1_competitor_node_10.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_112.addWidget(self.un_10_5_grup_1_competitor_node_10)

        self.un_10_5_grup_1_competitor_node_11 = QTextEdit(self.frame_154)
        self.un_10_5_grup_1_competitor_node_11.setObjectName(u"un_10_5_grup_1_competitor_node_11")
        self.un_10_5_grup_1_competitor_node_11.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_112.addWidget(self.un_10_5_grup_1_competitor_node_11)


        self.verticalLayout_111.addWidget(self.frame_154)

        self.frame_155 = QFrame(self.frame_153)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)
        self.verticalLayout_113 = QVBoxLayout(self.frame_155)
        self.verticalLayout_113.setSpacing(0)
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.verticalLayout_113.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_12 = QTextEdit(self.frame_155)
        self.un_10_5_grup_1_competitor_node_12.setObjectName(u"un_10_5_grup_1_competitor_node_12")
        self.un_10_5_grup_1_competitor_node_12.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_113.addWidget(self.un_10_5_grup_1_competitor_node_12)

        self.un_10_5_grup_1_competitor_node_13 = QTextEdit(self.frame_155)
        self.un_10_5_grup_1_competitor_node_13.setObjectName(u"un_10_5_grup_1_competitor_node_13")
        self.un_10_5_grup_1_competitor_node_13.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_113.addWidget(self.un_10_5_grup_1_competitor_node_13)


        self.verticalLayout_111.addWidget(self.frame_155)


        self.horizontalLayout_60.addWidget(self.frame_153)

        self.frame_156 = QFrame(self.under_5_g1)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setMinimumSize(QSize(25, 0))
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)
        self.verticalLayout_114 = QVBoxLayout(self.frame_156)
        self.verticalLayout_114.setObjectName(u"verticalLayout_114")
        self.verticalLayout_114.setContentsMargins(0, -1, -1, -1)
        self.label_43 = QLabel(self.frame_156)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font1)
        self.label_43.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_114.addWidget(self.label_43)

        self.frame_157 = QFrame(self.frame_156)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)
        self.verticalLayout_115 = QVBoxLayout(self.frame_157)
        self.verticalLayout_115.setSpacing(0)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_14 = QTextEdit(self.frame_157)
        self.un_10_5_grup_1_competitor_node_14.setObjectName(u"un_10_5_grup_1_competitor_node_14")
        self.un_10_5_grup_1_competitor_node_14.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_115.addWidget(self.un_10_5_grup_1_competitor_node_14)

        self.un_10_5_grup_1_competitor_node_15 = QTextEdit(self.frame_157)
        self.un_10_5_grup_1_competitor_node_15.setObjectName(u"un_10_5_grup_1_competitor_node_15")
        self.un_10_5_grup_1_competitor_node_15.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_115.addWidget(self.un_10_5_grup_1_competitor_node_15)


        self.verticalLayout_114.addWidget(self.frame_157)

        self.frame_158 = QFrame(self.frame_156)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)
        self.verticalLayout_116 = QVBoxLayout(self.frame_158)
        self.verticalLayout_116.setSpacing(0)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_16 = QTextEdit(self.frame_158)
        self.un_10_5_grup_1_competitor_node_16.setObjectName(u"un_10_5_grup_1_competitor_node_16")
        self.un_10_5_grup_1_competitor_node_16.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_116.addWidget(self.un_10_5_grup_1_competitor_node_16)

        self.un_10_5_grup_1_competitor_node_17 = QTextEdit(self.frame_158)
        self.un_10_5_grup_1_competitor_node_17.setObjectName(u"un_10_5_grup_1_competitor_node_17")
        self.un_10_5_grup_1_competitor_node_17.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_17.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_17.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_116.addWidget(self.un_10_5_grup_1_competitor_node_17)


        self.verticalLayout_114.addWidget(self.frame_158)


        self.horizontalLayout_60.addWidget(self.frame_156)

        self.frame_159 = QFrame(self.under_5_g1)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setMinimumSize(QSize(25, 0))
        self.frame_159.setFrameShape(QFrame.StyledPanel)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_117 = QVBoxLayout(self.frame_159)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.label_44 = QLabel(self.frame_159)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font1)
        self.label_44.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_117.addWidget(self.label_44)

        self.frame_174 = QFrame(self.frame_159)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setFrameShape(QFrame.StyledPanel)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_174)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_18 = QTextEdit(self.frame_174)
        self.un_10_5_grup_1_competitor_node_18.setObjectName(u"un_10_5_grup_1_competitor_node_18")
        self.un_10_5_grup_1_competitor_node_18.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_18.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_18.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_119.addWidget(self.un_10_5_grup_1_competitor_node_18)

        self.un_10_5_grup_1_competitor_node_19 = QTextEdit(self.frame_174)
        self.un_10_5_grup_1_competitor_node_19.setObjectName(u"un_10_5_grup_1_competitor_node_19")
        self.un_10_5_grup_1_competitor_node_19.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_19.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_19.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_119.addWidget(self.un_10_5_grup_1_competitor_node_19)


        self.verticalLayout_117.addWidget(self.frame_174)

        self.frame_175 = QFrame(self.frame_159)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.StyledPanel)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_175)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_20 = QTextEdit(self.frame_175)
        self.un_10_5_grup_1_competitor_node_20.setObjectName(u"un_10_5_grup_1_competitor_node_20")
        self.un_10_5_grup_1_competitor_node_20.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_20.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_20.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_120.addWidget(self.un_10_5_grup_1_competitor_node_20)

        self.un_10_5_grup_1_competitor_node_21 = QTextEdit(self.frame_175)
        self.un_10_5_grup_1_competitor_node_21.setObjectName(u"un_10_5_grup_1_competitor_node_21")
        self.un_10_5_grup_1_competitor_node_21.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_21.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_21.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_120.addWidget(self.un_10_5_grup_1_competitor_node_21)


        self.verticalLayout_117.addWidget(self.frame_175)


        self.horizontalLayout_60.addWidget(self.frame_159)

        self.frame_176 = QFrame(self.under_5_g1)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setMinimumSize(QSize(50, 0))
        self.frame_176.setMaximumSize(QSize(16777215, 16777215))
        self.frame_176.setFrameShape(QFrame.StyledPanel)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.frame_176)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.label_45 = QLabel(self.frame_176)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font1)
        self.label_45.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_135.addWidget(self.label_45)

        self.frame_177 = QFrame(self.frame_176)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setFrameShape(QFrame.StyledPanel)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_177)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_22 = QTextEdit(self.frame_177)
        self.un_10_5_grup_1_competitor_node_22.setObjectName(u"un_10_5_grup_1_competitor_node_22")
        self.un_10_5_grup_1_competitor_node_22.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_22.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_22.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_136.addWidget(self.un_10_5_grup_1_competitor_node_22)

        self.un_10_5_grup_1_competitor_node_23 = QTextEdit(self.frame_177)
        self.un_10_5_grup_1_competitor_node_23.setObjectName(u"un_10_5_grup_1_competitor_node_23")
        self.un_10_5_grup_1_competitor_node_23.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_23.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_23.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_136.addWidget(self.un_10_5_grup_1_competitor_node_23)


        self.verticalLayout_135.addWidget(self.frame_177)

        self.frame_178 = QFrame(self.frame_176)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setFrameShape(QFrame.StyledPanel)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.frame_178)
        self.verticalLayout_137.setSpacing(0)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.verticalLayout_137.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_1_competitor_node_24 = QTextEdit(self.frame_178)
        self.un_10_5_grup_1_competitor_node_24.setObjectName(u"un_10_5_grup_1_competitor_node_24")
        self.un_10_5_grup_1_competitor_node_24.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_24.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_24.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_137.addWidget(self.un_10_5_grup_1_competitor_node_24)

        self.un_10_5_grup_1_competitor_node_25 = QTextEdit(self.frame_178)
        self.un_10_5_grup_1_competitor_node_25.setObjectName(u"un_10_5_grup_1_competitor_node_25")
        self.un_10_5_grup_1_competitor_node_25.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_1_competitor_node_25.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_1_competitor_node_25.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_137.addWidget(self.un_10_5_grup_1_competitor_node_25)


        self.verticalLayout_135.addWidget(self.frame_178)


        self.horizontalLayout_60.addWidget(self.frame_176)

        self.Grup_I_Under10_G1.addWidget(self.under_5_g1)
        self.under_4_g1 = QWidget()
        self.under_4_g1.setObjectName(u"under_4_g1")
        self.horizontalLayout_69 = QHBoxLayout(self.under_4_g1)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.frame_179 = QFrame(self.under_4_g1)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.frame_179)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.frame_180 = QFrame(self.frame_179)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setFrameShape(QFrame.StyledPanel)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.frame_180)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.label_46 = QLabel(self.frame_180)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)

        self.verticalLayout_139.addWidget(self.label_46)


        self.verticalLayout_138.addWidget(self.frame_180)

        self.frame_181 = QFrame(self.frame_179)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_181)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.frame_182 = QFrame(self.frame_181)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setFrameShape(QFrame.StyledPanel)
        self.frame_182.setFrameShadow(QFrame.Raised)
        self.verticalLayout_140 = QVBoxLayout(self.frame_182)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.un_10_4_grup_1_competitor_node_1 = QTextEdit(self.frame_182)
        self.un_10_4_grup_1_competitor_node_1.setObjectName(u"un_10_4_grup_1_competitor_node_1")
        self.un_10_4_grup_1_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_140.addWidget(self.un_10_4_grup_1_competitor_node_1)

        self.un_10_4_grup_1_competitor_node_2 = QTextEdit(self.frame_182)
        self.un_10_4_grup_1_competitor_node_2.setObjectName(u"un_10_4_grup_1_competitor_node_2")
        self.un_10_4_grup_1_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_140.addWidget(self.un_10_4_grup_1_competitor_node_2)

        self.un_10_4_grup_1_competitor_node_3 = QTextEdit(self.frame_182)
        self.un_10_4_grup_1_competitor_node_3.setObjectName(u"un_10_4_grup_1_competitor_node_3")
        self.un_10_4_grup_1_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_140.addWidget(self.un_10_4_grup_1_competitor_node_3)

        self.un_10_4_grup_1_competitor_node_4 = QTextEdit(self.frame_182)
        self.un_10_4_grup_1_competitor_node_4.setObjectName(u"un_10_4_grup_1_competitor_node_4")
        self.un_10_4_grup_1_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_140.addWidget(self.un_10_4_grup_1_competitor_node_4)


        self.horizontalLayout_70.addWidget(self.frame_182)

        self.frame_183 = QFrame(self.frame_181)
        self.frame_183.setObjectName(u"frame_183")
        self.frame_183.setMaximumSize(QSize(50, 16777215))
        self.frame_183.setFrameShape(QFrame.StyledPanel)
        self.frame_183.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.frame_183)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.un_10_4_grup_1_point_node_1 = QTextEdit(self.frame_183)
        self.un_10_4_grup_1_point_node_1.setObjectName(u"un_10_4_grup_1_point_node_1")
        self.un_10_4_grup_1_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_141.addWidget(self.un_10_4_grup_1_point_node_1)

        self.un_10_4_grup_1_point_node_2 = QTextEdit(self.frame_183)
        self.un_10_4_grup_1_point_node_2.setObjectName(u"un_10_4_grup_1_point_node_2")
        self.un_10_4_grup_1_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_141.addWidget(self.un_10_4_grup_1_point_node_2)

        self.un_10_4_grup_1_point_node_3 = QTextEdit(self.frame_183)
        self.un_10_4_grup_1_point_node_3.setObjectName(u"un_10_4_grup_1_point_node_3")
        self.un_10_4_grup_1_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_141.addWidget(self.un_10_4_grup_1_point_node_3)

        self.un_10_4_grup_1_point_node_4 = QTextEdit(self.frame_183)
        self.un_10_4_grup_1_point_node_4.setObjectName(u"un_10_4_grup_1_point_node_4")
        self.un_10_4_grup_1_point_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_point_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_point_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_141.addWidget(self.un_10_4_grup_1_point_node_4)


        self.horizontalLayout_70.addWidget(self.frame_183)


        self.verticalLayout_138.addWidget(self.frame_181)


        self.horizontalLayout_69.addWidget(self.frame_179)

        self.frame_184 = QFrame(self.under_4_g1)
        self.frame_184.setObjectName(u"frame_184")
        self.frame_184.setMinimumSize(QSize(25, 0))
        self.frame_184.setFrameShape(QFrame.StyledPanel)
        self.frame_184.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.frame_184)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.label_47 = QLabel(self.frame_184)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font1)
        self.label_47.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_146.addWidget(self.label_47)

        self.frame_185 = QFrame(self.frame_184)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setEnabled(True)
        self.frame_185.setFrameShape(QFrame.NoFrame)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self._6 = QVBoxLayout(self.frame_185)
        self._6.setSpacing(0)
        self._6.setObjectName(u"_6")
        self._6.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_1_competitor_node_5 = QTextEdit(self.frame_185)
        self.un_10_4_grup_1_competitor_node_5.setObjectName(u"un_10_4_grup_1_competitor_node_5")
        self.un_10_4_grup_1_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._6.addWidget(self.un_10_4_grup_1_competitor_node_5)

        self.un_10_4_grup_1_competitor_node_6 = QTextEdit(self.frame_185)
        self.un_10_4_grup_1_competitor_node_6.setObjectName(u"un_10_4_grup_1_competitor_node_6")
        self.un_10_4_grup_1_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._6.addWidget(self.un_10_4_grup_1_competitor_node_6)


        self.verticalLayout_146.addWidget(self.frame_185)

        self.frame_186 = QFrame(self.frame_184)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_186)
        self.verticalLayout_147.setSpacing(0)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.verticalLayout_147.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_1_competitor_node_7 = QTextEdit(self.frame_186)
        self.un_10_4_grup_1_competitor_node_7.setObjectName(u"un_10_4_grup_1_competitor_node_7")
        self.un_10_4_grup_1_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_147.addWidget(self.un_10_4_grup_1_competitor_node_7)

        self.un_10_4_grup_1_competitor_node_8 = QTextEdit(self.frame_186)
        self.un_10_4_grup_1_competitor_node_8.setObjectName(u"un_10_4_grup_1_competitor_node_8")
        self.un_10_4_grup_1_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_147.addWidget(self.un_10_4_grup_1_competitor_node_8)


        self.verticalLayout_146.addWidget(self.frame_186)


        self.horizontalLayout_69.addWidget(self.frame_184)

        self.frame_198 = QFrame(self.under_4_g1)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setMinimumSize(QSize(25, 0))
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_198)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.label_48 = QLabel(self.frame_198)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font1)
        self.label_48.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_148.addWidget(self.label_48)

        self.frame_199 = QFrame(self.frame_198)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_199)
        self.verticalLayout_150.setSpacing(0)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.verticalLayout_150.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_1_competitor_node_9 = QTextEdit(self.frame_199)
        self.un_10_4_grup_1_competitor_node_9.setObjectName(u"un_10_4_grup_1_competitor_node_9")
        self.un_10_4_grup_1_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_150.addWidget(self.un_10_4_grup_1_competitor_node_9)

        self.un_10_4_grup_1_competitor_node_10 = QTextEdit(self.frame_199)
        self.un_10_4_grup_1_competitor_node_10.setObjectName(u"un_10_4_grup_1_competitor_node_10")
        self.un_10_4_grup_1_competitor_node_10.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_150.addWidget(self.un_10_4_grup_1_competitor_node_10)


        self.verticalLayout_148.addWidget(self.frame_199)

        self.frame_200 = QFrame(self.frame_198)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.verticalLayout_151 = QVBoxLayout(self.frame_200)
        self.verticalLayout_151.setSpacing(0)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.verticalLayout_151.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_1_competitor_node_11 = QTextEdit(self.frame_200)
        self.un_10_4_grup_1_competitor_node_11.setObjectName(u"un_10_4_grup_1_competitor_node_11")
        self.un_10_4_grup_1_competitor_node_11.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_151.addWidget(self.un_10_4_grup_1_competitor_node_11)

        self.un_10_4_grup_1_competitor_node_12 = QTextEdit(self.frame_200)
        self.un_10_4_grup_1_competitor_node_12.setObjectName(u"un_10_4_grup_1_competitor_node_12")
        self.un_10_4_grup_1_competitor_node_12.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_151.addWidget(self.un_10_4_grup_1_competitor_node_12)


        self.verticalLayout_148.addWidget(self.frame_200)


        self.horizontalLayout_69.addWidget(self.frame_198)

        self.frame_201 = QFrame(self.under_4_g1)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setMinimumSize(QSize(25, 0))
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.frame_201)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.verticalLayout_152.setContentsMargins(0, -1, -1, -1)
        self.label_49 = QLabel(self.frame_201)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)
        self.label_49.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_152.addWidget(self.label_49)

        self.frame_202 = QFrame(self.frame_201)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_202)
        self.verticalLayout_153.setSpacing(0)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.verticalLayout_153.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_1_competitor_node_13 = QTextEdit(self.frame_202)
        self.un_10_4_grup_1_competitor_node_13.setObjectName(u"un_10_4_grup_1_competitor_node_13")
        self.un_10_4_grup_1_competitor_node_13.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_153.addWidget(self.un_10_4_grup_1_competitor_node_13)

        self.un_10_4_grup_1_competitor_node_14 = QTextEdit(self.frame_202)
        self.un_10_4_grup_1_competitor_node_14.setObjectName(u"un_10_4_grup_1_competitor_node_14")
        self.un_10_4_grup_1_competitor_node_14.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_153.addWidget(self.un_10_4_grup_1_competitor_node_14)


        self.verticalLayout_152.addWidget(self.frame_202)

        self.frame_203 = QFrame(self.frame_201)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_203)
        self.verticalLayout_154.setSpacing(0)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.verticalLayout_154.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_1_competitor_node_15 = QTextEdit(self.frame_203)
        self.un_10_4_grup_1_competitor_node_15.setObjectName(u"un_10_4_grup_1_competitor_node_15")
        self.un_10_4_grup_1_competitor_node_15.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_154.addWidget(self.un_10_4_grup_1_competitor_node_15)

        self.un_10_4_grup_1_competitor_node_16 = QTextEdit(self.frame_203)
        self.un_10_4_grup_1_competitor_node_16.setObjectName(u"un_10_4_grup_1_competitor_node_16")
        self.un_10_4_grup_1_competitor_node_16.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_1_competitor_node_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_1_competitor_node_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_154.addWidget(self.un_10_4_grup_1_competitor_node_16)


        self.verticalLayout_152.addWidget(self.frame_203)


        self.horizontalLayout_69.addWidget(self.frame_201)

        self.Grup_I_Under10_G1.addWidget(self.under_4_g1)
        self.under_3_g1 = QWidget()
        self.under_3_g1.setObjectName(u"under_3_g1")
        self.horizontalLayout_71 = QHBoxLayout(self.under_3_g1)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.frame_204 = QFrame(self.under_3_g1)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_204)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.frame_205 = QFrame(self.frame_204)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_205)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.label_50 = QLabel(self.frame_205)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)

        self.verticalLayout_156.addWidget(self.label_50)


        self.verticalLayout_155.addWidget(self.frame_205)

        self.frame_206 = QFrame(self.frame_204)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.frame_207 = QFrame(self.frame_206)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_207)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.un_10_3_grup_1_competitor_node_1 = QTextEdit(self.frame_207)
        self.un_10_3_grup_1_competitor_node_1.setObjectName(u"un_10_3_grup_1_competitor_node_1")
        self.un_10_3_grup_1_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_157.addWidget(self.un_10_3_grup_1_competitor_node_1)

        self.un_10_3_grup_1_competitor_node_2 = QTextEdit(self.frame_207)
        self.un_10_3_grup_1_competitor_node_2.setObjectName(u"un_10_3_grup_1_competitor_node_2")
        self.un_10_3_grup_1_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_157.addWidget(self.un_10_3_grup_1_competitor_node_2)

        self.un_10_3_grup_1_competitor_node_3 = QTextEdit(self.frame_207)
        self.un_10_3_grup_1_competitor_node_3.setObjectName(u"un_10_3_grup_1_competitor_node_3")
        self.un_10_3_grup_1_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_157.addWidget(self.un_10_3_grup_1_competitor_node_3)


        self.horizontalLayout_73.addWidget(self.frame_207)

        self.frame_208 = QFrame(self.frame_206)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMaximumSize(QSize(50, 16777215))
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_208)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.un_10_3_grup_1_point_node_1 = QTextEdit(self.frame_208)
        self.un_10_3_grup_1_point_node_1.setObjectName(u"un_10_3_grup_1_point_node_1")
        self.un_10_3_grup_1_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_158.addWidget(self.un_10_3_grup_1_point_node_1)

        self.un_10_3_grup_1_point_node_2 = QTextEdit(self.frame_208)
        self.un_10_3_grup_1_point_node_2.setObjectName(u"un_10_3_grup_1_point_node_2")
        self.un_10_3_grup_1_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_158.addWidget(self.un_10_3_grup_1_point_node_2)

        self.un_10_3_grup_1_point_node_3 = QTextEdit(self.frame_208)
        self.un_10_3_grup_1_point_node_3.setObjectName(u"un_10_3_grup_1_point_node_3")
        self.un_10_3_grup_1_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_158.addWidget(self.un_10_3_grup_1_point_node_3)


        self.horizontalLayout_73.addWidget(self.frame_208)


        self.verticalLayout_155.addWidget(self.frame_206)


        self.horizontalLayout_71.addWidget(self.frame_204)

        self.frame_209 = QFrame(self.under_3_g1)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setMinimumSize(QSize(25, 0))
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_209)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.label_51 = QLabel(self.frame_209)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)
        self.label_51.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_159.addWidget(self.label_51)

        self.frame_210 = QFrame(self.frame_209)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setEnabled(True)
        self.frame_210.setFrameShape(QFrame.NoFrame)
        self.frame_210.setFrameShadow(QFrame.Raised)
        self._7 = QVBoxLayout(self.frame_210)
        self._7.setSpacing(0)
        self._7.setObjectName(u"_7")
        self._7.setContentsMargins(0, 0, 0, 0)
        self.un_10_3_grup_1_competitor_node_4 = QTextEdit(self.frame_210)
        self.un_10_3_grup_1_competitor_node_4.setObjectName(u"un_10_3_grup_1_competitor_node_4")
        self.un_10_3_grup_1_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._7.addWidget(self.un_10_3_grup_1_competitor_node_4)

        self.un_10_3_grup_1_competitor_node_5 = QTextEdit(self.frame_210)
        self.un_10_3_grup_1_competitor_node_5.setObjectName(u"un_10_3_grup_1_competitor_node_5")
        self.un_10_3_grup_1_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._7.addWidget(self.un_10_3_grup_1_competitor_node_5)


        self.verticalLayout_159.addWidget(self.frame_210)


        self.horizontalLayout_71.addWidget(self.frame_209)

        self.frame_211 = QFrame(self.under_3_g1)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setMinimumSize(QSize(25, 0))
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_211)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.label_52 = QLabel(self.frame_211)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)
        self.label_52.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_160.addWidget(self.label_52)

        self.frame_212 = QFrame(self.frame_211)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_212)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.un_10_3_grup_1_competitor_node_6 = QTextEdit(self.frame_212)
        self.un_10_3_grup_1_competitor_node_6.setObjectName(u"un_10_3_grup_1_competitor_node_6")
        self.un_10_3_grup_1_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_161.addWidget(self.un_10_3_grup_1_competitor_node_6)

        self.un_10_3_grup_1_competitor_node_7 = QTextEdit(self.frame_212)
        self.un_10_3_grup_1_competitor_node_7.setObjectName(u"un_10_3_grup_1_competitor_node_7")
        self.un_10_3_grup_1_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_161.addWidget(self.un_10_3_grup_1_competitor_node_7)


        self.verticalLayout_160.addWidget(self.frame_212)


        self.horizontalLayout_71.addWidget(self.frame_211)

        self.frame_213 = QFrame(self.under_3_g1)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setMinimumSize(QSize(25, 0))
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_213)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.verticalLayout_162.setContentsMargins(0, -1, -1, -1)
        self.label_53 = QLabel(self.frame_213)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)
        self.label_53.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_162.addWidget(self.label_53)

        self.frame_214 = QFrame(self.frame_213)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_214)
        self.verticalLayout_163.setSpacing(0)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.verticalLayout_163.setContentsMargins(0, 0, 0, 0)
        self.un_10_3_grup_1_competitor_node_8 = QTextEdit(self.frame_214)
        self.un_10_3_grup_1_competitor_node_8.setObjectName(u"un_10_3_grup_1_competitor_node_8")
        self.un_10_3_grup_1_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_163.addWidget(self.un_10_3_grup_1_competitor_node_8)

        self.un_10_3_grup_1_competitor_node_9 = QTextEdit(self.frame_214)
        self.un_10_3_grup_1_competitor_node_9.setObjectName(u"un_10_3_grup_1_competitor_node_9")
        self.un_10_3_grup_1_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_1_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_1_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_163.addWidget(self.un_10_3_grup_1_competitor_node_9)


        self.verticalLayout_162.addWidget(self.frame_214)


        self.horizontalLayout_71.addWidget(self.frame_213)

        self.Grup_I_Under10_G1.addWidget(self.under_3_g1)

        self.verticalLayout_221.addWidget(self.Grup_I_Under10_G1)

        self.match_10.addWidget(self.Grup_I_Under10)
        self.Grup_II_Under10 = QWidget()
        self.Grup_II_Under10.setObjectName(u"Grup_II_Under10")
        self.verticalLayout_222 = QVBoxLayout(self.Grup_II_Under10)
        self.verticalLayout_222.setObjectName(u"verticalLayout_222")
        self.label_77 = QLabel(self.Grup_II_Under10)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font1)

        self.verticalLayout_222.addWidget(self.label_77, 0, Qt.AlignHCenter)

        self.Top_menu_wraper_2 = QFrame(self.Grup_II_Under10)
        self.Top_menu_wraper_2.setObjectName(u"Top_menu_wraper_2")
        self.Top_menu_wraper_2.setMaximumSize(QSize(16777215, 100))
        self.Top_menu_wraper_2.setFrameShape(QFrame.StyledPanel)
        self.Top_menu_wraper_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.Top_menu_wraper_2)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_222.addWidget(self.Top_menu_wraper_2, 0, Qt.AlignHCenter)

        self.Grup_II_Under10_G2 = QStackedWidget(self.Grup_II_Under10)
        self.Grup_II_Under10_G2.setObjectName(u"Grup_II_Under10_G2")
        self.under_5_g2 = QWidget()
        self.under_5_g2.setObjectName(u"under_5_g2")
        self.horizontalLayout_72 = QHBoxLayout(self.under_5_g2)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.frame_226 = QFrame(self.under_5_g2)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setFrameShape(QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_226)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.frame_227 = QFrame(self.frame_226)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.frame_227)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.label_58 = QLabel(self.frame_227)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)

        self.verticalLayout_174.addWidget(self.label_58)


        self.verticalLayout_173.addWidget(self.frame_227)

        self.frame_228 = QFrame(self.frame_226)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_228)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.frame_229 = QFrame(self.frame_228)
        self.frame_229.setObjectName(u"frame_229")
        self.frame_229.setFrameShape(QFrame.StyledPanel)
        self.frame_229.setFrameShadow(QFrame.Raised)
        self.verticalLayout_175 = QVBoxLayout(self.frame_229)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.un_10_5_grup_2_competitor_node_1 = QTextEdit(self.frame_229)
        self.un_10_5_grup_2_competitor_node_1.setObjectName(u"un_10_5_grup_2_competitor_node_1")
        self.un_10_5_grup_2_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_175.addWidget(self.un_10_5_grup_2_competitor_node_1)

        self.un_10_5_grup_2_competitor_node_2 = QTextEdit(self.frame_229)
        self.un_10_5_grup_2_competitor_node_2.setObjectName(u"un_10_5_grup_2_competitor_node_2")
        self.un_10_5_grup_2_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_175.addWidget(self.un_10_5_grup_2_competitor_node_2)

        self.un_10_5_grup_2_competitor_node_3 = QTextEdit(self.frame_229)
        self.un_10_5_grup_2_competitor_node_3.setObjectName(u"un_10_5_grup_2_competitor_node_3")
        self.un_10_5_grup_2_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_175.addWidget(self.un_10_5_grup_2_competitor_node_3)

        self.un_10_5_grup_2_competitor_node_4 = QTextEdit(self.frame_229)
        self.un_10_5_grup_2_competitor_node_4.setObjectName(u"un_10_5_grup_2_competitor_node_4")
        self.un_10_5_grup_2_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_175.addWidget(self.un_10_5_grup_2_competitor_node_4)

        self.un_10_5_grup_2_competitor_node_5 = QTextEdit(self.frame_229)
        self.un_10_5_grup_2_competitor_node_5.setObjectName(u"un_10_5_grup_2_competitor_node_5")
        self.un_10_5_grup_2_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_175.addWidget(self.un_10_5_grup_2_competitor_node_5)


        self.horizontalLayout_85.addWidget(self.frame_229)

        self.frame_230 = QFrame(self.frame_228)
        self.frame_230.setObjectName(u"frame_230")
        self.frame_230.setMaximumSize(QSize(50, 16777215))
        self.frame_230.setFrameShape(QFrame.StyledPanel)
        self.frame_230.setFrameShadow(QFrame.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_230)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.un_10_5_grup_2_point_node_1 = QTextEdit(self.frame_230)
        self.un_10_5_grup_2_point_node_1.setObjectName(u"un_10_5_grup_2_point_node_1")
        self.un_10_5_grup_2_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_176.addWidget(self.un_10_5_grup_2_point_node_1)

        self.un_10_5_grup_2_point_node_2 = QTextEdit(self.frame_230)
        self.un_10_5_grup_2_point_node_2.setObjectName(u"un_10_5_grup_2_point_node_2")
        self.un_10_5_grup_2_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_176.addWidget(self.un_10_5_grup_2_point_node_2)

        self.un_10_5_grup_2_point_node_3 = QTextEdit(self.frame_230)
        self.un_10_5_grup_2_point_node_3.setObjectName(u"un_10_5_grup_2_point_node_3")
        self.un_10_5_grup_2_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_176.addWidget(self.un_10_5_grup_2_point_node_3)

        self.un_10_5_grup_2_point_node_4 = QTextEdit(self.frame_230)
        self.un_10_5_grup_2_point_node_4.setObjectName(u"un_10_5_grup_2_point_node_4")
        self.un_10_5_grup_2_point_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_point_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_point_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_176.addWidget(self.un_10_5_grup_2_point_node_4)

        self.un_10_5_grup_2_point_node_5 = QTextEdit(self.frame_230)
        self.un_10_5_grup_2_point_node_5.setObjectName(u"un_10_5_grup_2_point_node_5")
        self.un_10_5_grup_2_point_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_point_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_point_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_176.addWidget(self.un_10_5_grup_2_point_node_5)


        self.horizontalLayout_85.addWidget(self.frame_230)


        self.verticalLayout_173.addWidget(self.frame_228)


        self.horizontalLayout_72.addWidget(self.frame_226)

        self.frame_231 = QFrame(self.under_5_g2)
        self.frame_231.setObjectName(u"frame_231")
        self.frame_231.setMinimumSize(QSize(25, 0))
        self.frame_231.setFrameShape(QFrame.StyledPanel)
        self.frame_231.setFrameShadow(QFrame.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_231)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.label_59 = QLabel(self.frame_231)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font1)
        self.label_59.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_177.addWidget(self.label_59)

        self.frame_232 = QFrame(self.frame_231)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setEnabled(True)
        self.frame_232.setFrameShape(QFrame.NoFrame)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self._9 = QVBoxLayout(self.frame_232)
        self._9.setSpacing(0)
        self._9.setObjectName(u"_9")
        self._9.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_6 = QTextEdit(self.frame_232)
        self.un_10_5_grup_2_competitor_node_6.setObjectName(u"un_10_5_grup_2_competitor_node_6")
        self.un_10_5_grup_2_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._9.addWidget(self.un_10_5_grup_2_competitor_node_6)

        self.un_10_5_grup_2_competitor_node_7 = QTextEdit(self.frame_232)
        self.un_10_5_grup_2_competitor_node_7.setObjectName(u"un_10_5_grup_2_competitor_node_7")
        self.un_10_5_grup_2_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._9.addWidget(self.un_10_5_grup_2_competitor_node_7)


        self.verticalLayout_177.addWidget(self.frame_232)

        self.frame_233 = QFrame(self.frame_231)
        self.frame_233.setObjectName(u"frame_233")
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)
        self.verticalLayout_178 = QVBoxLayout(self.frame_233)
        self.verticalLayout_178.setSpacing(0)
        self.verticalLayout_178.setObjectName(u"verticalLayout_178")
        self.verticalLayout_178.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_8 = QTextEdit(self.frame_233)
        self.un_10_5_grup_2_competitor_node_8.setObjectName(u"un_10_5_grup_2_competitor_node_8")
        self.un_10_5_grup_2_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_178.addWidget(self.un_10_5_grup_2_competitor_node_8)

        self.un_10_5_grup_2_competitor_node_9 = QTextEdit(self.frame_233)
        self.un_10_5_grup_2_competitor_node_9.setObjectName(u"un_10_5_grup_2_competitor_node_9")
        self.un_10_5_grup_2_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_178.addWidget(self.un_10_5_grup_2_competitor_node_9)


        self.verticalLayout_177.addWidget(self.frame_233)


        self.horizontalLayout_72.addWidget(self.frame_231)

        self.frame_234 = QFrame(self.under_5_g2)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setMinimumSize(QSize(25, 0))
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.verticalLayout_179 = QVBoxLayout(self.frame_234)
        self.verticalLayout_179.setObjectName(u"verticalLayout_179")
        self.label_60 = QLabel(self.frame_234)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)
        self.label_60.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_179.addWidget(self.label_60)

        self.frame_235 = QFrame(self.frame_234)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.verticalLayout_180 = QVBoxLayout(self.frame_235)
        self.verticalLayout_180.setSpacing(0)
        self.verticalLayout_180.setObjectName(u"verticalLayout_180")
        self.verticalLayout_180.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_10 = QTextEdit(self.frame_235)
        self.un_10_5_grup_2_competitor_node_10.setObjectName(u"un_10_5_grup_2_competitor_node_10")
        self.un_10_5_grup_2_competitor_node_10.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_180.addWidget(self.un_10_5_grup_2_competitor_node_10)

        self.un_10_5_grup_2_competitor_node_11 = QTextEdit(self.frame_235)
        self.un_10_5_grup_2_competitor_node_11.setObjectName(u"un_10_5_grup_2_competitor_node_11")
        self.un_10_5_grup_2_competitor_node_11.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_180.addWidget(self.un_10_5_grup_2_competitor_node_11)


        self.verticalLayout_179.addWidget(self.frame_235)

        self.frame_236 = QFrame(self.frame_234)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.verticalLayout_181 = QVBoxLayout(self.frame_236)
        self.verticalLayout_181.setSpacing(0)
        self.verticalLayout_181.setObjectName(u"verticalLayout_181")
        self.verticalLayout_181.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_12 = QTextEdit(self.frame_236)
        self.un_10_5_grup_2_competitor_node_12.setObjectName(u"un_10_5_grup_2_competitor_node_12")
        self.un_10_5_grup_2_competitor_node_12.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_181.addWidget(self.un_10_5_grup_2_competitor_node_12)

        self.un_10_5_grup_2_competitor_node_13 = QTextEdit(self.frame_236)
        self.un_10_5_grup_2_competitor_node_13.setObjectName(u"un_10_5_grup_2_competitor_node_13")
        self.un_10_5_grup_2_competitor_node_13.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_181.addWidget(self.un_10_5_grup_2_competitor_node_13)


        self.verticalLayout_179.addWidget(self.frame_236)


        self.horizontalLayout_72.addWidget(self.frame_234)

        self.frame_237 = QFrame(self.under_5_g2)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setMinimumSize(QSize(25, 0))
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.verticalLayout_182 = QVBoxLayout(self.frame_237)
        self.verticalLayout_182.setObjectName(u"verticalLayout_182")
        self.verticalLayout_182.setContentsMargins(0, -1, -1, -1)
        self.label_61 = QLabel(self.frame_237)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font1)
        self.label_61.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_182.addWidget(self.label_61)

        self.frame_238 = QFrame(self.frame_237)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)
        self.verticalLayout_183 = QVBoxLayout(self.frame_238)
        self.verticalLayout_183.setSpacing(0)
        self.verticalLayout_183.setObjectName(u"verticalLayout_183")
        self.verticalLayout_183.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_14 = QTextEdit(self.frame_238)
        self.un_10_5_grup_2_competitor_node_14.setObjectName(u"un_10_5_grup_2_competitor_node_14")
        self.un_10_5_grup_2_competitor_node_14.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_183.addWidget(self.un_10_5_grup_2_competitor_node_14)

        self.un_10_5_grup_2_competitor_node_15 = QTextEdit(self.frame_238)
        self.un_10_5_grup_2_competitor_node_15.setObjectName(u"un_10_5_grup_2_competitor_node_15")
        self.un_10_5_grup_2_competitor_node_15.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_183.addWidget(self.un_10_5_grup_2_competitor_node_15)


        self.verticalLayout_182.addWidget(self.frame_238)

        self.frame_239 = QFrame(self.frame_237)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.verticalLayout_184 = QVBoxLayout(self.frame_239)
        self.verticalLayout_184.setSpacing(0)
        self.verticalLayout_184.setObjectName(u"verticalLayout_184")
        self.verticalLayout_184.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_16 = QTextEdit(self.frame_239)
        self.un_10_5_grup_2_competitor_node_16.setObjectName(u"un_10_5_grup_2_competitor_node_16")
        self.un_10_5_grup_2_competitor_node_16.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_184.addWidget(self.un_10_5_grup_2_competitor_node_16)

        self.un_10_5_grup_2_competitor_node_17 = QTextEdit(self.frame_239)
        self.un_10_5_grup_2_competitor_node_17.setObjectName(u"un_10_5_grup_2_competitor_node_17")
        self.un_10_5_grup_2_competitor_node_17.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_17.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_17.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_184.addWidget(self.un_10_5_grup_2_competitor_node_17)


        self.verticalLayout_182.addWidget(self.frame_239)


        self.horizontalLayout_72.addWidget(self.frame_237)

        self.frame_240 = QFrame(self.under_5_g2)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setMinimumSize(QSize(25, 0))
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.verticalLayout_185 = QVBoxLayout(self.frame_240)
        self.verticalLayout_185.setObjectName(u"verticalLayout_185")
        self.label_62 = QLabel(self.frame_240)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font1)
        self.label_62.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_185.addWidget(self.label_62)

        self.frame_241 = QFrame(self.frame_240)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setFrameShape(QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Raised)
        self.verticalLayout_186 = QVBoxLayout(self.frame_241)
        self.verticalLayout_186.setSpacing(0)
        self.verticalLayout_186.setObjectName(u"verticalLayout_186")
        self.verticalLayout_186.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_18 = QTextEdit(self.frame_241)
        self.un_10_5_grup_2_competitor_node_18.setObjectName(u"un_10_5_grup_2_competitor_node_18")
        self.un_10_5_grup_2_competitor_node_18.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_18.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_18.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_186.addWidget(self.un_10_5_grup_2_competitor_node_18)

        self.un_10_5_grup_2_competitor_node_19 = QTextEdit(self.frame_241)
        self.un_10_5_grup_2_competitor_node_19.setObjectName(u"un_10_5_grup_2_competitor_node_19")
        self.un_10_5_grup_2_competitor_node_19.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_19.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_19.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_186.addWidget(self.un_10_5_grup_2_competitor_node_19)


        self.verticalLayout_185.addWidget(self.frame_241)

        self.frame_242 = QFrame(self.frame_240)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setFrameShape(QFrame.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Raised)
        self.verticalLayout_187 = QVBoxLayout(self.frame_242)
        self.verticalLayout_187.setSpacing(0)
        self.verticalLayout_187.setObjectName(u"verticalLayout_187")
        self.verticalLayout_187.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_20 = QTextEdit(self.frame_242)
        self.un_10_5_grup_2_competitor_node_20.setObjectName(u"un_10_5_grup_2_competitor_node_20")
        self.un_10_5_grup_2_competitor_node_20.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_20.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_20.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_187.addWidget(self.un_10_5_grup_2_competitor_node_20)

        self.un_10_5_grup_2_competitor_node_21 = QTextEdit(self.frame_242)
        self.un_10_5_grup_2_competitor_node_21.setObjectName(u"un_10_5_grup_2_competitor_node_21")
        self.un_10_5_grup_2_competitor_node_21.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_21.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_21.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_187.addWidget(self.un_10_5_grup_2_competitor_node_21)


        self.verticalLayout_185.addWidget(self.frame_242)


        self.horizontalLayout_72.addWidget(self.frame_240)

        self.frame_243 = QFrame(self.under_5_g2)
        self.frame_243.setObjectName(u"frame_243")
        self.frame_243.setMinimumSize(QSize(50, 0))
        self.frame_243.setMaximumSize(QSize(16777215, 16777215))
        self.frame_243.setFrameShape(QFrame.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Raised)
        self.verticalLayout_188 = QVBoxLayout(self.frame_243)
        self.verticalLayout_188.setObjectName(u"verticalLayout_188")
        self.label_63 = QLabel(self.frame_243)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font1)
        self.label_63.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_188.addWidget(self.label_63)

        self.frame_244 = QFrame(self.frame_243)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setFrameShape(QFrame.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Raised)
        self.verticalLayout_189 = QVBoxLayout(self.frame_244)
        self.verticalLayout_189.setSpacing(0)
        self.verticalLayout_189.setObjectName(u"verticalLayout_189")
        self.verticalLayout_189.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_22 = QTextEdit(self.frame_244)
        self.un_10_5_grup_2_competitor_node_22.setObjectName(u"un_10_5_grup_2_competitor_node_22")
        self.un_10_5_grup_2_competitor_node_22.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_22.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_22.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_189.addWidget(self.un_10_5_grup_2_competitor_node_22)

        self.un_10_5_grup_2_competitor_node_23 = QTextEdit(self.frame_244)
        self.un_10_5_grup_2_competitor_node_23.setObjectName(u"un_10_5_grup_2_competitor_node_23")
        self.un_10_5_grup_2_competitor_node_23.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_23.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_23.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_189.addWidget(self.un_10_5_grup_2_competitor_node_23)


        self.verticalLayout_188.addWidget(self.frame_244)

        self.frame_245 = QFrame(self.frame_243)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setFrameShape(QFrame.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Raised)
        self.verticalLayout_190 = QVBoxLayout(self.frame_245)
        self.verticalLayout_190.setSpacing(0)
        self.verticalLayout_190.setObjectName(u"verticalLayout_190")
        self.verticalLayout_190.setContentsMargins(0, 0, 0, 0)
        self.un_10_5_grup_2_competitor_node_24 = QTextEdit(self.frame_245)
        self.un_10_5_grup_2_competitor_node_24.setObjectName(u"un_10_5_grup_2_competitor_node_24")
        self.un_10_5_grup_2_competitor_node_24.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_24.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_24.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_190.addWidget(self.un_10_5_grup_2_competitor_node_24)

        self.un_10_5_grup_2_competitor_node_25 = QTextEdit(self.frame_245)
        self.un_10_5_grup_2_competitor_node_25.setObjectName(u"un_10_5_grup_2_competitor_node_25")
        self.un_10_5_grup_2_competitor_node_25.setMaximumSize(QSize(16777215, 50))
        self.un_10_5_grup_2_competitor_node_25.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_5_grup_2_competitor_node_25.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_190.addWidget(self.un_10_5_grup_2_competitor_node_25)


        self.verticalLayout_188.addWidget(self.frame_245)


        self.horizontalLayout_72.addWidget(self.frame_243)

        self.Grup_II_Under10_G2.addWidget(self.under_5_g2)
        self.under_4_g2 = QWidget()
        self.under_4_g2.setObjectName(u"under_4_g2")
        self.horizontalLayout_86 = QHBoxLayout(self.under_4_g2)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.frame_246 = QFrame(self.under_4_g2)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setFrameShape(QFrame.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Raised)
        self.verticalLayout_191 = QVBoxLayout(self.frame_246)
        self.verticalLayout_191.setObjectName(u"verticalLayout_191")
        self.frame_247 = QFrame(self.frame_246)
        self.frame_247.setObjectName(u"frame_247")
        self.frame_247.setFrameShape(QFrame.StyledPanel)
        self.frame_247.setFrameShadow(QFrame.Raised)
        self.verticalLayout_192 = QVBoxLayout(self.frame_247)
        self.verticalLayout_192.setObjectName(u"verticalLayout_192")
        self.label_64 = QLabel(self.frame_247)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font1)

        self.verticalLayout_192.addWidget(self.label_64)


        self.verticalLayout_191.addWidget(self.frame_247)

        self.frame_248 = QFrame(self.frame_246)
        self.frame_248.setObjectName(u"frame_248")
        self.frame_248.setFrameShape(QFrame.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_248)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.frame_249 = QFrame(self.frame_248)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)
        self.verticalLayout_193 = QVBoxLayout(self.frame_249)
        self.verticalLayout_193.setObjectName(u"verticalLayout_193")
        self.un_10_4_grup_2_competitor_node_1 = QTextEdit(self.frame_249)
        self.un_10_4_grup_2_competitor_node_1.setObjectName(u"un_10_4_grup_2_competitor_node_1")
        self.un_10_4_grup_2_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_193.addWidget(self.un_10_4_grup_2_competitor_node_1)

        self.un_10_4_grup_2_competitor_node_2 = QTextEdit(self.frame_249)
        self.un_10_4_grup_2_competitor_node_2.setObjectName(u"un_10_4_grup_2_competitor_node_2")
        self.un_10_4_grup_2_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_193.addWidget(self.un_10_4_grup_2_competitor_node_2)

        self.un_10_4_grup_2_competitor_node_3 = QTextEdit(self.frame_249)
        self.un_10_4_grup_2_competitor_node_3.setObjectName(u"un_10_4_grup_2_competitor_node_3")
        self.un_10_4_grup_2_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_193.addWidget(self.un_10_4_grup_2_competitor_node_3)

        self.un_10_4_grup_2_competitor_node_4 = QTextEdit(self.frame_249)
        self.un_10_4_grup_2_competitor_node_4.setObjectName(u"un_10_4_grup_2_competitor_node_4")
        self.un_10_4_grup_2_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_193.addWidget(self.un_10_4_grup_2_competitor_node_4)


        self.horizontalLayout_87.addWidget(self.frame_249)

        self.frame_250 = QFrame(self.frame_248)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setMaximumSize(QSize(50, 16777215))
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)
        self.verticalLayout_194 = QVBoxLayout(self.frame_250)
        self.verticalLayout_194.setObjectName(u"verticalLayout_194")
        self.un_10_4_grup_2_point_node_1 = QTextEdit(self.frame_250)
        self.un_10_4_grup_2_point_node_1.setObjectName(u"un_10_4_grup_2_point_node_1")
        self.un_10_4_grup_2_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_194.addWidget(self.un_10_4_grup_2_point_node_1)

        self.un_10_4_grup_2_point_node_2 = QTextEdit(self.frame_250)
        self.un_10_4_grup_2_point_node_2.setObjectName(u"un_10_4_grup_2_point_node_2")
        self.un_10_4_grup_2_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_194.addWidget(self.un_10_4_grup_2_point_node_2)

        self.un_10_4_grup_2_point_node_3 = QTextEdit(self.frame_250)
        self.un_10_4_grup_2_point_node_3.setObjectName(u"un_10_4_grup_2_point_node_3")
        self.un_10_4_grup_2_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_194.addWidget(self.un_10_4_grup_2_point_node_3)

        self.un_10_4_grup_2_point_node_4 = QTextEdit(self.frame_250)
        self.un_10_4_grup_2_point_node_4.setObjectName(u"un_10_4_grup_2_point_node_4")
        self.un_10_4_grup_2_point_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_point_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_point_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_194.addWidget(self.un_10_4_grup_2_point_node_4)


        self.horizontalLayout_87.addWidget(self.frame_250)


        self.verticalLayout_191.addWidget(self.frame_248)


        self.horizontalLayout_86.addWidget(self.frame_246)

        self.frame_251 = QFrame(self.under_4_g2)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(25, 0))
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)
        self.verticalLayout_195 = QVBoxLayout(self.frame_251)
        self.verticalLayout_195.setObjectName(u"verticalLayout_195")
        self.label_65 = QLabel(self.frame_251)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font1)
        self.label_65.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_195.addWidget(self.label_65)

        self.frame_252 = QFrame(self.frame_251)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setEnabled(True)
        self.frame_252.setFrameShape(QFrame.NoFrame)
        self.frame_252.setFrameShadow(QFrame.Raised)
        self._10 = QVBoxLayout(self.frame_252)
        self._10.setSpacing(0)
        self._10.setObjectName(u"_10")
        self._10.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_2_competitor_node_5 = QTextEdit(self.frame_252)
        self.un_10_4_grup_2_competitor_node_5.setObjectName(u"un_10_4_grup_2_competitor_node_5")
        self.un_10_4_grup_2_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._10.addWidget(self.un_10_4_grup_2_competitor_node_5)

        self.un_10_4_grup_2_competitor_node_6 = QTextEdit(self.frame_252)
        self.un_10_4_grup_2_competitor_node_6.setObjectName(u"un_10_4_grup_2_competitor_node_6")
        self.un_10_4_grup_2_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._10.addWidget(self.un_10_4_grup_2_competitor_node_6)


        self.verticalLayout_195.addWidget(self.frame_252)

        self.frame_253 = QFrame(self.frame_251)
        self.frame_253.setObjectName(u"frame_253")
        self.frame_253.setFrameShape(QFrame.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Raised)
        self.verticalLayout_196 = QVBoxLayout(self.frame_253)
        self.verticalLayout_196.setSpacing(0)
        self.verticalLayout_196.setObjectName(u"verticalLayout_196")
        self.verticalLayout_196.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_2_competitor_node_7 = QTextEdit(self.frame_253)
        self.un_10_4_grup_2_competitor_node_7.setObjectName(u"un_10_4_grup_2_competitor_node_7")
        self.un_10_4_grup_2_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_196.addWidget(self.un_10_4_grup_2_competitor_node_7)

        self.un_10_4_grup_2_competitor_node_8 = QTextEdit(self.frame_253)
        self.un_10_4_grup_2_competitor_node_8.setObjectName(u"un_10_4_grup_2_competitor_node_8")
        self.un_10_4_grup_2_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_196.addWidget(self.un_10_4_grup_2_competitor_node_8)


        self.verticalLayout_195.addWidget(self.frame_253)


        self.horizontalLayout_86.addWidget(self.frame_251)

        self.frame_254 = QFrame(self.under_4_g2)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setMinimumSize(QSize(25, 0))
        self.frame_254.setFrameShape(QFrame.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Raised)
        self.verticalLayout_197 = QVBoxLayout(self.frame_254)
        self.verticalLayout_197.setObjectName(u"verticalLayout_197")
        self.label_66 = QLabel(self.frame_254)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font1)
        self.label_66.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_197.addWidget(self.label_66)

        self.frame_255 = QFrame(self.frame_254)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setFrameShape(QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Raised)
        self.verticalLayout_198 = QVBoxLayout(self.frame_255)
        self.verticalLayout_198.setSpacing(0)
        self.verticalLayout_198.setObjectName(u"verticalLayout_198")
        self.verticalLayout_198.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_2_competitor_node_9 = QTextEdit(self.frame_255)
        self.un_10_4_grup_2_competitor_node_9.setObjectName(u"un_10_4_grup_2_competitor_node_9")
        self.un_10_4_grup_2_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_198.addWidget(self.un_10_4_grup_2_competitor_node_9)

        self.un_10_4_grup_2_competitor_node_10 = QTextEdit(self.frame_255)
        self.un_10_4_grup_2_competitor_node_10.setObjectName(u"un_10_4_grup_2_competitor_node_10")
        self.un_10_4_grup_2_competitor_node_10.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_198.addWidget(self.un_10_4_grup_2_competitor_node_10)


        self.verticalLayout_197.addWidget(self.frame_255)

        self.frame_256 = QFrame(self.frame_254)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setFrameShape(QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Raised)
        self.verticalLayout_199 = QVBoxLayout(self.frame_256)
        self.verticalLayout_199.setSpacing(0)
        self.verticalLayout_199.setObjectName(u"verticalLayout_199")
        self.verticalLayout_199.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_2_competitor_node_11 = QTextEdit(self.frame_256)
        self.un_10_4_grup_2_competitor_node_11.setObjectName(u"un_10_4_grup_2_competitor_node_11")
        self.un_10_4_grup_2_competitor_node_11.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_199.addWidget(self.un_10_4_grup_2_competitor_node_11)

        self.un_10_4_grup_2_competitor_node_12 = QTextEdit(self.frame_256)
        self.un_10_4_grup_2_competitor_node_12.setObjectName(u"un_10_4_grup_2_competitor_node_12")
        self.un_10_4_grup_2_competitor_node_12.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_199.addWidget(self.un_10_4_grup_2_competitor_node_12)


        self.verticalLayout_197.addWidget(self.frame_256)


        self.horizontalLayout_86.addWidget(self.frame_254)

        self.frame_257 = QFrame(self.under_4_g2)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setMinimumSize(QSize(25, 0))
        self.frame_257.setFrameShape(QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Raised)
        self.verticalLayout_200 = QVBoxLayout(self.frame_257)
        self.verticalLayout_200.setObjectName(u"verticalLayout_200")
        self.verticalLayout_200.setContentsMargins(0, -1, -1, -1)
        self.label_67 = QLabel(self.frame_257)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font1)
        self.label_67.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_200.addWidget(self.label_67)

        self.frame_258 = QFrame(self.frame_257)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setFrameShape(QFrame.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Raised)
        self.verticalLayout_201 = QVBoxLayout(self.frame_258)
        self.verticalLayout_201.setSpacing(0)
        self.verticalLayout_201.setObjectName(u"verticalLayout_201")
        self.verticalLayout_201.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_2_competitor_node_13 = QTextEdit(self.frame_258)
        self.un_10_4_grup_2_competitor_node_13.setObjectName(u"un_10_4_grup_2_competitor_node_13")
        self.un_10_4_grup_2_competitor_node_13.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_201.addWidget(self.un_10_4_grup_2_competitor_node_13)

        self.un_10_4_grup_2_competitor_node_14 = QTextEdit(self.frame_258)
        self.un_10_4_grup_2_competitor_node_14.setObjectName(u"un_10_4_grup_2_competitor_node_14")
        self.un_10_4_grup_2_competitor_node_14.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_201.addWidget(self.un_10_4_grup_2_competitor_node_14)


        self.verticalLayout_200.addWidget(self.frame_258)

        self.frame_259 = QFrame(self.frame_257)
        self.frame_259.setObjectName(u"frame_259")
        self.frame_259.setFrameShape(QFrame.StyledPanel)
        self.frame_259.setFrameShadow(QFrame.Raised)
        self.verticalLayout_202 = QVBoxLayout(self.frame_259)
        self.verticalLayout_202.setSpacing(0)
        self.verticalLayout_202.setObjectName(u"verticalLayout_202")
        self.verticalLayout_202.setContentsMargins(0, 0, 0, 0)
        self.un_10_4_grup_2_competitor_node_15 = QTextEdit(self.frame_259)
        self.un_10_4_grup_2_competitor_node_15.setObjectName(u"un_10_4_grup_2_competitor_node_15")
        self.un_10_4_grup_2_competitor_node_15.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_202.addWidget(self.un_10_4_grup_2_competitor_node_15)

        self.un_10_4_grup_2_competitor_node_16 = QTextEdit(self.frame_259)
        self.un_10_4_grup_2_competitor_node_16.setObjectName(u"un_10_4_grup_2_competitor_node_16")
        self.un_10_4_grup_2_competitor_node_16.setMaximumSize(QSize(16777215, 50))
        self.un_10_4_grup_2_competitor_node_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_4_grup_2_competitor_node_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_202.addWidget(self.un_10_4_grup_2_competitor_node_16)


        self.verticalLayout_200.addWidget(self.frame_259)


        self.horizontalLayout_86.addWidget(self.frame_257)

        self.Grup_II_Under10_G2.addWidget(self.under_4_g2)
        self.under_3_g2 = QWidget()
        self.under_3_g2.setObjectName(u"under_3_g2")
        self.horizontalLayout_88 = QHBoxLayout(self.under_3_g2)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.frame_260 = QFrame(self.under_3_g2)
        self.frame_260.setObjectName(u"frame_260")
        self.frame_260.setFrameShape(QFrame.StyledPanel)
        self.frame_260.setFrameShadow(QFrame.Raised)
        self.verticalLayout_203 = QVBoxLayout(self.frame_260)
        self.verticalLayout_203.setObjectName(u"verticalLayout_203")
        self.frame_261 = QFrame(self.frame_260)
        self.frame_261.setObjectName(u"frame_261")
        self.frame_261.setFrameShape(QFrame.StyledPanel)
        self.frame_261.setFrameShadow(QFrame.Raised)
        self.verticalLayout_204 = QVBoxLayout(self.frame_261)
        self.verticalLayout_204.setObjectName(u"verticalLayout_204")
        self.label_68 = QLabel(self.frame_261)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font1)

        self.verticalLayout_204.addWidget(self.label_68)


        self.verticalLayout_203.addWidget(self.frame_261)

        self.frame_262 = QFrame(self.frame_260)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setFrameShape(QFrame.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_262)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.frame_263 = QFrame(self.frame_262)
        self.frame_263.setObjectName(u"frame_263")
        self.frame_263.setFrameShape(QFrame.StyledPanel)
        self.frame_263.setFrameShadow(QFrame.Raised)
        self.verticalLayout_205 = QVBoxLayout(self.frame_263)
        self.verticalLayout_205.setObjectName(u"verticalLayout_205")
        self.un_10_3_grup_2_competitor_node_1 = QTextEdit(self.frame_263)
        self.un_10_3_grup_2_competitor_node_1.setObjectName(u"un_10_3_grup_2_competitor_node_1")
        self.un_10_3_grup_2_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_205.addWidget(self.un_10_3_grup_2_competitor_node_1)

        self.un_10_3_grup_2_competitor_node_2 = QTextEdit(self.frame_263)
        self.un_10_3_grup_2_competitor_node_2.setObjectName(u"un_10_3_grup_2_competitor_node_2")
        self.un_10_3_grup_2_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_205.addWidget(self.un_10_3_grup_2_competitor_node_2)

        self.un_10_3_grup_2_competitor_node_3 = QTextEdit(self.frame_263)
        self.un_10_3_grup_2_competitor_node_3.setObjectName(u"un_10_3_grup_2_competitor_node_3")
        self.un_10_3_grup_2_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_205.addWidget(self.un_10_3_grup_2_competitor_node_3)


        self.horizontalLayout_89.addWidget(self.frame_263)

        self.frame_264 = QFrame(self.frame_262)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setMaximumSize(QSize(50, 16777215))
        self.frame_264.setFrameShape(QFrame.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Raised)
        self.verticalLayout_206 = QVBoxLayout(self.frame_264)
        self.verticalLayout_206.setObjectName(u"verticalLayout_206")
        self.un_10_3_grup_2_point_node_1 = QTextEdit(self.frame_264)
        self.un_10_3_grup_2_point_node_1.setObjectName(u"un_10_3_grup_2_point_node_1")
        self.un_10_3_grup_2_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_206.addWidget(self.un_10_3_grup_2_point_node_1)

        self.un_10_3_grup_2_point_node_2 = QTextEdit(self.frame_264)
        self.un_10_3_grup_2_point_node_2.setObjectName(u"un_10_3_grup_2_point_node_2")
        self.un_10_3_grup_2_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_206.addWidget(self.un_10_3_grup_2_point_node_2)

        self.un_10_3_grup_2_point_node_3 = QTextEdit(self.frame_264)
        self.un_10_3_grup_2_point_node_3.setObjectName(u"un_10_3_grup_2_point_node_3")
        self.un_10_3_grup_2_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_206.addWidget(self.un_10_3_grup_2_point_node_3)


        self.horizontalLayout_89.addWidget(self.frame_264)


        self.verticalLayout_203.addWidget(self.frame_262)


        self.horizontalLayout_88.addWidget(self.frame_260)

        self.frame_265 = QFrame(self.under_3_g2)
        self.frame_265.setObjectName(u"frame_265")
        self.frame_265.setMinimumSize(QSize(25, 0))
        self.frame_265.setFrameShape(QFrame.StyledPanel)
        self.frame_265.setFrameShadow(QFrame.Raised)
        self.verticalLayout_207 = QVBoxLayout(self.frame_265)
        self.verticalLayout_207.setObjectName(u"verticalLayout_207")
        self.label_69 = QLabel(self.frame_265)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font1)
        self.label_69.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_207.addWidget(self.label_69)

        self.frame_266 = QFrame(self.frame_265)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setEnabled(True)
        self.frame_266.setFrameShape(QFrame.NoFrame)
        self.frame_266.setFrameShadow(QFrame.Raised)
        self._11 = QVBoxLayout(self.frame_266)
        self._11.setSpacing(0)
        self._11.setObjectName(u"_11")
        self._11.setContentsMargins(0, 0, 0, 0)
        self.un_10_3_grup_2_competitor_node_4 = QTextEdit(self.frame_266)
        self.un_10_3_grup_2_competitor_node_4.setObjectName(u"un_10_3_grup_2_competitor_node_4")
        self.un_10_3_grup_2_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._11.addWidget(self.un_10_3_grup_2_competitor_node_4)

        self.un_10_3_grup_2_competitor_node_5 = QTextEdit(self.frame_266)
        self.un_10_3_grup_2_competitor_node_5.setObjectName(u"un_10_3_grup_2_competitor_node_5")
        self.un_10_3_grup_2_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._11.addWidget(self.un_10_3_grup_2_competitor_node_5)


        self.verticalLayout_207.addWidget(self.frame_266)


        self.horizontalLayout_88.addWidget(self.frame_265)

        self.frame_267 = QFrame(self.under_3_g2)
        self.frame_267.setObjectName(u"frame_267")
        self.frame_267.setMinimumSize(QSize(25, 0))
        self.frame_267.setFrameShape(QFrame.StyledPanel)
        self.frame_267.setFrameShadow(QFrame.Raised)
        self.verticalLayout_208 = QVBoxLayout(self.frame_267)
        self.verticalLayout_208.setObjectName(u"verticalLayout_208")
        self.label_70 = QLabel(self.frame_267)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font1)
        self.label_70.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_208.addWidget(self.label_70)

        self.frame_268 = QFrame(self.frame_267)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setFrameShape(QFrame.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Raised)
        self.verticalLayout_209 = QVBoxLayout(self.frame_268)
        self.verticalLayout_209.setSpacing(0)
        self.verticalLayout_209.setObjectName(u"verticalLayout_209")
        self.verticalLayout_209.setContentsMargins(0, 0, 0, 0)
        self.un_10_3_grup_2_competitor_node_6 = QTextEdit(self.frame_268)
        self.un_10_3_grup_2_competitor_node_6.setObjectName(u"un_10_3_grup_2_competitor_node_6")
        self.un_10_3_grup_2_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_209.addWidget(self.un_10_3_grup_2_competitor_node_6)

        self.un_10_3_grup_2_competitor_node_7 = QTextEdit(self.frame_268)
        self.un_10_3_grup_2_competitor_node_7.setObjectName(u"un_10_3_grup_2_competitor_node_7")
        self.un_10_3_grup_2_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_209.addWidget(self.un_10_3_grup_2_competitor_node_7)


        self.verticalLayout_208.addWidget(self.frame_268)


        self.horizontalLayout_88.addWidget(self.frame_267)

        self.frame_269 = QFrame(self.under_3_g2)
        self.frame_269.setObjectName(u"frame_269")
        self.frame_269.setMinimumSize(QSize(25, 0))
        self.frame_269.setFrameShape(QFrame.StyledPanel)
        self.frame_269.setFrameShadow(QFrame.Raised)
        self.verticalLayout_210 = QVBoxLayout(self.frame_269)
        self.verticalLayout_210.setObjectName(u"verticalLayout_210")
        self.verticalLayout_210.setContentsMargins(0, -1, -1, -1)
        self.label_71 = QLabel(self.frame_269)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font1)
        self.label_71.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_210.addWidget(self.label_71)

        self.frame_270 = QFrame(self.frame_269)
        self.frame_270.setObjectName(u"frame_270")
        self.frame_270.setFrameShape(QFrame.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Raised)
        self.verticalLayout_211 = QVBoxLayout(self.frame_270)
        self.verticalLayout_211.setSpacing(0)
        self.verticalLayout_211.setObjectName(u"verticalLayout_211")
        self.verticalLayout_211.setContentsMargins(0, 0, 0, 0)
        self.un_10_3_grup_2_competitor_node_8 = QTextEdit(self.frame_270)
        self.un_10_3_grup_2_competitor_node_8.setObjectName(u"un_10_3_grup_2_competitor_node_8")
        self.un_10_3_grup_2_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_211.addWidget(self.un_10_3_grup_2_competitor_node_8)

        self.un_10_3_grup_2_competitor_node_9 = QTextEdit(self.frame_270)
        self.un_10_3_grup_2_competitor_node_9.setObjectName(u"un_10_3_grup_2_competitor_node_9")
        self.un_10_3_grup_2_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_10_3_grup_2_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_3_grup_2_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_211.addWidget(self.un_10_3_grup_2_competitor_node_9)


        self.verticalLayout_210.addWidget(self.frame_270)


        self.horizontalLayout_88.addWidget(self.frame_269)

        self.Grup_II_Under10_G2.addWidget(self.under_3_g2)

        self.verticalLayout_222.addWidget(self.Grup_II_Under10_G2)

        self.match_10.addWidget(self.Grup_II_Under10)
        self.Finals_Under10 = QWidget()
        self.Finals_Under10.setObjectName(u"Finals_Under10")
        self.verticalLayout_223 = QVBoxLayout(self.Finals_Under10)
        self.verticalLayout_223.setObjectName(u"verticalLayout_223")
        self.frame_187 = QFrame(self.Finals_Under10)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.verticalLayout_142 = QVBoxLayout(self.frame_187)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.frame_188 = QFrame(self.frame_187)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.frame_188)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.frame_189 = QFrame(self.frame_188)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_37 = QLabel(self.frame_189)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font1)

        self.horizontalLayout_76.addWidget(self.label_37, 0, Qt.AlignHCenter)


        self.verticalLayout_143.addWidget(self.frame_189)

        self.un_10_final_competitor_node_3 = QTextEdit(self.frame_188)
        self.un_10_final_competitor_node_3.setObjectName(u"un_10_final_competitor_node_3")
        self.un_10_final_competitor_node_3.setMaximumSize(QSize(270, 50))

        self.verticalLayout_143.addWidget(self.un_10_final_competitor_node_3, 0, Qt.AlignHCenter)

        self.frame_190 = QFrame(self.frame_188)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_190)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.un_10_final_competitor_node_1 = QTextEdit(self.frame_190)
        self.un_10_final_competitor_node_1.setObjectName(u"un_10_final_competitor_node_1")
        self.un_10_final_competitor_node_1.setMaximumSize(QSize(270, 50))
        self.un_10_final_competitor_node_1.setStyleSheet(u"")
        self.un_10_final_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_final_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_final_competitor_node_1.setUndoRedoEnabled(False)

        self.horizontalLayout_77.addWidget(self.un_10_final_competitor_node_1, 0, Qt.AlignHCenter)

        self.un_10_final_competitor_node_2 = QTextEdit(self.frame_190)
        self.un_10_final_competitor_node_2.setObjectName(u"un_10_final_competitor_node_2")
        self.un_10_final_competitor_node_2.setMaximumSize(QSize(270, 50))
        self.un_10_final_competitor_node_2.setStyleSheet(u"")
        self.un_10_final_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_final_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_final_competitor_node_2.setUndoRedoEnabled(False)

        self.horizontalLayout_77.addWidget(self.un_10_final_competitor_node_2)


        self.verticalLayout_143.addWidget(self.frame_190)


        self.verticalLayout_142.addWidget(self.frame_188, 0, Qt.AlignHCenter)

        self.frame_191 = QFrame(self.frame_187)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_191)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.frame_192 = QFrame(self.frame_191)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.verticalLayout_144 = QVBoxLayout(self.frame_192)
        self.verticalLayout_144.setObjectName(u"verticalLayout_144")
        self.frame_193 = QFrame(self.frame_192)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_193)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_38 = QLabel(self.frame_193)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.horizontalLayout_79.addWidget(self.label_38, 0, Qt.AlignHCenter)


        self.verticalLayout_144.addWidget(self.frame_193)

        self.un_10_half_final_competitor_node_5 = QTextEdit(self.frame_192)
        self.un_10_half_final_competitor_node_5.setObjectName(u"un_10_half_final_competitor_node_5")
        self.un_10_half_final_competitor_node_5.setMaximumSize(QSize(270, 50))

        self.verticalLayout_144.addWidget(self.un_10_half_final_competitor_node_5, 0, Qt.AlignHCenter)

        self.frame_194 = QFrame(self.frame_192)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_194)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.un_10_half_final_competitor_node_1 = QTextEdit(self.frame_194)
        self.un_10_half_final_competitor_node_1.setObjectName(u"un_10_half_final_competitor_node_1")
        self.un_10_half_final_competitor_node_1.setMaximumSize(QSize(270, 50))
        self.un_10_half_final_competitor_node_1.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.un_10_half_final_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_1.setUndoRedoEnabled(False)

        self.horizontalLayout_80.addWidget(self.un_10_half_final_competitor_node_1)

        self.un_10_half_final_competitor_node_2 = QTextEdit(self.frame_194)
        self.un_10_half_final_competitor_node_2.setObjectName(u"un_10_half_final_competitor_node_2")
        self.un_10_half_final_competitor_node_2.setMaximumSize(QSize(270, 50))
        self.un_10_half_final_competitor_node_2.setStyleSheet(u"")
        self.un_10_half_final_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_2.setUndoRedoEnabled(False)

        self.horizontalLayout_80.addWidget(self.un_10_half_final_competitor_node_2)


        self.verticalLayout_144.addWidget(self.frame_194)


        self.horizontalLayout_78.addWidget(self.frame_192)

        self.frame_195 = QFrame(self.frame_191)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.verticalLayout_145 = QVBoxLayout(self.frame_195)
        self.verticalLayout_145.setObjectName(u"verticalLayout_145")
        self.frame_196 = QFrame(self.frame_195)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_196)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.label_39 = QLabel(self.frame_196)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.horizontalLayout_81.addWidget(self.label_39, 0, Qt.AlignHCenter)


        self.verticalLayout_145.addWidget(self.frame_196)

        self.un_10_half_final_competitor_node_6 = QTextEdit(self.frame_195)
        self.un_10_half_final_competitor_node_6.setObjectName(u"un_10_half_final_competitor_node_6")
        self.un_10_half_final_competitor_node_6.setMaximumSize(QSize(270, 50))

        self.verticalLayout_145.addWidget(self.un_10_half_final_competitor_node_6, 0, Qt.AlignHCenter)

        self.frame_197 = QFrame(self.frame_195)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.un_10_half_final_competitor_node_3 = QTextEdit(self.frame_197)
        self.un_10_half_final_competitor_node_3.setObjectName(u"un_10_half_final_competitor_node_3")
        self.un_10_half_final_competitor_node_3.setMaximumSize(QSize(270, 50))
        self.un_10_half_final_competitor_node_3.setStyleSheet(u"")
        self.un_10_half_final_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_3.setUndoRedoEnabled(False)

        self.horizontalLayout_82.addWidget(self.un_10_half_final_competitor_node_3)

        self.un_10_half_final_competitor_node_4 = QTextEdit(self.frame_197)
        self.un_10_half_final_competitor_node_4.setObjectName(u"un_10_half_final_competitor_node_4")
        self.un_10_half_final_competitor_node_4.setMaximumSize(QSize(270, 50))
        self.un_10_half_final_competitor_node_4.setStyleSheet(u"")
        self.un_10_half_final_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_10_half_final_competitor_node_4.setUndoRedoEnabled(False)

        self.horizontalLayout_82.addWidget(self.un_10_half_final_competitor_node_4)


        self.verticalLayout_145.addWidget(self.frame_197)


        self.horizontalLayout_78.addWidget(self.frame_195)


        self.verticalLayout_142.addWidget(self.frame_191)


        self.verticalLayout_223.addWidget(self.frame_187)

        self.match_10.addWidget(self.Finals_Under10)

        self.verticalLayout_149.addWidget(self.match_10)

        self.AllMatchesWraper.addWidget(self.MatchUnder10)
        self.MatchUnder5 = QWidget()
        self.MatchUnder5.setObjectName(u"MatchUnder5")
        self.horizontalLayout_31 = QHBoxLayout(self.MatchUnder5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.match_5 = QStackedWidget(self.MatchUnder5)
        self.match_5.setObjectName(u"match_5")
        self.match_5.setStyleSheet(u"")
        self.under_5 = QWidget()
        self.under_5.setObjectName(u"under_5")
        self.horizontalLayout_36 = QHBoxLayout(self.under_5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.frame_57 = QFrame(self.under_5)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_57)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.frame_61 = QFrame(self.frame_57)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_61)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_3 = QLabel(self.frame_61)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_53.addWidget(self.label_3)


        self.verticalLayout_34.addWidget(self.frame_61)

        self.frame_64 = QFrame(self.frame_57)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.frame_66 = QFrame(self.frame_64)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_66)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.un_5_competitor_node_1 = QTextEdit(self.frame_66)
        self.un_5_competitor_node_1.setObjectName(u"un_5_competitor_node_1")
        self.un_5_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_51.addWidget(self.un_5_competitor_node_1)

        self.un_5_competitor_node_2 = QTextEdit(self.frame_66)
        self.un_5_competitor_node_2.setObjectName(u"un_5_competitor_node_2")
        self.un_5_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_51.addWidget(self.un_5_competitor_node_2)

        self.un_5_competitor_node_3 = QTextEdit(self.frame_66)
        self.un_5_competitor_node_3.setObjectName(u"un_5_competitor_node_3")
        self.un_5_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_51.addWidget(self.un_5_competitor_node_3)

        self.un_5_competitor_node_4 = QTextEdit(self.frame_66)
        self.un_5_competitor_node_4.setObjectName(u"un_5_competitor_node_4")
        self.un_5_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_51.addWidget(self.un_5_competitor_node_4)

        self.un_5_competitor_node_5 = QTextEdit(self.frame_66)
        self.un_5_competitor_node_5.setObjectName(u"un_5_competitor_node_5")
        self.un_5_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_51.addWidget(self.un_5_competitor_node_5)


        self.horizontalLayout_39.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_64)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMaximumSize(QSize(50, 16777215))
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_67)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.un_5_point_node_1 = QTextEdit(self.frame_67)
        self.un_5_point_node_1.setObjectName(u"un_5_point_node_1")
        self.un_5_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_5_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_52.addWidget(self.un_5_point_node_1)

        self.un_5_point_node_2 = QTextEdit(self.frame_67)
        self.un_5_point_node_2.setObjectName(u"un_5_point_node_2")
        self.un_5_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_5_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_52.addWidget(self.un_5_point_node_2)

        self.un_5_point_node_3 = QTextEdit(self.frame_67)
        self.un_5_point_node_3.setObjectName(u"un_5_point_node_3")
        self.un_5_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_5_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_52.addWidget(self.un_5_point_node_3)

        self.un_5_point_node_4 = QTextEdit(self.frame_67)
        self.un_5_point_node_4.setObjectName(u"un_5_point_node_4")
        self.un_5_point_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_5_point_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_point_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_52.addWidget(self.un_5_point_node_4)

        self.un_5_point_node_5 = QTextEdit(self.frame_67)
        self.un_5_point_node_5.setObjectName(u"un_5_point_node_5")
        self.un_5_point_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_5_point_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_point_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_52.addWidget(self.un_5_point_node_5)


        self.horizontalLayout_39.addWidget(self.frame_67)


        self.verticalLayout_34.addWidget(self.frame_64)


        self.horizontalLayout_36.addWidget(self.frame_57)

        self.frame_56 = QFrame(self.under_5)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(25, 0))
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_56)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_4 = QLabel(self.frame_56)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_37.addWidget(self.label_4)

        self.frame_71 = QFrame(self.frame_56)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setEnabled(True)
        self.frame_71.setFrameShape(QFrame.NoFrame)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.frame_71)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_6 = QTextEdit(self.frame_71)
        self.un_5_competitor_node_6.setObjectName(u"un_5_competitor_node_6")
        self.un_5_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.vboxLayout.addWidget(self.un_5_competitor_node_6)

        self.un_5_competitor_node_7 = QTextEdit(self.frame_71)
        self.un_5_competitor_node_7.setObjectName(u"un_5_competitor_node_7")
        self.un_5_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.vboxLayout.addWidget(self.un_5_competitor_node_7)


        self.verticalLayout_37.addWidget(self.frame_71)

        self.frame_69 = QFrame(self.frame_56)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_69)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_8 = QTextEdit(self.frame_69)
        self.un_5_competitor_node_8.setObjectName(u"un_5_competitor_node_8")
        self.un_5_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_55.addWidget(self.un_5_competitor_node_8)

        self.un_5_competitor_node_9 = QTextEdit(self.frame_69)
        self.un_5_competitor_node_9.setObjectName(u"un_5_competitor_node_9")
        self.un_5_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_55.addWidget(self.un_5_competitor_node_9)


        self.verticalLayout_37.addWidget(self.frame_69)


        self.horizontalLayout_36.addWidget(self.frame_56)

        self.frame_55 = QFrame(self.under_5)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(25, 0))
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_55)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_8 = QLabel(self.frame_55)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_38.addWidget(self.label_8)

        self.frame_73 = QFrame(self.frame_55)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_73)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_10 = QTextEdit(self.frame_73)
        self.un_5_competitor_node_10.setObjectName(u"un_5_competitor_node_10")
        self.un_5_competitor_node_10.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_57.addWidget(self.un_5_competitor_node_10)

        self.un_5_competitor_node_11 = QTextEdit(self.frame_73)
        self.un_5_competitor_node_11.setObjectName(u"un_5_competitor_node_11")
        self.un_5_competitor_node_11.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_57.addWidget(self.un_5_competitor_node_11)


        self.verticalLayout_38.addWidget(self.frame_73)

        self.frame_70 = QFrame(self.frame_55)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_70)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_12 = QTextEdit(self.frame_70)
        self.un_5_competitor_node_12.setObjectName(u"un_5_competitor_node_12")
        self.un_5_competitor_node_12.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_62.addWidget(self.un_5_competitor_node_12)

        self.un_5_competitor_node_13 = QTextEdit(self.frame_70)
        self.un_5_competitor_node_13.setObjectName(u"un_5_competitor_node_13")
        self.un_5_competitor_node_13.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_62.addWidget(self.un_5_competitor_node_13)


        self.verticalLayout_38.addWidget(self.frame_70)


        self.horizontalLayout_36.addWidget(self.frame_55)

        self.frame_52 = QFrame(self.under_5)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(25, 0))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_52)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, -1, -1, -1)
        self.label_9 = QLabel(self.frame_52)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_39.addWidget(self.label_9)

        self.frame_75 = QFrame(self.frame_52)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_75)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_14 = QTextEdit(self.frame_75)
        self.un_5_competitor_node_14.setObjectName(u"un_5_competitor_node_14")
        self.un_5_competitor_node_14.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_58.addWidget(self.un_5_competitor_node_14)

        self.un_5_competitor_node_15 = QTextEdit(self.frame_75)
        self.un_5_competitor_node_15.setObjectName(u"un_5_competitor_node_15")
        self.un_5_competitor_node_15.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_58.addWidget(self.un_5_competitor_node_15)


        self.verticalLayout_39.addWidget(self.frame_75)

        self.frame_72 = QFrame(self.frame_52)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_72)
        self.verticalLayout_63.setSpacing(0)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_16 = QTextEdit(self.frame_72)
        self.un_5_competitor_node_16.setObjectName(u"un_5_competitor_node_16")
        self.un_5_competitor_node_16.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_63.addWidget(self.un_5_competitor_node_16)

        self.un_5_competitor_node_17 = QTextEdit(self.frame_72)
        self.un_5_competitor_node_17.setObjectName(u"un_5_competitor_node_17")
        self.un_5_competitor_node_17.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_17.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_17.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_63.addWidget(self.un_5_competitor_node_17)


        self.verticalLayout_39.addWidget(self.frame_72)


        self.horizontalLayout_36.addWidget(self.frame_52)

        self.frame_49 = QFrame(self.under_5)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(25, 0))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_49)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_10 = QLabel(self.frame_49)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_40.addWidget(self.label_10)

        self.frame_76 = QFrame(self.frame_49)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_76)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_18 = QTextEdit(self.frame_76)
        self.un_5_competitor_node_18.setObjectName(u"un_5_competitor_node_18")
        self.un_5_competitor_node_18.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_18.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_18.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_59.addWidget(self.un_5_competitor_node_18)

        self.un_5_competitor_node_19 = QTextEdit(self.frame_76)
        self.un_5_competitor_node_19.setObjectName(u"un_5_competitor_node_19")
        self.un_5_competitor_node_19.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_19.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_19.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_59.addWidget(self.un_5_competitor_node_19)


        self.verticalLayout_40.addWidget(self.frame_76)

        self.frame_74 = QFrame(self.frame_49)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_74)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_20 = QTextEdit(self.frame_74)
        self.un_5_competitor_node_20.setObjectName(u"un_5_competitor_node_20")
        self.un_5_competitor_node_20.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_20.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_20.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_60.addWidget(self.un_5_competitor_node_20)

        self.un_5_competitor_node_21 = QTextEdit(self.frame_74)
        self.un_5_competitor_node_21.setObjectName(u"un_5_competitor_node_21")
        self.un_5_competitor_node_21.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_21.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_21.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_60.addWidget(self.un_5_competitor_node_21)


        self.verticalLayout_40.addWidget(self.frame_74)


        self.horizontalLayout_36.addWidget(self.frame_49)

        self.frame_2 = QFrame(self.under_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(50, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_2)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_50.addWidget(self.label_17)

        self.frame_78 = QFrame(self.frame_2)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_78)
        self.verticalLayout_64.setSpacing(0)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_22 = QTextEdit(self.frame_78)
        self.un_5_competitor_node_22.setObjectName(u"un_5_competitor_node_22")
        self.un_5_competitor_node_22.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_22.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_22.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_64.addWidget(self.un_5_competitor_node_22)

        self.un_5_competitor_node_23 = QTextEdit(self.frame_78)
        self.un_5_competitor_node_23.setObjectName(u"un_5_competitor_node_23")
        self.un_5_competitor_node_23.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_23.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_23.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_64.addWidget(self.un_5_competitor_node_23)


        self.verticalLayout_50.addWidget(self.frame_78)

        self.frame_77 = QFrame(self.frame_2)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_77)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.un_5_competitor_node_24 = QTextEdit(self.frame_77)
        self.un_5_competitor_node_24.setObjectName(u"un_5_competitor_node_24")
        self.un_5_competitor_node_24.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_24.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_24.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_61.addWidget(self.un_5_competitor_node_24)

        self.un_5_competitor_node_25 = QTextEdit(self.frame_77)
        self.un_5_competitor_node_25.setObjectName(u"un_5_competitor_node_25")
        self.un_5_competitor_node_25.setMaximumSize(QSize(16777215, 50))
        self.un_5_competitor_node_25.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_5_competitor_node_25.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_61.addWidget(self.un_5_competitor_node_25)


        self.verticalLayout_50.addWidget(self.frame_77)


        self.horizontalLayout_36.addWidget(self.frame_2)

        self.match_5.addWidget(self.under_5)
        self.under_4 = QWidget()
        self.under_4.setObjectName(u"under_4")
        self.horizontalLayout_27 = QHBoxLayout(self.under_4)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.frame_90 = QFrame(self.under_4)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_90)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.frame_91 = QFrame(self.frame_90)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_91)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.label_20 = QLabel(self.frame_91)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.verticalLayout_73.addWidget(self.label_20)


        self.verticalLayout_49.addWidget(self.frame_91)

        self.frame_92 = QFrame(self.frame_90)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_93)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.un_4_competitor_node_1 = QTextEdit(self.frame_93)
        self.un_4_competitor_node_1.setObjectName(u"un_4_competitor_node_1")
        self.un_4_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_74.addWidget(self.un_4_competitor_node_1)

        self.un_4_competitor_node_2 = QTextEdit(self.frame_93)
        self.un_4_competitor_node_2.setObjectName(u"un_4_competitor_node_2")
        self.un_4_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_74.addWidget(self.un_4_competitor_node_2)

        self.un_4_competitor_node_3 = QTextEdit(self.frame_93)
        self.un_4_competitor_node_3.setObjectName(u"un_4_competitor_node_3")
        self.un_4_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_74.addWidget(self.un_4_competitor_node_3)

        self.un_4_competitor_node_4 = QTextEdit(self.frame_93)
        self.un_4_competitor_node_4.setObjectName(u"un_4_competitor_node_4")
        self.un_4_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_74.addWidget(self.un_4_competitor_node_4)


        self.horizontalLayout_40.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMaximumSize(QSize(50, 16777215))
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_94)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.un_4_point_node_1 = QTextEdit(self.frame_94)
        self.un_4_point_node_1.setObjectName(u"un_4_point_node_1")
        self.un_4_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_4_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_75.addWidget(self.un_4_point_node_1)

        self.un_4_point_node_2 = QTextEdit(self.frame_94)
        self.un_4_point_node_2.setObjectName(u"un_4_point_node_2")
        self.un_4_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_4_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_75.addWidget(self.un_4_point_node_2)

        self.un_4_point_node_3 = QTextEdit(self.frame_94)
        self.un_4_point_node_3.setObjectName(u"un_4_point_node_3")
        self.un_4_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_4_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_75.addWidget(self.un_4_point_node_3)

        self.un_4_point_node_4 = QTextEdit(self.frame_94)
        self.un_4_point_node_4.setObjectName(u"un_4_point_node_4")
        self.un_4_point_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_4_point_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_point_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_75.addWidget(self.un_4_point_node_4)


        self.horizontalLayout_40.addWidget(self.frame_94)


        self.verticalLayout_49.addWidget(self.frame_92)


        self.horizontalLayout_27.addWidget(self.frame_90)

        self.frame_63 = QFrame(self.under_4)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(25, 0))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_63)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_12 = QLabel(self.frame_63)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_45.addWidget(self.label_12)

        self.frame_81 = QFrame(self.frame_63)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setEnabled(True)
        self.frame_81.setFrameShape(QFrame.NoFrame)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self._2 = QVBoxLayout(self.frame_81)
        self._2.setSpacing(0)
        self._2.setObjectName(u"_2")
        self._2.setContentsMargins(0, 0, 0, 0)
        self.un_4_competitor_node_5 = QTextEdit(self.frame_81)
        self.un_4_competitor_node_5.setObjectName(u"un_4_competitor_node_5")
        self.un_4_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._2.addWidget(self.un_4_competitor_node_5)

        self.un_4_competitor_node_6 = QTextEdit(self.frame_81)
        self.un_4_competitor_node_6.setObjectName(u"un_4_competitor_node_6")
        self.un_4_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._2.addWidget(self.un_4_competitor_node_6)


        self.verticalLayout_45.addWidget(self.frame_81)

        self.frame_82 = QFrame(self.frame_63)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_82)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.un_4_competitor_node_7 = QTextEdit(self.frame_82)
        self.un_4_competitor_node_7.setObjectName(u"un_4_competitor_node_7")
        self.un_4_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_56.addWidget(self.un_4_competitor_node_7)

        self.un_4_competitor_node_8 = QTextEdit(self.frame_82)
        self.un_4_competitor_node_8.setObjectName(u"un_4_competitor_node_8")
        self.un_4_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_56.addWidget(self.un_4_competitor_node_8)


        self.verticalLayout_45.addWidget(self.frame_82)


        self.horizontalLayout_27.addWidget(self.frame_63)

        self.frame_68 = QFrame(self.under_4)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(25, 0))
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_68)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_18 = QLabel(self.frame_68)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)
        self.label_18.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_48.addWidget(self.label_18)

        self.frame_85 = QFrame(self.frame_68)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_85)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.un_4_competitor_node_9 = QTextEdit(self.frame_85)
        self.un_4_competitor_node_9.setObjectName(u"un_4_competitor_node_9")
        self.un_4_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_69.addWidget(self.un_4_competitor_node_9)

        self.un_4_competitor_node_10 = QTextEdit(self.frame_85)
        self.un_4_competitor_node_10.setObjectName(u"un_4_competitor_node_10")
        self.un_4_competitor_node_10.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_10.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_10.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_69.addWidget(self.un_4_competitor_node_10)


        self.verticalLayout_48.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_68)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_86)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.un_4_competitor_node_11 = QTextEdit(self.frame_86)
        self.un_4_competitor_node_11.setObjectName(u"un_4_competitor_node_11")
        self.un_4_competitor_node_11.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_11.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_70.addWidget(self.un_4_competitor_node_11)

        self.un_4_competitor_node_12 = QTextEdit(self.frame_86)
        self.un_4_competitor_node_12.setObjectName(u"un_4_competitor_node_12")
        self.un_4_competitor_node_12.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_70.addWidget(self.un_4_competitor_node_12)


        self.verticalLayout_48.addWidget(self.frame_86)


        self.horizontalLayout_27.addWidget(self.frame_68)

        self.frame_65 = QFrame(self.under_4)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(25, 0))
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_65)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, -1, -1, -1)
        self.label_13 = QLabel(self.frame_65)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_47.addWidget(self.label_13)

        self.frame_83 = QFrame(self.frame_65)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_83)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.un_4_competitor_node_13 = QTextEdit(self.frame_83)
        self.un_4_competitor_node_13.setObjectName(u"un_4_competitor_node_13")
        self.un_4_competitor_node_13.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_67.addWidget(self.un_4_competitor_node_13)

        self.un_4_competitor_node_14 = QTextEdit(self.frame_83)
        self.un_4_competitor_node_14.setObjectName(u"un_4_competitor_node_14")
        self.un_4_competitor_node_14.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_67.addWidget(self.un_4_competitor_node_14)


        self.verticalLayout_47.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.frame_65)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_84)
        self.verticalLayout_68.setSpacing(0)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.verticalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.un_4_competitor_node_15 = QTextEdit(self.frame_84)
        self.un_4_competitor_node_15.setObjectName(u"un_4_competitor_node_15")
        self.un_4_competitor_node_15.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_68.addWidget(self.un_4_competitor_node_15)

        self.un_4_competitor_node_16 = QTextEdit(self.frame_84)
        self.un_4_competitor_node_16.setObjectName(u"un_4_competitor_node_16")
        self.un_4_competitor_node_16.setMaximumSize(QSize(16777215, 50))
        self.un_4_competitor_node_16.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_4_competitor_node_16.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_68.addWidget(self.un_4_competitor_node_16)


        self.verticalLayout_47.addWidget(self.frame_84)


        self.horizontalLayout_27.addWidget(self.frame_65)

        self.match_5.addWidget(self.under_4)
        self.under_3 = QWidget()
        self.under_3.setObjectName(u"under_3")
        self.horizontalLayout_37 = QHBoxLayout(self.under_3)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.frame_99 = QFrame(self.under_3)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_99)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.frame_100 = QFrame(self.frame_99)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_100)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_21 = QLabel(self.frame_100)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.verticalLayout_79.addWidget(self.label_21)


        self.verticalLayout_78.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_99)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.frame_102 = QFrame(self.frame_101)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_102)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.un_3_competitor_node_1 = QTextEdit(self.frame_102)
        self.un_3_competitor_node_1.setObjectName(u"un_3_competitor_node_1")
        self.un_3_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_80.addWidget(self.un_3_competitor_node_1)

        self.un_3_competitor_node_2 = QTextEdit(self.frame_102)
        self.un_3_competitor_node_2.setObjectName(u"un_3_competitor_node_2")
        self.un_3_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_80.addWidget(self.un_3_competitor_node_2)

        self.un_3_competitor_node_3 = QTextEdit(self.frame_102)
        self.un_3_competitor_node_3.setObjectName(u"un_3_competitor_node_3")
        self.un_3_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_80.addWidget(self.un_3_competitor_node_3)


        self.horizontalLayout_41.addWidget(self.frame_102)

        self.frame_103 = QFrame(self.frame_101)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setMaximumSize(QSize(50, 16777215))
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_103)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.un_3_point_node_1 = QTextEdit(self.frame_103)
        self.un_3_point_node_1.setObjectName(u"un_3_point_node_1")
        self.un_3_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_3_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_81.addWidget(self.un_3_point_node_1)

        self.un_3_point_node_2 = QTextEdit(self.frame_103)
        self.un_3_point_node_2.setObjectName(u"un_3_point_node_2")
        self.un_3_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_3_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_81.addWidget(self.un_3_point_node_2)

        self.un_3_point_node_3 = QTextEdit(self.frame_103)
        self.un_3_point_node_3.setObjectName(u"un_3_point_node_3")
        self.un_3_point_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_3_point_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_point_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_81.addWidget(self.un_3_point_node_3)


        self.horizontalLayout_41.addWidget(self.frame_103)


        self.verticalLayout_78.addWidget(self.frame_101)


        self.horizontalLayout_37.addWidget(self.frame_99)

        self.frame_96 = QFrame(self.under_3)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setMinimumSize(QSize(25, 0))
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_96)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_15 = QLabel(self.frame_96)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_46.addWidget(self.label_15)

        self.frame_97 = QFrame(self.frame_96)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setEnabled(True)
        self.frame_97.setFrameShape(QFrame.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self._3 = QVBoxLayout(self.frame_97)
        self._3.setSpacing(0)
        self._3.setObjectName(u"_3")
        self._3.setContentsMargins(0, 0, 0, 0)
        self.un_3_competitor_node_4 = QTextEdit(self.frame_97)
        self.un_3_competitor_node_4.setObjectName(u"un_3_competitor_node_4")
        self.un_3_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._3.addWidget(self.un_3_competitor_node_4)

        self.un_3_competitor_node_5 = QTextEdit(self.frame_97)
        self.un_3_competitor_node_5.setObjectName(u"un_3_competitor_node_5")
        self.un_3_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._3.addWidget(self.un_3_competitor_node_5)


        self.verticalLayout_46.addWidget(self.frame_97)


        self.horizontalLayout_37.addWidget(self.frame_96)

        self.frame_80 = QFrame(self.under_3)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(25, 0))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_80)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_19 = QLabel(self.frame_80)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_65.addWidget(self.label_19)

        self.frame_89 = QFrame(self.frame_80)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_89)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.un_3_competitor_node_6 = QTextEdit(self.frame_89)
        self.un_3_competitor_node_6.setObjectName(u"un_3_competitor_node_6")
        self.un_3_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_76.addWidget(self.un_3_competitor_node_6)

        self.un_3_competitor_node_7 = QTextEdit(self.frame_89)
        self.un_3_competitor_node_7.setObjectName(u"un_3_competitor_node_7")
        self.un_3_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_76.addWidget(self.un_3_competitor_node_7)


        self.verticalLayout_65.addWidget(self.frame_89)


        self.horizontalLayout_37.addWidget(self.frame_80)

        self.frame_79 = QFrame(self.under_3)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(25, 0))
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_79)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, -1, -1, -1)
        self.label_14 = QLabel(self.frame_79)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_54.addWidget(self.label_14)

        self.frame_87 = QFrame(self.frame_79)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_87)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.un_3_competitor_node_8 = QTextEdit(self.frame_87)
        self.un_3_competitor_node_8.setObjectName(u"un_3_competitor_node_8")
        self.un_3_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_71.addWidget(self.un_3_competitor_node_8)

        self.un_3_competitor_node_9 = QTextEdit(self.frame_87)
        self.un_3_competitor_node_9.setObjectName(u"un_3_competitor_node_9")
        self.un_3_competitor_node_9.setMaximumSize(QSize(16777215, 50))
        self.un_3_competitor_node_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_3_competitor_node_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_71.addWidget(self.un_3_competitor_node_9)


        self.verticalLayout_54.addWidget(self.frame_87)


        self.horizontalLayout_37.addWidget(self.frame_79)

        self.match_5.addWidget(self.under_3)
        self.Under2 = QWidget()
        self.Under2.setObjectName(u"Under2")
        self.horizontalLayout_38 = QHBoxLayout(self.Under2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_105 = QFrame(self.Under2)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_105)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.frame_106 = QFrame(self.frame_105)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_106)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.label_23 = QLabel(self.frame_106)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.verticalLayout_83.addWidget(self.label_23)


        self.verticalLayout_82.addWidget(self.frame_106)

        self.frame_107 = QFrame(self.frame_105)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.frame_108 = QFrame(self.frame_107)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_108)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.un_2_competitor_node_1 = QTextEdit(self.frame_108)
        self.un_2_competitor_node_1.setObjectName(u"un_2_competitor_node_1")
        self.un_2_competitor_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_84.addWidget(self.un_2_competitor_node_1)

        self.un_2_competitor_node_2 = QTextEdit(self.frame_108)
        self.un_2_competitor_node_2.setObjectName(u"un_2_competitor_node_2")
        self.un_2_competitor_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_84.addWidget(self.un_2_competitor_node_2)


        self.horizontalLayout_42.addWidget(self.frame_108)

        self.frame_109 = QFrame(self.frame_107)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setMaximumSize(QSize(50, 16777215))
        self.frame_109.setFrameShape(QFrame.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_109)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.un_2_point_node_1 = QTextEdit(self.frame_109)
        self.un_2_point_node_1.setObjectName(u"un_2_point_node_1")
        self.un_2_point_node_1.setMaximumSize(QSize(16777215, 50))
        self.un_2_point_node_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_point_node_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_85.addWidget(self.un_2_point_node_1)

        self.un_2_point_node_2 = QTextEdit(self.frame_109)
        self.un_2_point_node_2.setObjectName(u"un_2_point_node_2")
        self.un_2_point_node_2.setMaximumSize(QSize(16777215, 50))
        self.un_2_point_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_point_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_85.addWidget(self.un_2_point_node_2)


        self.horizontalLayout_42.addWidget(self.frame_109)


        self.verticalLayout_82.addWidget(self.frame_107)


        self.horizontalLayout_38.addWidget(self.frame_105)

        self.frame_98 = QFrame(self.Under2)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(25, 0))
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_98)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_22 = QLabel(self.frame_98)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)
        self.label_22.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_77.addWidget(self.label_22)

        self.frame_104 = QFrame(self.frame_98)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setEnabled(True)
        self.frame_104.setFrameShape(QFrame.NoFrame)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self._4 = QVBoxLayout(self.frame_104)
        self._4.setSpacing(0)
        self._4.setObjectName(u"_4")
        self._4.setContentsMargins(0, 0, 0, 0)
        self.un_2_competitor_node_3 = QTextEdit(self.frame_104)
        self.un_2_competitor_node_3.setObjectName(u"un_2_competitor_node_3")
        self.un_2_competitor_node_3.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._4.addWidget(self.un_2_competitor_node_3)

        self.un_2_competitor_node_4 = QTextEdit(self.frame_104)
        self.un_2_competitor_node_4.setObjectName(u"un_2_competitor_node_4")
        self.un_2_competitor_node_4.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self._4.addWidget(self.un_2_competitor_node_4)


        self.verticalLayout_77.addWidget(self.frame_104)


        self.horizontalLayout_38.addWidget(self.frame_98)

        self.frame_110 = QFrame(self.Under2)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMinimumSize(QSize(25, 0))
        self.frame_110.setFrameShape(QFrame.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_110)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.label_24 = QLabel(self.frame_110)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)
        self.label_24.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_86.addWidget(self.label_24)

        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.frame_111)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.un_2_competitor_node_5 = QTextEdit(self.frame_111)
        self.un_2_competitor_node_5.setObjectName(u"un_2_competitor_node_5")
        self.un_2_competitor_node_5.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_87.addWidget(self.un_2_competitor_node_5)

        self.un_2_competitor_node_6 = QTextEdit(self.frame_111)
        self.un_2_competitor_node_6.setObjectName(u"un_2_competitor_node_6")
        self.un_2_competitor_node_6.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_87.addWidget(self.un_2_competitor_node_6)


        self.verticalLayout_86.addWidget(self.frame_111)


        self.horizontalLayout_38.addWidget(self.frame_110)

        self.frame_88 = QFrame(self.Under2)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(25, 0))
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_88)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, -1, -1, -1)
        self.label_16 = QLabel(self.frame_88)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_66.addWidget(self.label_16)

        self.frame_95 = QFrame(self.frame_88)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setStyleSheet(u"")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_95)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.un_2_competitor_node_7 = QTextEdit(self.frame_95)
        self.un_2_competitor_node_7.setObjectName(u"un_2_competitor_node_7")
        self.un_2_competitor_node_7.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_72.addWidget(self.un_2_competitor_node_7)

        self.un_2_competitor_node_8 = QTextEdit(self.frame_95)
        self.un_2_competitor_node_8.setObjectName(u"un_2_competitor_node_8")
        self.un_2_competitor_node_8.setMaximumSize(QSize(16777215, 50))
        self.un_2_competitor_node_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.un_2_competitor_node_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_72.addWidget(self.un_2_competitor_node_8)


        self.verticalLayout_66.addWidget(self.frame_95)


        self.horizontalLayout_38.addWidget(self.frame_88)

        self.match_5.addWidget(self.Under2)

        self.horizontalLayout_31.addWidget(self.match_5)

        self.AllMatchesWraper.addWidget(self.MatchUnder5)
        self.MatchUnder2 = QWidget()
        self.MatchUnder2.setObjectName(u"MatchUnder2")
        self.horizontalLayout_33 = QHBoxLayout(self.MatchUnder2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.AllMatchesWraper.addWidget(self.MatchUnder2)
        self.TeemMatch = QWidget()
        self.TeemMatch.setObjectName(u"TeemMatch")
        self.verticalLayout_165 = QVBoxLayout(self.TeemMatch)
        self.verticalLayout_165.setObjectName(u"verticalLayout_165")
        self.frame_215 = QFrame(self.TeemMatch)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setMaximumSize(QSize(16777215, 120))
        self.frame_215.setStyleSheet(u"QTextEdit {\n"
"	color: rgb(54, 54, 54);\n"
"	font: 75 35pt \"Calibri\";\n"
"	font-weight: bold;\n"
"	text-align: center;\n"
"}")
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.TeamName_1 = QLabel(self.frame_215)
        self.TeamName_1.setObjectName(u"TeamName_1")
        self.TeamName_1.setFont(font1)
        self.TeamName_1.setStyleSheet(u"QLabel {\n"
"	\n"
"}")
        self.TeamName_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.TeamName_1)

        self.team_1_score = QTextEdit(self.frame_215)
        self.team_1_score.setObjectName(u"team_1_score")
        self.team_1_score.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_74.addWidget(self.team_1_score)

        self.label_56 = QLabel(self.frame_215)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMaximumSize(QSize(10, 16777215))
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(25)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(9)
        self.label_56.setFont(font3)
        self.label_56.setStyleSheet(u"font: 75 25pt \"Calibri\";\n"
"color:rgb(255, 255, 255);")

        self.horizontalLayout_74.addWidget(self.label_56)

        self.team_2_score = QTextEdit(self.frame_215)
        self.team_2_score.setObjectName(u"team_2_score")
        self.team_2_score.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_74.addWidget(self.team_2_score)

        self.TeamName_2 = QLabel(self.frame_215)
        self.TeamName_2.setObjectName(u"TeamName_2")
        self.TeamName_2.setFont(font1)
        self.TeamName_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_74.addWidget(self.TeamName_2)


        self.verticalLayout_165.addWidget(self.frame_215)

        self.frame_216 = QFrame(self.TeemMatch)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setMinimumSize(QSize(0, 100))
        self.frame_216.setMaximumSize(QSize(16777215, 500))
        self.frame_216.setStyleSheet(u"QTextEdit {\n"
"	width: 100px;\n"
"}")
        self.frame_216.setFrameShape(QFrame.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_216)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.frame_217 = QFrame(self.frame_216)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setFrameShape(QFrame.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_217)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.team_1_competitor_1 = QTextEdit(self.frame_217)
        self.team_1_competitor_1.setObjectName(u"team_1_competitor_1")
        self.team_1_competitor_1.setMaximumSize(QSize(630, 16777215))

        self.verticalLayout_167.addWidget(self.team_1_competitor_1)

        self.team_1_competitor_2 = QTextEdit(self.frame_217)
        self.team_1_competitor_2.setObjectName(u"team_1_competitor_2")
        self.team_1_competitor_2.setMaximumSize(QSize(630, 16777215))

        self.verticalLayout_167.addWidget(self.team_1_competitor_2)

        self.team_1_competitor_3 = QTextEdit(self.frame_217)
        self.team_1_competitor_3.setObjectName(u"team_1_competitor_3")
        self.team_1_competitor_3.setMaximumSize(QSize(630, 16777215))

        self.verticalLayout_167.addWidget(self.team_1_competitor_3)

        self.team_1_competitor_4 = QTextEdit(self.frame_217)
        self.team_1_competitor_4.setObjectName(u"team_1_competitor_4")
        self.team_1_competitor_4.setMaximumSize(QSize(630, 16777215))

        self.verticalLayout_167.addWidget(self.team_1_competitor_4)


        self.horizontalLayout_75.addWidget(self.frame_217)

        self.frame_218 = QFrame(self.frame_216)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setStyleSheet(u"QTextEdit {\n"
"	margin-left: 108px;\n"
"}")
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_218)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.team_2_competitor_1 = QTextEdit(self.frame_218)
        self.team_2_competitor_1.setObjectName(u"team_2_competitor_1")
        self.team_2_competitor_1.setMaximumSize(QSize(16777215, 16777215))
        self.team_2_competitor_1.setStyleSheet(u"")

        self.verticalLayout_166.addWidget(self.team_2_competitor_1)

        self.team_2_competitor_2 = QTextEdit(self.frame_218)
        self.team_2_competitor_2.setObjectName(u"team_2_competitor_2")
        self.team_2_competitor_2.setMaximumSize(QSize(16777215, 16777215))
        self.team_2_competitor_2.setStyleSheet(u"")

        self.verticalLayout_166.addWidget(self.team_2_competitor_2)

        self.team_2_competitor_3 = QTextEdit(self.frame_218)
        self.team_2_competitor_3.setObjectName(u"team_2_competitor_3")
        self.team_2_competitor_3.setMaximumSize(QSize(16777215, 16777215))
        self.team_2_competitor_3.setStyleSheet(u"")

        self.verticalLayout_166.addWidget(self.team_2_competitor_3)

        self.team_2_competitor_4 = QTextEdit(self.frame_218)
        self.team_2_competitor_4.setObjectName(u"team_2_competitor_4")
        self.team_2_competitor_4.setMaximumSize(QSize(16777215, 16777215))
        self.team_2_competitor_4.setStyleSheet(u"")

        self.verticalLayout_166.addWidget(self.team_2_competitor_4)


        self.horizontalLayout_75.addWidget(self.frame_218)


        self.verticalLayout_165.addWidget(self.frame_216)

        self.frame_219 = QFrame(self.TeemMatch)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setMinimumSize(QSize(40, 40))
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_219)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame_219)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(40, 40))
        self.pushButton_3.setStyleSheet(u"background:transparent;")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/icons/cil-arrow-top.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon9)

        self.verticalLayout_168.addWidget(self.pushButton_3, 0, Qt.AlignHCenter)

        self.frame_220 = QFrame(self.frame_219)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)

        self.verticalLayout_168.addWidget(self.frame_220)


        self.verticalLayout_165.addWidget(self.frame_219)

        self.AllMatchesWraper.addWidget(self.TeemMatch)

        self.verticalLayout_20.addWidget(self.AllMatchesWraper)


        self.horizontalLayout_6.addWidget(self.Content_wraper)

        self.ControlPanel = QFrame(self.AcountPage)
        self.ControlPanel.setObjectName(u"ControlPanel")
        self.ControlPanel.setMinimumSize(QSize(250, 0))
        self.ControlPanel.setMaximumSize(QSize(250, 16777215))
        self.ControlPanel.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(61, 61, 61);\n"
"}\n"
"\n"
"QTextEdit{\n"
"   background-color: rgb(217, 217, 217);\n"
"}\n"
"QPushButton{	\n"
"	background-color: rgb(30, 30, 30);\n"
" 	border-radius: 2px;\n"
"	font: 75 11pt \"Calibri\";\n"
"	color: rgb(186, 186, 186);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(157, 157, 157);\n"
"	color: rgb(0, 0, 0,)\n"
"}\n"
"")
        self.ControlPanel.setFrameShape(QFrame.StyledPanel)
        self.ControlPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.ControlPanel)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.DisplayCompetitors = QFrame(self.ControlPanel)
        self.DisplayCompetitors.setObjectName(u"DisplayCompetitors")
        self.DisplayCompetitors.setFrameShape(QFrame.StyledPanel)
        self.DisplayCompetitors.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.DisplayCompetitors)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.pushButton = QPushButton(self.DisplayCompetitors)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(11)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.pushButton.setFont(font4)

        self.verticalLayout_18.addWidget(self.pushButton)

        self.Competitor_1 = QTextEdit(self.DisplayCompetitors)
        self.Competitor_1.setObjectName(u"Competitor_1")
        self.Competitor_1.setMaximumSize(QSize(16777215, 160))
        self.Competitor_1.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.Competitor_1)

        self.pushButton_2 = QPushButton(self.DisplayCompetitors)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font4)

        self.verticalLayout_18.addWidget(self.pushButton_2)

        self.Competitor_2 = QTextEdit(self.DisplayCompetitors)
        self.Competitor_2.setObjectName(u"Competitor_2")
        self.Competitor_2.setMaximumSize(QSize(16777215, 160))
        self.Competitor_2.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.Competitor_2)

        self.frame_3 = QFrame(self.DisplayCompetitors)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_3)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.frame_221 = QFrame(self.frame_3)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_221)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.win_left = QPushButton(self.frame_221)
        self.win_left.setObjectName(u"win_left")
        self.win_left.setMinimumSize(QSize(0, 30))

        self.verticalLayout_171.addWidget(self.win_left)

        self.win_right = QPushButton(self.frame_221)
        self.win_right.setObjectName(u"win_right")
        self.win_right.setMinimumSize(QSize(0, 30))

        self.verticalLayout_171.addWidget(self.win_right)


        self.verticalLayout_169.addWidget(self.frame_221)

        self.frame_222 = QFrame(self.frame_3)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setFrameShape(QFrame.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_222)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.make_match_button = QPushButton(self.frame_222)
        self.make_match_button.setObjectName(u"make_match_button")
        self.make_match_button.setMinimumSize(QSize(0, 30))

        self.verticalLayout_170.addWidget(self.make_match_button)

        self.go_to_all_match_button = QPushButton(self.frame_222)
        self.go_to_all_match_button.setObjectName(u"go_to_all_match_button")
        self.go_to_all_match_button.setMinimumSize(QSize(0, 30))

        self.verticalLayout_170.addWidget(self.go_to_all_match_button)


        self.verticalLayout_169.addWidget(self.frame_222)


        self.verticalLayout_18.addWidget(self.frame_3)


        self.verticalLayout_17.addWidget(self.DisplayCompetitors)

        self.frame_23 = QFrame(self.ControlPanel)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.prev_match = QPushButton(self.frame_23)
        self.prev_match.setObjectName(u"prev_match")
        self.prev_match.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.prev_match)

        self.next_match = QPushButton(self.frame_23)
        self.next_match.setObjectName(u"next_match")
        self.next_match.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_12.addWidget(self.next_match)


        self.verticalLayout_17.addWidget(self.frame_23)


        self.horizontalLayout_6.addWidget(self.ControlPanel)

        self.stackedWidget.addWidget(self.AcountPage)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)


        self.horizontalLayout.addWidget(self.center_main_items)

        self.right_menu = QFrame(self.main_body)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(0, 0))
        self.right_menu.setMaximumSize(QSize(0, 16777215))
        self.right_menu.setStyleSheet(u"background-color: rgb(81, 81, 81);")
        self.right_menu.setFrameShape(QFrame.StyledPanel)
        self.right_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.right_menu)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.CloseCommunicateButton = QPushButton(self.right_menu)
        self.CloseCommunicateButton.setObjectName(u"CloseCommunicateButton")
        self.CloseCommunicateButton.setMaximumSize(QSize(25, 25))
        self.CloseCommunicateButton.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseCommunicateButton.setIcon(icon10)

        self.verticalLayout_43.addWidget(self.CloseCommunicateButton)

        self.Communicate = QTextEdit(self.right_menu)
        self.Communicate.setObjectName(u"Communicate")

        self.verticalLayout_43.addWidget(self.Communicate)


        self.horizontalLayout.addWidget(self.right_menu)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget_2.setCurrentIndex(2)
        self.AllMatchesWraper.setCurrentIndex(4)
        self.match_16.setCurrentIndex(1)
        self.match_10.setCurrentIndex(2)
        self.Grup_I_Under10_G1.setCurrentIndex(2)
        self.Grup_II_Under10_G2.setCurrentIndex(2)
        self.match_5.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_menu_toggle_button.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.HomeButton.setText(QCoreApplication.translate("MainWindow", u"Strona g\u0142\u00f3wna", None))
        self.AccountButton.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None))
        self.AddCategoriesButton.setText(QCoreApplication.translate("MainWindow", u"Wprowadzanie zawodnik\u00f3w", None))
        self.AccountButton_3.setText(QCoreApplication.translate("MainWindow", u"Raporty", None))
        self.RandomFunctionsButton.setText(QCoreApplication.translate("MainWindow", u"Losowanie", None))
        self.InfoButton.setText(QCoreApplication.translate("MainWindow", u"Komunikaty", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.Hide_category_menu.setText("")
        self.Button_16_competitors.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.Button_10_competitors.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.Button_5_competitors.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Button_4_competitors.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Button_3_competitors.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Button_2_competitors.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Dodaj kategori\u0119", None))
        self.CategoriesToAdd_2.setText("")
        self.CategoriesBrowseButton_2.setText(QCoreApplication.translate("MainWindow", u"Przegl\u0105daj", None))
        self.AddCategoriesButton_3.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Dodane kategorie", None))
        ___qtablewidgetitem = self.CategoriesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nowa kolumna", None));
        ___qtablewidgetitem1 = self.CategoriesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Wiek", None));
        ___qtablewidgetitem2 = self.CategoriesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Waga", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nowa kolumna", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None));
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Krzy\u017c\u00f3wka do 16 zawodnik\u00f3w", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Krzy\u017c\u00f3wka do 10 zawodnik\u00f3w", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Grupa I", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Grupa II", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Krzy\u017c\u00f3wka do 5 zwodni\u00f3w", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Losuj", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Wyniki", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kategoria", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Dodaj kategori\u0119", None))
        self.CategoriesBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Przegl\u0105daj", None))
        self.AddCategoriesButton_2.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Dodane kategorie", None))
        self.FilterCattegoryButton.setText(QCoreApplication.translate("MainWindow", u"Filtruj", None))
        ___qtablewidgetitem5 = self.CompetitorsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119", None));
        ___qtablewidgetitem6 = self.CompetitorsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None));
        ___qtablewidgetitem7 = self.CompetitorsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Klub", None));
        ___qtablewidgetitem8 = self.CompetitorsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Numer Licencji", None));
        self.ComprtitorName.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119:", None))
        self.CompetitorSurname.setText(QCoreApplication.translate("MainWindow", u"Nazwisko:", None))
        self.CompetitorClub.setText(QCoreApplication.translate("MainWindow", u"Klub:", None))
        self.CompetitorBornDate.setText(QCoreApplication.translate("MainWindow", u"Rok urodzenia:", None))
        self.CompetitorLicenceNo.setText(QCoreApplication.translate("MainWindow", u"Nr licencji:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Waga", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Kategorie", None))
        ___qtablewidgetitem9 = self.CompetitorCategories.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Grupa wiekowa", None));
        ___qtablewidgetitem10 = self.CompetitorCategories.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"P\u0142e\u0107", None));
        ___qtablewidgetitem11 = self.CompetitorCategories.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Kategoria", None));
        self.DeleteCompetitorCategoryButton.setText("")
        self.AddCompetitorCategoryButton.setText("")
        self.SaveCompetitorButton.setText(QCoreApplication.translate("MainWindow", u"               Zapisz zmiany dla zawodnika", None))
        self.SaveCategoriesToTxt.setText(QCoreApplication.translate("MainWindow", u"Generuj pliki do loswa\u0144", None))
        self.SaveCategoriesToPdf.setText(QCoreApplication.translate("MainWindow", u"Generuj pliki podsumowuj\u0105ce", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Dziecko", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"M\u0142odzik (u12)", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Kadet (u16)", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Junior (u18)", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"M\u0142odzierzowiec (u21)", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"M\u0142odzierzowiec (u23)", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Senior", None))
        self.saveSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Zapisz zmiany", None))
        self.Eliminations_button.setText(QCoreApplication.translate("MainWindow", u"Eliminacje", None))
        self.HalfFinal_button.setText(QCoreApplication.translate("MainWindow", u"P\u00f3\u0142 fina\u0142y", None))
        self.Repechage_button.setText(QCoreApplication.translate("MainWindow", u"Repasarze", None))
        self.Final_button.setText(QCoreApplication.translate("MainWindow", u"walki medalowe", None))
        self.Top_menu_slide_button.setText("")
        self.el_16_node_16.setMarkdown("")
        self.el_16_node_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:72;\"><br /></p></body></html>", None))
        self.el_16_node_16.setPlaceholderText("")
        self.el_16_node_24.setMarkdown("")
        self.el_16_node_24.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.rep_16_node_8.setMarkdown("")
        self.rep_16_node_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_9.setMarkdown("")
        self.rep_16_node_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_10.setMarkdown("")
        self.rep_16_node_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_11.setMarkdown("")
        self.rep_16_node_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_4.setMarkdown("")
        self.rep_16_node_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_5.setMarkdown("")
        self.rep_16_node_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_2.setMarkdown("")
        self.rep_16_node_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_12.setMarkdown("")
        self.rep_16_node_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_13.setMarkdown("")
        self.rep_16_node_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_14.setMarkdown("")
        self.rep_16_node_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_15.setMarkdown("")
        self.rep_16_node_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_6.setMarkdown("")
        self.rep_16_node_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_7.setMarkdown("")
        self.rep_16_node_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.rep_16_node_3.setMarkdown("")
        self.rep_16_node_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fina\u0142", None))
        self.el_16_node_2_cpy.setMarkdown("")
        self.el_16_node_2_cpy.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.el_16_node_3_cpy.setMarkdown("")
        self.el_16_node_3_cpy.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Walka o pierwszy br\u0105z", None))
        self.rep_16_node_2_cpy.setMarkdown("")
        self.rep_16_node_2_cpy.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.firstBronzeFinalist_16_node.setMarkdown("")
        self.firstBronzeFinalist_16_node.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Walka o drugi br\u0105z", None))
        self.rep_16_node_3_cpy.setMarkdown("")
        self.rep_16_node_3_cpy.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.secondBronzeFinalist_16_node.setMarkdown("")
        self.secondBronzeFinalist_16_node.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"P\u00f3\u0142 Fina\u0142 I", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"P\u00f3\u0142 Fina\u0142 II", None))
        self.Under_10_group_1_button.setText(QCoreApplication.translate("MainWindow", u"Grupa I", None))
        self.Under_10_group_2_button.setText(QCoreApplication.translate("MainWindow", u"Grupa II", None))
        self.Under_10_finals_button.setText(QCoreApplication.translate("MainWindow", u"Fina\u0142y", None))
        self.Top_menu_slide_button_2.setText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Grupa I", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Runda IV", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Runda V", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Grupa II", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Runda IV", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Runda V", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Fina\u0142", None))
        self.un_10_final_competitor_node_1.setMarkdown("")
        self.un_10_final_competitor_node_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.un_10_final_competitor_node_2.setMarkdown("")
        self.un_10_final_competitor_node_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"I P\u00f3\u0142fina\u0142", None))
        self.un_10_half_final_competitor_node_1.setMarkdown("")
        self.un_10_half_final_competitor_node_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.un_10_half_final_competitor_node_2.setMarkdown("")
        self.un_10_half_final_competitor_node_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"II P\u00f3\u0142fina\u0142", None))
        self.un_10_half_final_competitor_node_3.setMarkdown("")
        self.un_10_half_final_competitor_node_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.un_10_half_final_competitor_node_4.setMarkdown("")
        self.un_10_half_final_competitor_node_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:72;\"><br /></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Runda IV", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Runda V", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Zawodnicy", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Runda I", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Runda II", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Runda III", None))
        self.TeamName_1.setText(QCoreApplication.translate("MainWindow", u"Dru\u017cyna I", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.TeamName_2.setText(QCoreApplication.translate("MainWindow", u"Dru\u017cyna II", None))
        self.pushButton_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Zawodnik I", None))
        self.Competitor_1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Imi\u0119:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Nazwisko:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Klub:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Waga:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Wygrane:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Przegrane:</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Zawodnik II", None))
        self.Competitor_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Imi\u0119:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Nazwisko:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Klub:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inden"
                        "t:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Waga:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Wygrane:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Przegrane:</span></p></body></html>", None))
        self.win_left.setText(QCoreApplication.translate("MainWindow", u"Wygra\u0142 I", None))
        self.win_right.setText(QCoreApplication.translate("MainWindow", u"Wygra\u0142 II", None))
        self.make_match_button.setText(QCoreApplication.translate("MainWindow", u"Rozegraj mecz", None))
        self.go_to_all_match_button.setText(QCoreApplication.translate("MainWindow", u"Powr\u00f3t do krzy\u017c\u00f3wki", None))
        self.prev_match.setText(QCoreApplication.translate("MainWindow", u"Poprzedni", None))
        self.next_match.setText(QCoreApplication.translate("MainWindow", u"Nast\u0119pny", None))
        self.CloseCommunicateButton.setText("")
    # retranslateUi

