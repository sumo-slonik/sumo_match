# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowFDbSyd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import GUI_test.test_kuba.gui_theme

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1165, 780)
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
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(7, 0, 0, 0)
        self.frame = QFrame(self.left_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.HomeButton = QPushButton(self.frame)
        self.HomeButton.setObjectName(u"HomeButton")
        self.HomeButton.setMinimumSize(QSize(100, 0))
        self.HomeButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-home.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"padding-left: 50px;\n"
"\n"
"")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.HomeButton)

        self.AccountButton = QPushButton(self.frame)
        self.AccountButton.setObjectName(u"AccountButton")
        self.AccountButton.setStyleSheet(u"background-image: url(:/Icons/icons/cil-user.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.AccountButton)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

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
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.HomePage = QWidget()
        self.HomePage.setObjectName(u"HomePage")
        self.HomePage.setStyleSheet(u"background-color: rgb(85, 170, 0);")
        self.stackedWidget.addWidget(self.HomePage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.SettingsPage.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.stackedWidget.addWidget(self.SettingsPage)
        self.AcountPage = QWidget()
        self.AcountPage.setObjectName(u"AcountPage")
        self.AcountPage.setStyleSheet(u"background-color: rgb(85, 85, 255);")
        self.horizontalLayout_6 = QHBoxLayout(self.AcountPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_2 = QFrame(self.AcountPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.Top_menu_wraper = QFrame(self.frame_2)
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
        icon4 = QIcon()
        icon4.addFile(u":/Icons/icons/cil-arrow-bottom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Top_menu_slide_button.setIcon(icon4)

        self.verticalLayout_21.addWidget(self.Top_menu_slide_button, 0, Qt.AlignHCenter)


        self.verticalLayout_20.addWidget(self.Top_menu_wraper)

        self.match_16 = QStackedWidget(self.frame_2)
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


        self.verticalLayout_19.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

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
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)

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
        self.label_7.setFont(font)

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
        self.label_5.setFont(font)

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
        self.label.setFont(font)

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
        self.label_2.setFont(font)

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

        self.verticalLayout_20.addWidget(self.match_16)


        self.horizontalLayout_6.addWidget(self.frame_2)

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
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)

        self.verticalLayout_18.addWidget(self.pushButton)

        self.textEdit = QTextEdit(self.DisplayCompetitors)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 160))
        self.textEdit.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.textEdit)

        self.pushButton_2 = QPushButton(self.DisplayCompetitors)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.verticalLayout_18.addWidget(self.pushButton_2)

        self.textEdit_2 = QTextEdit(self.DisplayCompetitors)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 160))
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.textEdit_2)

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

        self.Second_left_menu = QFrame(self.center_main_items)
        self.Second_left_menu.setObjectName(u"Second_left_menu")
        self.Second_left_menu.setFrameShape(QFrame.StyledPanel)
        self.Second_left_menu.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.Second_left_menu, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.center_main_items)

        self.right_menu = QFrame(self.main_body)
        self.right_menu.setObjectName(u"right_menu")
        self.right_menu.setMinimumSize(QSize(0, 0))
        self.right_menu.setMaximumSize(QSize(100, 16777215))
        self.right_menu.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.right_menu.setFrameShape(QFrame.StyledPanel)
        self.right_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.right_menu)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMaximumSize(QSize(16777215, 50))
        self.main_footer.setStyleSheet(u"background-color: rgb(170, 85, 127);")
        self.main_footer.setFrameShape(QFrame.StyledPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)
        self.match_16.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_menu_toggle_button.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.HomeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.AccountButton.setText(QCoreApplication.translate("MainWindow", u"Acount", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
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
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Zawodnik I", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
    # retranslateUi

