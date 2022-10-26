# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shoplist.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewBookWindow(object):
    def setupUi(self, NewBookWindow):
        if not NewBookWindow.objectName():
            NewBookWindow.setObjectName(u"NewBookWindow")
        NewBookWindow.resize(552, 440)
        NewBookWindow.setCursor(QCursor(Qt.PointingHandCursor))
        NewBookWindow.setStyleSheet(u"background-color: rgb(223, 160, 0);")
        self.gridLayout_2 = QGridLayout(NewBookWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget = QWidget(NewBookWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"Noto Serif CJK KR\";")

        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"background-color: rgb(241, 241, 241);")

        self.verticalLayout.addWidget(self.tableWidget)

        self.addButton = QPushButton(self.widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
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
        self.addButton.setIcon(icon)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setFlat(True)

        self.verticalLayout.addWidget(self.addButton)

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


        self.retranslateUi(NewBookWindow)

        QMetaObject.connectSlotsByName(NewBookWindow)
    # setupUi

    def retranslateUi(self, NewBookWindow):
        NewBookWindow.setWindowTitle(QCoreApplication.translate("NewBookWindow", u"Carrito", None))
        self.label.setText(QCoreApplication.translate("NewBookWindow", u"LISTADO DE COMPRAS", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NewBookWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NewBookWindow", u"NAME", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NewBookWindow", u"PRICE", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NewBookWindow", u"IDK2", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NewBookWindow", u"IDK", None));
        self.addButton.setText(QCoreApplication.translate("NewBookWindow", u"PAGAR", None))
        self.cancelButton.setText(QCoreApplication.translate("NewBookWindow", u"CANCELAR", None))
    # retranslateUi

