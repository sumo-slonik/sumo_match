# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowBnAtwj.ui'
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
        MainWindow.resize(920, 658)
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
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 0))
        self.pushButton_4.setStyleSheet(u"background-image: url(:/Icons/icons/cil-home.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"padding-left: 50px;\n"
"\n"
"")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-image: url(:/Icons/icons/cil-user.png);\n"
"background-repeat:none;\n"
"background-position: center left;\n"
"\n"
"padding-left: 50px;\n"
"")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.pushButton_3)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.pushButton_2 = QPushButton(self.left_menu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/Icons/icons/cil-settings.png);\n"
"background-repeat:none;\n"
"padding-left: 50px;\n"
"background-position: center left;\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.cente_main_items = QFrame(self.main_body)
        self.cente_main_items.setObjectName(u"cente_main_items")
        self.cente_main_items.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.cente_main_items.setFrameShape(QFrame.StyledPanel)
        self.cente_main_items.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.cente_main_items)

        self.right_menu = QFrame(self.main_body)
        self.right_menu.setObjectName(u"right_menu")
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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_menu_toggle_button.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Acount", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

