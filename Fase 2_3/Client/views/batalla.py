# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batalla.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
CPATH='/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/images'
PATH='/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos'

class NewGameForm(object):
    def setupUi(self, NewBookWindow):
        if not NewBookWindow.objectName():
            NewBookWindow.setObjectName(u"NewBookWindow")
        NewBookWindow.resize(822, 591)
        NewBookWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.stackedWidget = QStackedWidget(NewBookWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 826, 596))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.pushButton_8 = QPushButton(self.page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.gridLayout.addWidget(self.pushButton_8, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1163, 1055))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        # self.label_4.setPixmap(QPixmap(PATH+"/dispersa2.png"))
        self.label_4.setPixmap(QPixmap(PATH+"/dispersa.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 4)

        self.lineEditY = QLineEdit(self.page)
        self.lineEditY.setObjectName(u"lineEditY")

        self.gridLayout.addWidget(self.lineEditY, 2, 3, 1, 1)

        self.pushButton_9 = QPushButton(self.page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.gridLayout.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.bt_Disparo = QPushButton(self.page)
        self.bt_Disparo.setObjectName(u"bt_Disparo")
        self.bt_Disparo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(228, 73, 73, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        icon = QIcon()
        icon.addFile(CPATH+"/shoot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Disparo.setIcon(icon)

        self.gridLayout.addWidget(self.bt_Disparo, 3, 0, 1, 4)

        self.lineEditX = QLineEdit(self.page)
        self.lineEditX.setObjectName(u"lineEditX")

        self.gridLayout.addWidget(self.lineEditX, 2, 1, 1, 1)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 11pt \"Noto Serif Khmer\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 85, 0);")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page)

        self.retranslateUi(NewBookWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(NewBookWindow)
    # setupUi

    def retranslateUi(self, NewBookWindow):
        NewBookWindow.setWindowTitle(QCoreApplication.translate("NewBookWindow", u"Nuevo Libro", None))
        self.pushButton_8.setText(QCoreApplication.translate("NewBookWindow", u"X", None))
        self.label_4.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("NewBookWindow", u"Y", None))
        self.bt_Disparo.setText(QCoreApplication.translate("NewBookWindow", u"DISPARAR", None))
        self.lineEditX.setPlaceholderText(QCoreApplication.translate("NewBookWindow", u"Ingrese posicion en X", None))
        self.lineEditY.setPlaceholderText(QCoreApplication.translate("NewBookWindow", u"Ingrese posicion en Y", None))
        self.label.setText(QCoreApplication.translate("NewBookWindow", u"   JUGADOR 2v2   ", None))
    # retranslateUi

