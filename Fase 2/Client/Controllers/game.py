import sys
import os

import requests

#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2/Client/views/')
from game_template import *
# from menu import *
# from callme import login
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets

CPATH='/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2/Client'
base_url = "http://localhost:5000"
# loga = login

class inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #eliminar barra y de titulo - opacidad
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # mover ventana
        self.ui.frame_superior.mouseMoveEvent = self.mover_ventana

        #acceder a las paginas
        self.ui.bt_inicio.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))			
        self.ui.bt_inicio.clicked.connect(lambda: print('ola ola ola'))			
        self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
        self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))	
        self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))
        self.ui.bt_cuatro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuatro))			
        self.ui.bt_cinco.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cinco))

        #control barra de titulos
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(lambda: self.control_bt_maximizar() )
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())
        self.ui.bt_restaurar.hide()
        #menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)
        
        # --PETICIONES--
        # Boton pagina 1
        self.ui.bt_pagina1.clicked.connect(lambda: self.getUsuarios())
        # Boton pagina 2
        self.ui.bt_pagina2.clicked.connect(lambda: self.addUsuario())
        # Boton pagina 3
        self.ui.bt_pagina3.clicked.connect(lambda: self.deleteUsuario())

    def getUsuarios(self):
        res = requests.get(f'{base_url}/usuarios') 
        data = res.json() #convertimos la respuesta en dict
        print(data)

    def addUsuario(self):
        usuario = {'nick': 'NUEVO ','password':'new','monedas':'45','edad':'56'}
        x = requests.post(f'{base_url}/guardar_usuario', json = usuario)
        print(x.text)
    
    def deleteUsuario(self):
        x = requests.delete(f'{base_url}/eliminar_usuario', json = {'nick': 'josue','password':'jos'})
        print(x.status_code)

# --------------------------------------|
# --------------------------------------|
# --------------------------------------|
    def control_bt_minimizar(self):
        self.showMinimized()		

    def  control_bt_normal(self): 
        print('ESTE ES IUN BNOTON DE LA BARRA MAJE')
        self.showNormal()		
        self.ui.bt_restaurar.hide()
        self.ui.bt_maximizar.show()

    def  control_bt_maximizar(self): 
        self.showMaximized()
        print('entra')
        self.ui.bt_maximizar.hide()
        self.ui.bt_restaurar.show()

    def mover_menu(self):
        if True:			
            width = self.ui.frame_lateral.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.ui.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    ## SizeGrip
    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    ## mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()
        # sys.exit()
# -------------------------------------|
# -------------------------------------|
# -------------------------------------|
    def startMenu():
        app2 = QApplication(sys.argv)
        mi_app2 = inicio()
        mi_app2.show()
        sys.exit(app2.exec_())	

if __name__ == "__main__":
    # inicio() 
    app = QApplication(sys.argv)
    mi_app = inicio()
    mi_app.show()
    sys.exit(app.exec_())	
  
#   login.startLogin()

