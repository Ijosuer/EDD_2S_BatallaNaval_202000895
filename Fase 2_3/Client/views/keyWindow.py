# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_KeyWindow(object):
    def setupUi(self, KeyWindow):
        if not KeyWindow.objectName():
            KeyWindow.setObjectName(u"KeyWindow")
        KeyWindow.resize(300, 194)
        KeyWindow.setCursor(QCursor(Qt.PointingHandCursor))
        KeyWindow.setStyleSheet(u"background-color: rgb(255, 170, 127);")
        self.gridLayout_2 = QGridLayout(KeyWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(KeyWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Noto Serif CJK KR\";")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.lineEdit)

        self.bt_pass = QPushButton(self.widget)
        self.bt_pass.setObjectName(u"bt_pass")
        self.bt_pass.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_pass.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"	\n"
"background-color: rgb(116, 255, 2);\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_pass.setIcon(icon)
        self.bt_pass.setIconSize(QSize(30, 30))
        self.bt_pass.setFlat(True)

        self.verticalLayout.addWidget(self.bt_pass)

        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"	background-color: rgb(171, 0, 0);\n"
"	color:\"white\";\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setFlat(True)

        self.verticalLayout.addWidget(self.cancelButton)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(KeyWindow)

        QMetaObject.connectSlotsByName(KeyWindow)
    # setupUi

    def retranslateUi(self, KeyWindow):
        KeyWindow.setWindowTitle(QCoreApplication.translate("KeyWindow", u"Clave Privada", None))
        self.label.setText(QCoreApplication.translate("KeyWindow", u"Ingrese su clave privada", None))
        self.bt_pass.setText(QCoreApplication.translate("KeyWindow", u"SUBMIT", None))
        self.cancelButton.setText(QCoreApplication.translate("KeyWindow", u"CANCELAR", None))
    # retranslateUi

