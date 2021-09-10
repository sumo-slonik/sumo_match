# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'competitiorsWeightAkdIDR.ui'
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
        MainWindow.resize(1070, 733)
        MainWindow.setMinimumSize(QSize(1070, 733))
        MainWindow.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(7, 27, 45);\n"
"\n"
"}\n"
"\n"
"#Main\n"
"{\n"
"background-color: rgb(30, 255, 45);\n"
"}\n"
"\n"
"#Fotter\n"
"{\n"
"	background-color: rgb(203, 255, 135);\n"
"}\n"
"\n"
"#Header\n"
"{\n"
"	background-color: rgb(255, 128, 162);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Header = QFrame(self.frame)
        self.Header.setObjectName(u"Header")
        self.Header.setMaximumSize(QSize(16777215, 16777215))
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.Header)

        self.Main = QFrame(self.frame)
        self.Main.setObjectName(u"Main")
        self.Main.setFrameShape(QFrame.StyledPanel)
        self.Main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Main)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_2 = QFrame(self.Main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(450, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.calendarWidget = QCalendarWidget(self.frame_2)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout_3.addWidget(self.calendarWidget)

        self.CompetitonTable = QTableWidget(self.frame_2)
        if (self.CompetitonTable.columnCount() < 2):
            self.CompetitonTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.CompetitonTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.CompetitonTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.CompetitonTable.setObjectName(u"CompetitonTable")

        self.verticalLayout_3.addWidget(self.CompetitonTable)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.CompetitorsPanel = QFrame(self.Main)
        self.CompetitorsPanel.setObjectName(u"CompetitorsPanel")
        self.CompetitorsPanel.setFrameShape(QFrame.StyledPanel)
        self.CompetitorsPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.CompetitorsPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.CompetitorsPanel)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.CompetitorsTable = QTableWidget(self.frame_4)
        if (self.CompetitorsTable.columnCount() < 5):
            self.CompetitorsTable.setColumnCount(5)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.CompetitorsTable.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        self.CompetitorsTable.setObjectName(u"CompetitorsTable")

        self.verticalLayout_4.addWidget(self.CompetitorsTable)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.SingleCompetitorPanel = QFrame(self.CompetitorsPanel)
        self.SingleCompetitorPanel.setObjectName(u"SingleCompetitorPanel")
        self.SingleCompetitorPanel.setMinimumSize(QSize(0, 200))
        self.SingleCompetitorPanel.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: rgb(184, 172, 255);\n"
" 	border-radius: 15px;\n"
"	height:30%\n"
"}")
        self.SingleCompetitorPanel.setFrameShape(QFrame.StyledPanel)
        self.SingleCompetitorPanel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.SingleCompetitorPanel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.CompetitorDetails = QFrame(self.SingleCompetitorPanel)
        self.CompetitorDetails.setObjectName(u"CompetitorDetails")
        self.CompetitorDetails.setMinimumSize(QSize(300, 350))
        self.CompetitorDetails.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: rgb(242, 98, 255);\n"
