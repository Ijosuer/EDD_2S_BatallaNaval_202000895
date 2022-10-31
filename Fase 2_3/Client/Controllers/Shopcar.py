from datetime import datetime
from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from PySide2 import QtCore, QtGui, QtWidgets
from shoplist import *
import PrivateKey
import requests
import os
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/src/')
from Thash import Hash
from Merkle import Merkle

base_url = "http://localhost:5000"

hashito = Hash(13,20,80)

class NewCarListWindow(QWidget, Ui_NewBookWindow):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.window1 = PrivateKey.NewKeyWindow(self)
        self.iduser = self.parent.idUser
        self.nickuser = self.parent.nameUser
        self.pwduser = self.parent.pwdUser
        # self.parent.blockchain.inser
        self.setWindowFlag(Qt.Window)
        self.addButton.clicked.connect(lambda:self.toogle(self.window1))

    def toogle(self,window):
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def pagar(self):
        self.merkle = Merkle()
        date = datetime.now()
        if (self.window1.flag == True):
            for row in range(self.tableWidget.rowCount()):
                id = self.tableWidget.item(row, 0)
                name = self.tableWidget.item(row, 1)
                hashito.insert(int(id.text()+self.iduser),name.text())
                self.parent.total = 0
                self.parent.cantidad = 0
                self.parent.ui.btnCarrito.setText('0')
                self.parent.ui.label_Total.setText('Total    0')
                texto = str(id.text())+str(name.text())+str(date)
                self.merkle.add(texto)
            hashito.grafica()
            self.merkle.auth()
            self.parent.rowshop=0
            self.parent.blockchain.data = id.text()+name.text()
            self.parent.blockchain.rootMerkle = self.merkle.tophash.hash
            self.parent.blockchain.writeBlock()
            self.parent.blockchain.graficar()
            self.merkle.graficar()
        else:
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText(">ERROR EN LA COMPRA<")
            dlg.exec_()