from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from PySide2 import QtCore, QtGui, QtWidgets
from shoplist import *
import requests
import os
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
base_url = "http://localhost:5000"
class NewCarListWindow(QWidget, Ui_NewBookWindow):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.tableWidget.setItem(1,0,QtWidgets.QTableWidgetItem("sadf"))