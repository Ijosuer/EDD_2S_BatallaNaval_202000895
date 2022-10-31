# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_template.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 554)
        MainWindow.setMinimumSize(QSize(400, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 35))
        self.frame_superior.setMaximumSize(QSize(16777215, 50))
        self.frame_superior.setStyleSheet(u"\n"
"QFrame{\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"background-color: #245663 ;\n"
"\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 0, 2, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(200, 0))
        self.bt_menu.setMaximumSize(QSize(200, 16777215))
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"background-color: #245663 ;\n"
"font: 87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 12pt \"Arial Black\";\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(CPATH+"/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))
        self.bt_menu.setAutoDefault(False)
        self.bt_menu.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_menu, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(265, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMinimumSize(QSize(35, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#ffff00;\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(CPATH+"/minimizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QSize(32, 32))
        self.bt_minimizar.setFlat(False)

        self.horizontalLayout_8.addWidget(self.bt_minimizar, 0, Qt.AlignRight)

        self.bt_restaurar = QPushButton(self.frame_superior)
        self.bt_restaurar.setObjectName(u"bt_restaurar")
        self.bt_restaurar.setMaximumSize(QSize(35, 35))
        self.bt_restaurar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(CPATH+"/restaurar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_restaurar.setIcon(icon2)
        self.bt_restaurar.setIconSize(QSize(30, 30))

        self.horizontalLayout_8.addWidget(self.bt_restaurar, 0, Qt.AlignRight)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMaximumSize(QSize(35, 35))
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:#55ff00;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(CPATH+"/maximizar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon3)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_maximizar, 0, Qt.AlignRight)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(35, 16777215))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"background-color:red;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(CPATH+"/cerrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon4)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.bt_cerrar, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(200, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setLayoutDirection(Qt.LeftToRight)
        self.frame_lateral.setAutoFillBackground(False)
        self.frame_lateral.setStyleSheet(u"\n"
"QFrame{\n"
"background-color: #245663 ;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"background-color:  #245663 ;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 12pt \"Arial Narrow\";\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 9)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        self.bt_inicio.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bt_inicio.setLayoutDirection(Qt.LeftToRight)
        self.bt_inicio.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(CPATH+"/inteligencia-artificial.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon5)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_inicio)

        self.bt_uno = QPushButton(self.frame_lateral)
        self.bt_uno.setObjectName(u"bt_uno")
        self.bt_uno.setMinimumSize(QSize(0, 40))
        self.bt_uno.setToolTipDuration(0)
        self.bt_uno.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(CPATH+"/base-de-datos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_uno.setIcon(icon6)
        self.bt_uno.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_uno)

        self.bt_dos = QPushButton(self.frame_lateral)
        self.bt_dos.setObjectName(u"bt_dos")
        self.bt_dos.setMinimumSize(QSize(0, 40))
        self.bt_dos.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(CPATH+"/chip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_dos.setIcon(icon7)
        self.bt_dos.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_dos)

        self.bt_tres = QPushButton(self.frame_lateral)
        self.bt_tres.setObjectName(u"bt_tres")
        self.bt_tres.setMinimumSize(QSize(0, 40))
        self.bt_tres.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(CPATH+"/moto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_tres.setIcon(icon8)
        self.bt_tres.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_tres)

        self.bt_cuatro = QPushButton(self.frame_lateral)
        self.bt_cuatro.setObjectName(u"bt_cuatro")
        self.bt_cuatro.setMinimumSize(QSize(0, 40))
        self.bt_cuatro.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(CPATH+"/encriptado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cuatro.setIcon(icon9)
        self.bt_cuatro.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cuatro)

        self.bt_cinco = QPushButton(self.frame_lateral)
        self.bt_cinco.setObjectName(u"bt_cinco")
        self.bt_cinco.setMinimumSize(QSize(0, 40))
        self.bt_cinco.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(CPATH+"/videojuego.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cinco.setIcon(icon10)
        self.bt_cinco.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cinco)

        self.bt_seis = QPushButton(self.frame_lateral)
        self.bt_seis.setObjectName(u"bt_seis")
        self.bt_seis.setMinimumSize(QSize(0, 40))
        self.bt_seis.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon14 = QIcon()
        icon14.addFile(CPATH+"/videojuego.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_seis.setIcon(icon14)
        self.bt_seis.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_seis)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_2 = QLabel(self.frame_lateral)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(135, 135, 135);\n"
"font: 16pt \"Pristina\";")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_lateral, 0, Qt.AlignLeft)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setStyleSheet(u"")
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.frame_contenedor.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.stackedWidget.setLineWidth(0)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"images/imagen_dos.png"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(0)

        self.verticalLayout_9.addWidget(self.label)

        self.stackedWidget.addWidget(self.page)
        self.page_uno = QWidget()
        self.page_uno.setObjectName(u"page_uno")
        self.page_uno.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.page_uno)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 200, 121, 16))
        self.pwdLineEdit = QLineEdit(self.page_uno)
        self.pwdLineEdit.setObjectName(u"pwdLineEdit")
        self.pwdLineEdit.setGeometry(QRect(140, 220, 271, 20))
        self.cancelButton = QPushButton(self.page_uno)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(290, 330, 101, 31))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        self.cancelButton.setIconSize(QSize(30, 30))
        self.cancelButton.setFlat(True)
        self.label_7 = QLabel(self.page_uno)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 100, 131, 16))
        self.addButton = QPushButton(self.page_uno)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(184, 330, 101, 31))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"../images/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addButton.setIcon(icon11)
        self.addButton.setIconSize(QSize(30, 30))
        self.addButton.setFlat(True)
        self.label_8 = QLabel(self.page_uno)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(120, 60, 381, 20))
        self.label_8.setFrameShape(QFrame.Box)
        self.edadLineEdit = QLineEdit(self.page_uno)
        self.edadLineEdit.setObjectName(u"edadLineEdit")
        self.edadLineEdit.setGeometry(QRect(140, 280, 191, 20))
        self.oldnickLineEdit = QLineEdit(self.page_uno)
        self.oldnickLineEdit.setObjectName(u"oldnickLineEdit")
        self.oldnickLineEdit.setGeometry(QRect(140, 120, 351, 20))
        self.label_10 = QLabel(self.page_uno)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 260, 121, 16))
        self.label_9 = QLabel(self.page_uno)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 150, 121, 16))
        self.newnickLineEdit = QLineEdit(self.page_uno)
        self.newnickLineEdit.setObjectName(u"newnickLineEdit")
        self.newnickLineEdit.setGeometry(QRect(140, 170, 351, 20))
        self.stackedWidget.addWidget(self.page_uno)
        self.page_dos = QWidget()
        self.page_dos.setObjectName(u"page_dos")
        self.page_dos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget = QTableWidget(self.page_dos)
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
        self.tableWidget.setGeometry(QRect(10, 80, 631, 431))
        self.label_13 = QLabel(self.page_dos)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(50, 10, 100, 15))
        self.comprarlineEdit = QLineEdit(self.page_dos)
        self.comprarlineEdit.setObjectName(u"comprarlineEdit")
        self.comprarlineEdit.setGeometry(QRect(40, 30, 113, 23))
        self.bt_comprar = QPushButton(self.page_dos)
        self.bt_comprar.setObjectName(u"bt_comprar")
        self.bt_comprar.setGeometry(QRect(155, 20, 100, 26))
        self.bt_comprar.setStyleSheet(u"font: 57 italic 9pt \"Fira Sans Medium\";")
        icon12 = QIcon()
        icon12.addFile(CPATH+"/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_comprar.setIcon(icon12)
        self.bt_comprar.setIconSize(QSize(20, 20))
        self.bt_comprar.setFlat(True)
        self.label_14 = QLabel(self.page_dos)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(270, 20, 161, 20))
        self.label_coins = QLabel(self.page_dos)
        self.label_coins.setObjectName(u"label_coins")
        self.label_coins.setGeometry(QRect(340, 40, 57, 15))
        self.label_coins.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.btnCarrito = QPushButton(self.page_dos)
        self.btnCarrito.setObjectName(u"pushButton")
        self.btnCarrito.setGeometry(QRect(450, 20, 51, 31))
        self.btnCarrito.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 0, 89);\n"