"}")
        self.CompetitorDetails.setFrameShape(QFrame.StyledPanel)
        self.CompetitorDetails.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.CompetitorDetails)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.CompetitorDetails)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.CompetitorNameFrame = QFrame(self.frame_7)
        self.CompetitorNameFrame.setObjectName(u"CompetitorNameFrame")
        self.CompetitorNameFrame.setMinimumSize(QSize(0, 30))
        self.CompetitorNameFrame.setFrameShape(QFrame.StyledPanel)
        self.CompetitorNameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.CompetitorNameFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.CompetitorNameFrame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.CompetitorName = QLabel(self.CompetitorNameFrame)
        self.CompetitorName.setObjectName(u"CompetitorName")

        self.horizontalLayout_6.addWidget(self.CompetitorName)


        self.verticalLayout_7.addWidget(self.CompetitorNameFrame)

        self.CompetitorSurnameFrame = QFrame(self.frame_7)
        self.CompetitorSurnameFrame.setObjectName(u"CompetitorSurnameFrame")
        self.CompetitorSurnameFrame.setMinimumSize(QSize(0, 30))
        self.CompetitorSurnameFrame.setFrameShape(QFrame.StyledPanel)
        self.CompetitorSurnameFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.CompetitorSurnameFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.CompetitorSurnameFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.CompetitorSurname = QLabel(self.CompetitorSurnameFrame)
        self.CompetitorSurname.setObjectName(u"CompetitorSurname")

        self.horizontalLayout_10.addWidget(self.CompetitorSurname)


        self.verticalLayout_7.addWidget(self.CompetitorSurnameFrame)

        self.CompetitorBornDateFrame = QFrame(self.frame_7)
        self.CompetitorBornDateFrame.setObjectName(u"CompetitorBornDateFrame")
        self.CompetitorBornDateFrame.setMinimumSize(QSize(0, 30))
        self.CompetitorBornDateFrame.setFrameShape(QFrame.StyledPanel)
        self.CompetitorBornDateFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.CompetitorBornDateFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.CompetitorBornDateFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.CompetitorBornDate = QLabel(self.CompetitorBornDateFrame)
        self.CompetitorBornDate.setObjectName(u"CompetitorBornDate")

        self.horizontalLayout_7.addWidget(self.CompetitorBornDate)


        self.verticalLayout_7.addWidget(self.CompetitorBornDateFrame)

        self.CompetitorClubFrame = QFrame(self.frame_7)
        self.CompetitorClubFrame.setObjectName(u"CompetitorClubFrame")
        self.CompetitorClubFrame.setMinimumSize(QSize(0, 30))
        self.CompetitorClubFrame.setFrameShape(QFrame.StyledPanel)
        self.CompetitorClubFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.CompetitorClubFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.CompetitorClubFrame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.CompetitorClub = QLabel(self.CompetitorClubFrame)
        self.CompetitorClub.setObjectName(u"CompetitorClub")

        self.horizontalLayout_8.addWidget(self.CompetitorClub)


        self.verticalLayout_7.addWidget(self.CompetitorClubFrame)

        self.CompetitorClubFrame_2 = QFrame(self.frame_7)
        self.CompetitorClubFrame_2.setObjectName(u"CompetitorClubFrame_2")
        self.CompetitorClubFrame_2.setMinimumSize(QSize(0, 30))
        self.CompetitorClubFrame_2.setFrameShape(QFrame.StyledPanel)
        self.CompetitorClubFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.CompetitorClubFrame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.CompetitorClubFrame_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.CompetitorLicenceNo = QLabel(self.CompetitorClubFrame_2)
        self.CompetitorLicenceNo.setObjectName(u"CompetitorLicenceNo")

        self.horizontalLayout_9.addWidget(self.CompetitorLicenceNo)


        self.verticalLayout_7.addWidget(self.CompetitorClubFrame_2)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.CompetitorDetails)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_9)


        self.horizontalLayout_3.addWidget(self.CompetitorDetails)

        self.CompetitorCategories = QFrame(self.SingleCompetitorPanel)
        self.CompetitorCategories.setObjectName(u"CompetitorCategories")
        self.CompetitorCategories.setMinimumSize(QSize(0, 0))
        self.CompetitorCategories.setFrameShape(QFrame.StyledPanel)
        self.CompetitorCategories.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.CompetitorCategories)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableWidget_3 = QTableWidget(self.CompetitorCategories)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setMaximumSize(QSize(300, 16777215))

        self.horizontalLayout_4.addWidget(self.tableWidget_3)

        self.CompetitorButtons = QFrame(self.CompetitorCategories)
        self.CompetitorButtons.setObjectName(u"CompetitorButtons")
        self.CompetitorButtons.setMinimumSize(QSize(0, 0))
        self.CompetitorButtons.setStyleSheet(u"")
        self.CompetitorButtons.setFrameShape(QFrame.StyledPanel)
        self.CompetitorButtons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.CompetitorButtons)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.pushButton_3 = QPushButton(self.CompetitorButtons)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.CompetitorButtons)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_4.addWidget(self.CompetitorButtons)

        self.frame_3 = QFrame(self.CompetitorCategories)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.hideCompetitorPanelButton = QPushButton(self.frame_3)
        self.hideCompetitorPanelButton.setObjectName(u"hideCompetitorPanelButton")
        self.hideCompetitorPanelButton.setMinimumSize(QSize(30, 30))
        self.hideCompetitorPanelButton.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.hideCompetitorPanelButton)


        self.horizontalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.CompetitorCategories)


        self.verticalLayout_2.addWidget(self.SingleCompetitorPanel)


        self.horizontalLayout_2.addWidget(self.CompetitorsPanel)


        self.verticalLayout.addWidget(self.Main)

        self.Fotter = QFrame(self.frame)
        self.Fotter.setObjectName(u"Fotter")
        self.Fotter.setMaximumSize(QSize(16777215, 16777215))
        self.Fotter.setFrameShape(QFrame.StyledPanel)
        self.Fotter.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.Fotter)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1070, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.CompetitonTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nazwa imprezy", None));
        ___qtablewidgetitem1 = self.CompetitonTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Miasto", None));
        ___qtablewidgetitem2 = self.CompetitorsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119", None));
        ___qtablewidgetitem3 = self.CompetitorsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None));
        ___qtablewidgetitem4 = self.CompetitorsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"P\u0142e\u0107", None));
        ___qtablewidgetitem5 = self.CompetitorsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data urodzenia", None));
        ___qtablewidgetitem6 = self.CompetitorsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Numer licencji", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119", None))
        self.CompetitorName.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nazwisko", None))
        self.CompetitorSurname.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Data urodzenia", None))
        self.CompetitorBornDate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Klub", None))
        self.CompetitorClub.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Numer licencji", None))
        self.CompetitorLicenceNo.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Wiek", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Waga", None));
        self.pushButton_3.setText("")
        self.pushButton_2.setText("")
        self.hideCompetitorPanelButton.setText("")
    # retranslateUi

