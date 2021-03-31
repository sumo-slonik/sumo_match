# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowtDHhjz.ui'
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
        MainWindow.resize(1243, 752)
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
        self.eliminations_16 = QStackedWidget(self.AcountPage)
        self.eliminations_16.setObjectName(u"eliminations_16")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_19 = QVBoxLayout(self.page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(False)
        self.frame_2.setStyleSheet(u"QTextEdit\n"
"{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"	font: 75 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(250, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_4)
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

        self.el_16_node_2 = QTextEdit(self.frame_10)
        self.el_16_node_2.setObjectName(u"el_16_node_2")
        self.el_16_node_2.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_6.addWidget(self.el_16_node_2)


        self.horizontalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
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


        self.horizontalLayout_7.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 250))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_17 = QFrame(self.frame_14)
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

        self.el_16_node_3 = QTextEdit(self.frame_17)
        self.el_16_node_3.setObjectName(u"el_16_node_3")
        self.el_16_node_3.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_12.addWidget(self.el_16_node_3)


        self.horizontalLayout_10.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_14)
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

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(45, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.el_16_node_24 = QTextEdit(self.frame_15)
        self.el_16_node_24.setObjectName(u"el_16_node_24")
        self.el_16_node_24.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_24.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.el_16_node_24.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_24.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_24.setUndoRedoEnabled(False)

        self.verticalLayout_10.addWidget(self.el_16_node_24)

        self.el_16_node_25 = QTextEdit(self.frame_15)
        self.el_16_node_25.setObjectName(u"el_16_node_25")
        self.el_16_node_25.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_25.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_25.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_10.addWidget(self.el_16_node_25)

        self.el_16_node_26 = QTextEdit(self.frame_15)
        self.el_16_node_26.setObjectName(u"el_16_node_26")
        self.el_16_node_26.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_26.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_26.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_10.addWidget(self.el_16_node_26)

        self.el_16_node_27 = QTextEdit(self.frame_15)
        self.el_16_node_27.setObjectName(u"el_16_node_27")
        self.el_16_node_27.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_27.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_27.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_10.addWidget(self.el_16_node_27)


        self.horizontalLayout_10.addWidget(self.frame_15)


        self.verticalLayout_16.addWidget(self.frame_14)

        self.frame_18 = QFrame(self.frame_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 250))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_21 = QFrame(self.frame_18)
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

        self.frame_20 = QFrame(self.frame_18)
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

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(45, 0))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.el_16_node_28 = QTextEdit(self.frame_19)
        self.el_16_node_28.setObjectName(u"el_16_node_28")
        self.el_16_node_28.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_28.setStyleSheet(u"")
        self.el_16_node_28.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_28.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_28)

        self.el_16_node_29 = QTextEdit(self.frame_19)
        self.el_16_node_29.setObjectName(u"el_16_node_29")
        self.el_16_node_29.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_29.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_29.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_29)

        self.el_16_node_30 = QTextEdit(self.frame_19)
        self.el_16_node_30.setObjectName(u"el_16_node_30")
        self.el_16_node_30.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_30.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_30.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_30)

        self.el_16_node_31 = QTextEdit(self.frame_19)
        self.el_16_node_31.setObjectName(u"el_16_node_31")
        self.el_16_node_31.setMaximumSize(QSize(16777215, 50))
        self.el_16_node_31.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.el_16_node_31.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_13.addWidget(self.el_16_node_31)


        self.horizontalLayout_11.addWidget(self.frame_19)


        self.verticalLayout_16.addWidget(self.frame_18)


        self.horizontalLayout_7.addWidget(self.frame_5)


        self.verticalLayout_19.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.eliminations_16.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.eliminations_16.addWidget(self.page_2)

        self.horizontalLayout_6.addWidget(self.eliminations_16)

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
        self.textEdit_3 = QTextEdit(self.DisplayCompetitors)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 40))
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.textEdit_3)

        self.textEdit = QTextEdit(self.DisplayCompetitors)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(16777215, 160))
        self.textEdit.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.textEdit)

        self.textEdit_4 = QTextEdit(self.DisplayCompetitors)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 40))
        self.textEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_4.setReadOnly(True)

        self.verticalLayout_18.addWidget(self.textEdit_4)

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

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


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
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Zawodnik I</span></p></body></html>", None))
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
        self.textEdit_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Zawodnik II</span></p></body></html>", None))
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

