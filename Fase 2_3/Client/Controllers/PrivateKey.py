from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from PySide2 import QtCore, QtGui, QtWidgets
from keyWindow import *
import os
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/src/')
# from Thash import Hash
# hashito = Hash(13,20,80)

class NewKeyWindow(QWidget, Ui_KeyWindow):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.flag = False
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.bt_pass.clicked.connect(lambda:self.pagar())

    def pagar(self):
      pwd = self.lineEdit.text()
      if(pwd == self.parent.pwduser):
        self.flag = True
        self.hide()
        self.parent.pagar()
      else:
        print('error')
