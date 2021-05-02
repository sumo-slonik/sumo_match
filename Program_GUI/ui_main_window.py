# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowRAsFZQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Program_GUI.gui_theme

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1177, 789)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"background-color: rgb(170, 0, 127);")
        self.main_header.setFrameShape(QFrame.StyledPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title_bar_container = QFrame(self.main_header)
        self.title_bar_container.setObjectName(u"title_bar_container")
        self.title_bar_container.setMaximumSize(QSize(16777215, 50))
        self.title_bar_container.setStyleSheet(u"background-color: rgb(255, 85, 255);")
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
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}\n"
"QFrame\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
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
        self.top_right_btns.setStyleSheet(u"background-color: rgb(85, 0, 127);")
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
        self.main_body.setStyleSheet(u"background-color: rgb(255, 85, 255);")
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
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	padding: 25px 10px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 0, 0);\n"
"}\n"
"")
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

        self.AccountButton_4 = QPushButton(self.frame)
        self.AccountButton_4.setObjectName(u"AccountButton_4")
        self.AccountButton_4.setStyleSheet(u"background-image: url(:/Icons/icons/cil-reload.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"")

        self.verticalLayout_42.addWidget(self.AccountButton_4)


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
        self.center_main_items.setStyleSheet(u"background-color: rgb(85, 255, 127);")
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
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.HomePage.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.stackedWidget.addWidget(self.HomePage)
        self.SummaryPage = QWidget()
        self.SummaryPage.setObjectName(u"SummaryPage")
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
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)

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
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_112)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.label_25 = QLabel(self.frame_112)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_25.setFont(font1)

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
        self.frame_115.setFrameShape(QFrame.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Raised)
        self.verticalLayout_89 = QVBoxLayout(self.frame_115)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.label_26 = QLabel(self.frame_115)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.verticalLayout_89.addWidget(self.label_26)

        self.AddedCategories = QScrollArea(self.frame_115)
        self.AddedCategories.setObjectName(u"AddedCategories")
        self.AddedCategories.setWidgetResizable(True)
        self.AddedCategoriesContents = QWidget()
        self.AddedCategoriesContents.setObjectName(u"AddedCategoriesContents")
        self.AddedCategoriesContents.setGeometry(QRect(0, 0, 250, 253))
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
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_113)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.frame_118 = QFrame(self.frame_113)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMaximumSize(QSize(16777215, 50))
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_118)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.comboBox_2 = QComboBox(self.frame_118)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_50.addWidget(self.comboBox_2)

        self.comboBox_3 = QComboBox(self.frame_118)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_50.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.frame_118)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.horizontalLayout_50.addWidget(self.comboBox_4)

        self.pushButton_5 = QPushButton(self.frame_118)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_50.addWidget(self.pushButton_5)


        self.verticalLayout_91.addWidget(self.frame_118)

        self.frame_119 = QFrame(self.frame_113)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_119)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.tableWidget = QTableWidget(self.frame_119)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_92.addWidget(self.tableWidget)


        self.verticalLayout_91.addWidget(self.frame_119)


        self.horizontalLayout_47.addWidget(self.frame_113)


        self.horizontalLayout_46.addWidget(self.frame_62)

        self.stackedWidget.addWidget(self.CompetitorInputPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.SettingsPage.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.stackedWidget.addWidget(self.SettingsPage)
        self.AcountPage = QWidget()
        self.AcountPage.setObjectName(u"AcountPage")
        self.AcountPage.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.horizontalLayout_6 = QHBoxLayout(self.AcountPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Content_wraper = QFrame(self.AcountPage)
        self.Content_wraper.setObjectName(u"Content_wraper")
        self.Content_wraper.setFrameShape(QFrame.StyledPanel)
        self.Content_wraper.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.Content_wraper)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.AllMatchesWraper = QStackedWidget(self.Content_wraper)
        self.AllMatchesWraper.setObjectName(u"AllMatchesWraper")
        self.AllMatchesWraper.setStyleSheet(u"QTextEdit\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
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
        icon5 = QIcon()
        icon5.addFile(u":/Icons/icons/cil-arrow-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Top_menu_slide_button.setIcon(icon5)

        self.verticalLayout_21.addWidget(self.Top_menu_slide_button, 0, Qt.AlignHCenter)


        self.verticalLayout_118.addWidget(self.Top_menu_wraper)

        self.match_16 = QStackedWidget(self.MatchUnder16)
        self.match_16.setObjectName(u"match_16")
        self.match_16.setStyleSheet(u"QTextEdit\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.Eliminations = QWidget()
        self.Eliminations.setObjectName(u"Eliminations")
        self.verticalLayout_19 = QVBoxLayout(self.Eliminations)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_4 = QFrame(self.Eliminations)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(False)
        self.frame_4.setStyleSheet(u"QTextEdit\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
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
        self.el_16_node_24.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
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
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)

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
        self.label_7.setFont(font2)

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
        self.rep_16_node_2_cpy.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.rep_16_node_2_cpy.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_2_cpy.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.rep_16_node_2_cpy.setUndoRedoEnabled(False)

        self.horizontalLayout_35.addWidget(self.rep_16_node_2_cpy)

        self.firstBronzeFinalist_16_node = QTextEdit(self.frame_54)
        self.firstBronzeFinalist_16_node.setObjectName(u"firstBronzeFinalist_16_node")
        self.firstBronzeFinalist_16_node.setMaximumSize(QSize(270, 50))
        self.firstBronzeFinalist_16_node.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
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
        self.frame_24.setStyleSheet(u"QTextEdit\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
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
        self.label.setFont(font2)

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
        self.label_2.setFont(font2)

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
        self.MatchUnder5 = QWidget()
        self.MatchUnder5.setObjectName(u"MatchUnder5")
        self.horizontalLayout_31 = QHBoxLayout(self.MatchUnder5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.match_5 = QStackedWidget(self.MatchUnder5)
        self.match_5.setObjectName(u"match_5")
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

        self.verticalLayout_20.addWidget(self.AllMatchesWraper)


        self.horizontalLayout_6.addWidget(self.Content_wraper)

        self.ControlPanel = QFrame(self.AcountPage)
        self.ControlPanel.setObjectName(u"ControlPanel")
        self.ControlPanel.setMinimumSize(QSize(250, 0))
        self.ControlPanel.setMaximumSize(QSize(250, 16777215))
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
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton.setFont(font3)

        self.verticalLayout_18.addWidget(self.pushButton)

        self.Competitor_1 = QTextEdit(self.DisplayCompetitors)
        self.Competitor_1.setObjectName(u"Competitor_1")
        self.Competitor_1.setMaximumSize(QSize(16777215, 160))
        self.Competitor_1.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.Competitor_1)

        self.pushButton_2 = QPushButton(self.DisplayCompetitors)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font3)

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
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.win_left = QPushButton(self.frame_3)
        self.win_left.setObjectName(u"win_left")

        self.horizontalLayout_13.addWidget(self.win_left)

        self.win_right = QPushButton(self.frame_3)
        self.win_right.setObjectName(u"win_right")

        self.horizontalLayout_13.addWidget(self.win_right)


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

        self.horizontalLayout_12.addWidget(self.prev_match)

        self.next_match = QPushButton(self.frame_23)
        self.next_match.setObjectName(u"next_match")

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
        self.right_menu.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.right_menu.setFrameShape(QFrame.StyledPanel)
        self.right_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.right_menu)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.CloseCommunicateButton = QPushButton(self.right_menu)
        self.CloseCommunicateButton.setObjectName(u"CloseCommunicateButton")
        self.CloseCommunicateButton.setMaximumSize(QSize(25, 25))
        self.CloseCommunicateButton.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/icons/cil-x-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.CloseCommunicateButton.setIcon(icon6)

        self.verticalLayout_43.addWidget(self.CloseCommunicateButton)

        self.Communicate = QTextEdit(self.right_menu)
        self.Communicate.setObjectName(u"Communicate")

        self.verticalLayout_43.addWidget(self.Communicate)


        self.horizontalLayout.addWidget(self.right_menu)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 10))
        self.main_footer.setMaximumSize(QSize(16777215, 0))
        self.main_footer.setStyleSheet(u"background-color: rgb(170, 85, 127);")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.main_footer)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.AllMatchesWraper.setCurrentIndex(0)
        self.match_16.setCurrentIndex(0)
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
        self.AccountButton_4.setText(QCoreApplication.translate("MainWindow", u"Losowanie", None))
        self.InfoButton.setText(QCoreApplication.translate("MainWindow", u"Komunikaty", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
        self.Hide_category_menu.setText("")
        self.Button_16_competitors.setText(QCoreApplication.translate("MainWindow", u"16", None))
        self.Button_5_competitors.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Button_4_competitors.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Button_3_competitors.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Button_2_competitors.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Wyniki", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Kategoria", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Dodaj kategori\u0119", None))
        self.CategoriesBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Przegl\u0105daj", None))
        self.AddCategoriesButton_2.setText(QCoreApplication.translate("MainWindow", u"Dodaj", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Dodane kategorie", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Filtruj", None))
        self.Eliminations_button.setText(QCoreApplication.translate("MainWindow", u"Eliminacje", None))
        self.HalfFinal_button.setText(QCoreApplication.translate("MainWindow", u"P\u00f3\u0142 fina\u0142y", None))
        self.Repechage_button.setText(QCoreApplication.translate("MainWindow", u"Repasarze", None))
        self.Final_button.setText(QCoreApplication.translate("MainWindow", u"walki medalowe", None))
        self.Top_menu_slide_button.setText("")
        self.el_16_node_16.setMarkdown("")
        self.el_16_node_16.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:14pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.el_16_node_16.setPlaceholderText("")
        self.el_16_node_24.setMarkdown("")
        self.el_16_node_24.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
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
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.firstBronzeFinalist_16_node.setMarkdown("")
        self.firstBronzeFinalist_16_node.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
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
        self.prev_match.setText(QCoreApplication.translate("MainWindow", u"Poprzedni Mecz", None))
        self.next_match.setText(QCoreApplication.translate("MainWindow", u"Nast\u0119pny Mecz", None))
        self.CloseCommunicateButton.setText("")
    # retranslateUi

