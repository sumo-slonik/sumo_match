from PySide2.QtWidgets import QFileDialog
import os
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def create_pdf_repr(Form,name):
    wrapper = QFrame(Form)
    wrapper.setObjectName(u"frame")
    wrapper.setMinimumSize(QSize(240, 60))
    wrapper.setMaximumSize(QSize(240, 60))
    wrapper.setFrameShape(QFrame.StyledPanel)
    wrapper.setFrameShadow(QFrame.Raised)
    wrapperLayout = QHBoxLayout(wrapper)
    wrapperLayout.setSpacing(0)
    wrapperLayout.setObjectName(u"horizontalLayout")
    wrapperLayout.setContentsMargins(0, 0, 0, 0)
    icon_pdf = QPushButton(wrapper)
    icon_pdf.setObjectName(u"pushButton")
    icon_pdf.setEnabled(False)
    icon_pdf.setMinimumSize(QSize(40, 40))
    icon_pdf.setMaximumSize(QSize(40, 40))
    icon_pdf.setStyleSheet(u"background-color: rgb(85, 85, 127);")
    icon = QIcon()
    icon.addFile(u"icons/cil-description.png", QSize(), QIcon.Normal, QIcon.Off)
    icon_pdf.setIcon(icon)
    wrapperLayout.addWidget(icon_pdf)

    PdfName = QTextEdit(wrapper)
    PdfName.setObjectName(u"PdfName")
    PdfName.setMinimumSize(QSize(150, 40))
    PdfName.setMaximumSize(QSize(150, 40))
    PdfName.setText(name)

    wrapperLayout.addWidget(PdfName)

    DelPdf = QPushButton(wrapper)
    DelPdf.setObjectName(u"DelPdf")
    DelPdf.setMinimumSize(QSize(40, 40))
    DelPdf.setMaximumSize(QSize(40, 40))
    DelPdf.setStyleSheet(u"background-color: rgb(85, 85, 127);")
    icon1 = QIcon()
    icon1.addFile(u"icons/cil-trash.png", QSize(), QIcon.Normal, QIcon.Off)
    DelPdf.setIcon(icon1)

    wrapperLayout.addWidget(DelPdf)
    print("zwracam")
    return wrapper

class CategoryAdder:
    def __init__(self, window):
        self.added_categories = []
        self.competitors_list = []
        self.to_add = []
        self.window = window

    def add_category(self):
        files = QFileDialog.getOpenFileNames(self.window, "Dodaj kategorię", os.getcwd(), "Plik PDF (*.pdf)")
        self.to_add = files[0]
        self.window.ui.CategoriesToAdd.setText(str(files[0]))

    def confirm_categories(self):
        print("tuaj")
        self.window.ui.CategoriesToAdd.setText("")

        for i in range(10):
            new_repr = create_pdf_repr(self.window.ui.AddedCategoriesContents,str(i))
            new_repr.setObjectName(str(i)+"pdf")
            self.window.ui.verticalLayout_93.addWidget(new_repr)
            new_repr.show()
