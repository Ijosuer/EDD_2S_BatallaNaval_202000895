import sys
# import os
# import time

import requests

#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/src/')

from batalla import *
import game 
from Matriz_Dispersa import Matriz
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets

CPATH='/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client'
PATH = '/home/ijosuer/images'
GPATH = '/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos'

base_url = "http://localhost:5000"

class NewGameWindow(QWidget, NewGameForm):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        # self.ui = NewGameWindow()
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.matriz2 = None
        self.len = 0
        self.barcos2v2 = 0 
        self.bt_Disparo.clicked.connect(lambda: self.disparo())	
        self.S = 0		
        self.D = 0		
        self.B = 0		
        self.P = 0		

    def ventana(self, text):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle(" ")
        dlg.setText(text)
        dlg.exec_()

    def disparo(self):
        x = self.lineEditX.text()
        y = self.lineEditY.text()
        if (int(x) > self.len or int(y) > self.len or int(x) < 1 or int(y) < 1):
            print('error coordenada')
        else:
            ans = self.parent.matriz2v2.ubicarCoordenada(int(x),int(y))

            if (ans == None):
                self.parent.matriz2v2.insert(int(x),int(y)," ")
            else:
                if(ans.caracter == 'D'):
                    self.D +=1
                    if(self.D == 2):
                        self.D = 0
                        self.parent.barcos2v2-=1
                        self.ventana('D destruido pa xd')
                    ans.caracter = "F"
                elif (ans.caracter == 'B'):
                    self.parent.barcos2v2-=1
                    self.B +=1
                    ans.caracter = "F"
                elif (ans.caracter == 'S'):
                    self.S +=1
                    if(self.S == 3):
                        self.parent.barcos2v2-=1
                        self.S = 0
                        print('S destruido')
                    ans.caracter = "F"
                elif (ans.caracter == 'P'):
                    self.P +=1
                    if(self.P == 4):
                        self.parent.barcos2v2-=1
                        self.P = 0
                        print('P destruido')
                    ans.caracter = "F"
            self.parent.grafica()
            if(self.parent.barcos2v2 == 8):
                self.ventana('GANASTE CAPOOOOO')

    def disparoVs(self,x, y):
        ans = self.matriz2.ubicarCoordenada(int(x),int(y))
        if (ans == None):
            print('No le das ni a pipas')
        else:
            self.matriz2.insert(int(x),int(y),ans.caracter)
            print('NCCC PERRO')

        self.matriz2v2.graficarDibujo("dispersa","BATTLE SHIP")
        self.ui.label_11.setPixmap(QtGui.QPixmap(GPATH+"/dispersa.png"))

    def grafica(self):
        self.matriz2.graficarDibujo("dispersa2","BATTLE SHIP")
        self.label_4.setPixmap(QtGui.QPixmap(GPATH+"/dispersa2.png"))

# if __name__ == "__main__":
#     # inicio() 
#     app = QApplication(sys.argv)
#     mi_app = otherPlayer()
#     mi_app.show()
#     sys.exit(app.exec_())