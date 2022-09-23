# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_userDesing.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(433, 300)
        Form.setStyleSheet(u"background-color: rgb(51, 102, 153);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 30, 191, 21))
        self.label.setStyleSheet(u"font: 14pt \"Segoe MDL2 Assets\";\n"
"background-color: rgb(0, 63, 95);\n"
"color: rgb(255, 255, 255);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(100, 90, 235, 146))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 14pt \"Segoe MDL2 Assets\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 14pt \"Segoe MDL2 Assets\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 14pt \"Segoe MDL2 Assets\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_4, 2, 0, 2, 1)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 9pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 2, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 14pt \"Segoe MDL2 Assets\";\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 143, 214);")

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"REGISTRAR USUARIO", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"NICKNAME", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Ingrese nickname", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"MONEDAS", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Ingrese las monedas", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"PWD", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Ingrese PWD", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Ingrese edad", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"EDAD", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"CREAR", None))
    # retranslateUi