"font: 12pt \"Noto Sans Carian\";")
        icon13 = QIcon()
        icon13.addFile(CPATH+"/carrito-de-compras.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCarrito.setIcon(icon13)
        self.btnCarrito.setIconSize(QSize(28, 25))
        self.label_Total = QLabel(self.page_dos)
        self.label_Total.setObjectName(u"pushButton_4")
        self.label_Total.setGeometry(QRect(520, 20, 101, 31))
        self.label_Total.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(59, 0, 89);\n"
"font: 11pt \"Noto Sans Carian\";")
        self.label_Total.setAlignment(Qt.AlignCenter)


        self.stackedWidget.addWidget(self.page_dos)
        self.page_tres = QWidget()
        self.page_tres.setObjectName(u"page_tres")
        self.verticalLayout_6 = QVBoxLayout(self.page_tres)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.scrollArea_3 = QScrollArea(self.page_tres)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 2591, 1235))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(PATH+"/AVL.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea_3)

        self.pushButton_3 = QPushButton(self.page_tres)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: rgb(255, 255, 0);\n"
"font: 87 18pt \"Arial Black\";")

        self.verticalLayout_6.addWidget(self.pushButton_3)

        self.stackedWidget.addWidget(self.page_tres)
        self.page_cuatro = QWidget()
        self.page_cuatro.setObjectName(u"page_cuatro")
        self.page_cuatro.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_4 = QGridLayout(self.page_cuatro)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_2 = QScrollArea(self.page_cuatro)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 971, 863))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(PATH+"/dispersa.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.page_cuatro)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(85, 255, 0);\n"
"font: 87 18pt \"Arial Black\";")

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_cuatro)
        self.page_cinco = QWidget()
        self.page_cinco.setObjectName(u"page_cinco")
        self.page_cinco.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.page_cinco)
        self.gridLayout.setObjectName(u"gridLayout")
        self.bt_tamanio = QPushButton(self.page_cinco)
        self.bt_tamanio.setObjectName(u"bt_tamanio")
        self.bt_tamanio.setStyleSheet(u"background-color: rgb(194, 194, 194);\n"
"font: 63 9pt \"Noto Serif CJK KR SemiBold\";")

        self.gridLayout.addWidget(self.bt_tamanio, 0, 0, 1, 1)

        self.sizeLineEdit = QLineEdit(self.page_cinco)
        self.sizeLineEdit.setObjectName(u"sizeLineEdit")

        self.gridLayout.addWidget(self.sizeLineEdit, 0, 1, 1, 1)

        self.label_vidas = QLabel(self.page_cinco)
        self.label_vidas.setObjectName(u"label_vidas")

        self.gridLayout.addWidget(self.label_vidas, 0, 2, 1, 2)

        self.label_tokens = QLabel(self.page_cinco)
        self.label_tokens.setObjectName(u"label_tokens")

        self.gridLayout.addWidget(self.label_tokens, 0, 4, 1, 2)

        self.scrollArea = QScrollArea(self.page_cinco)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 971, 863))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(PATH+"/dispersa.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 6)

        self.bt_x = QPushButton(self.page_cinco)
        self.bt_x.setObjectName(u"bt_x")
        self.bt_x.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.gridLayout.addWidget(self.bt_x, 2, 0, 1, 1)

        self.lineEdit_x = QLineEdit(self.page_cinco)
        self.lineEdit_x.setObjectName(u"lineEdit_x")

        self.gridLayout.addWidget(self.lineEdit_x, 2, 1, 1, 2)

        self.bt_y = QPushButton(self.page_cinco)
        self.bt_y.setObjectName(u"bt_y")
        self.bt_y.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.gridLayout.addWidget(self.bt_y, 2, 3, 1, 2)

        self.lineEdit_y = QLineEdit(self.page_cinco)
        self.lineEdit_y.setObjectName(u"lineEdit_y")

        self.gridLayout.addWidget(self.lineEdit_y, 2, 5, 1, 1)

        self.bt_Disparo = QPushButton(self.page_cinco)
        self.bt_Disparo.setObjectName(u"bt_Disparo")
        self.bt_Disparo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(228, 73, 73, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        icon13 = QIcon()
        icon13.addFile(CPATH+"/shoot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Disparo.setIcon(icon13)

        self.gridLayout.addWidget(self.bt_Disparo, 3, 0, 1, 6)

        self.stackedWidget.addWidget(self.page_cinco)
# Agregamos la pagina seis de PVP
        self.page_seis = QWidget()
        self.page_seis.setObjectName(u"page_seis")
        self.page_seis.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_6 = QGridLayout(self.page_seis)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.bt_y2 = QPushButton(self.page_seis)
        self.bt_y2.setObjectName(u"bt_y2")
        self.bt_y2.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.gridLayout_6.addWidget(self.bt_y2, 2, 3, 1, 2)

        self.lineEdit_y2 = QLineEdit(self.page_seis)
        self.lineEdit_y2.setObjectName(u"lineEdit_y2")

        self.gridLayout_6.addWidget(self.lineEdit_y2, 2, 5, 1, 1)

        self.bt_Disparo2 = QPushButton(self.page_seis)
        self.bt_Disparo2.setObjectName(u"bt_Disparo2")
        self.bt_Disparo2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(228, 73, 73, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        icon14 = QIcon()
        icon14.addFile(CPATH+"/shoot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Disparo2.setIcon(icon14)

        self.gridLayout_6.addWidget(self.bt_Disparo2, 3, 0, 1, 6)

        self.scrollArea_4 = QScrollArea(self.page_seis)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_1 = QWidget()
        self.scrollAreaWidgetContents_1.setObjectName(u"scrollAreaWidgetContents_1")
        self.scrollAreaWidgetContents_1.setGeometry(QRect(0, 0, 4139, 3455))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_1)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_11 = QLabel(self.scrollAreaWidgetContents_1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(PATH+"/dispersa.png"))
        self.label_11.setScaledContents(True)

        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_1)

        self.gridLayout_6.addWidget(self.scrollArea_4, 1, 0, 1, 6)

        self.bt_x2 = QPushButton(self.page_seis)
        self.bt_x2.setObjectName(u"bt_x")
        self.bt_x2.setStyleSheet(u"background-color: rgb(170, 170, 127);")

        self.gridLayout_6.addWidget(self.bt_x2, 2, 0, 1, 1)

        self.lineEdit_x2 = QLineEdit(self.page_seis)
        self.lineEdit_x2.setObjectName(u"lineEdit_x2")

        self.gridLayout_6.addWidget(self.lineEdit_x2, 2, 1, 1, 2)

        self.sizeLineEdit2 = QLineEdit(self.page_seis)
        self.sizeLineEdit2.setObjectName(u"sizeLineEdit2")

        self.gridLayout_6.addWidget(self.sizeLineEdit2, 0, 1, 1, 1)

        self.bt_tamanio2 = QPushButton(self.page_seis)
        self.bt_tamanio2.setObjectName(u"bt_tamanio2")
        self.bt_tamanio2.setStyleSheet(u"background-color: rgb(194, 194, 194);\n"
"font: 63 9pt \"Noto Serif CJK KR SemiBold\";")

        self.gridLayout_6.addWidget(self.bt_tamanio2, 0, 0, 1, 1)

        self.combo = QComboBox(self.page_seis)
        self.combo.setObjectName(u"bt_combo")

        self.gridLayout_6.addWidget(self.combo, 0, 5, 1, 1)

        self.stackedWidget.addWidget(self.page_seis)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.bt_menu.setDefault(False)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"    MENU ", None))
        self.bt_minimizar.setText("")
        self.bt_restaurar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
        self.bt_inicio.setText(QCoreApplication.translate("MainWindow", u"       INICIO             ", None))
        self.bt_uno.setText(QCoreApplication.translate("MainWindow", u"EDITAR USUARIO", None))
        self.bt_dos.setText(QCoreApplication.translate("MainWindow", u"TIENDA", None))
        self.bt_tres.setText(QCoreApplication.translate("MainWindow", u"    VER SKINS", None))
        self.bt_cuatro.setText(QCoreApplication.translate("MainWindow", u"TUTORIAL", None))
        self.bt_cinco.setText(QCoreApplication.translate("MainWindow", u"JUGAR", None))
        self.bt_seis.setText(QCoreApplication.translate("MainWindow", u" PVP ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"By: iJosuer", None))
        self.label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Nueva Password</span></p></body></html>", None))
        self.cancelButton.setText(QCoreApplication.translate("MainWindow", u"CANCELAR", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Antiguo Nickname</span></p><p><br/></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">EDITAR USUARIO</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Nueva Edad</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Nuevo Nickname</span></p><p><br/></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Imagen", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Ingrese ID</span></p></body></html>", None))
        self.bt_comprar.setText(QCoreApplication.translate("MainWindow", u" comprar", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; font-style:italic;\">Monedas disponibles</span></p></body></html>", None))
        self.label_coins.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_Total.setText(QCoreApplication.translate("MainWindow", u"Total   0", None))
        self.btnCarrito.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Ver barcos", None))
        self.label_4.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PRESIONA PARA AVANZAR", None))
        self.bt_tamanio.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None))
        self.sizeLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese tama\u00f1o del tablero", None))
        self.label_vidas.setText(QCoreApplication.translate("MainWindow", u"3 VIDAS", None))
        self.label_tokens.setText(QCoreApplication.translate("MainWindow", u"TOKENS ->", None))
        self.label_5.setText("")
        self.bt_x.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_x.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese posicion en X", None))
        self.bt_y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.lineEdit_y.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese posicion en Y", None))
        self.bt_Disparo.setText(QCoreApplication.translate("MainWindow", u"DISPARAR", None))
        
        self.bt_Disparo2.setText(QCoreApplication.translate("MainWindow", u"DISPARAR", None))
        self.bt_x2.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.bt_y2.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.bt_tamanio2.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None))
        self.sizeLineEdit2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese tama\u00f1o del tablero", None))
        self.lineEdit_y2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese posicion en Y", None))
        self.lineEdit_x2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese posicion en X", None))
    # retranslateUi

