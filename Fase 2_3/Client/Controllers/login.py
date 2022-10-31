import sys
import time
import requests
import sys
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
from  login_template import *
from game import inicio
from admin import admin
menu = inicio
base_url = "http://localhost:5000"
class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindow = inicio()
        self.adminWindow = admin()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id = ''
        self.pwd = ''
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setMaximumSize(800,700)
        # 
        self.setAttribute(Qt.WA_TranslucentBackground)
        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        self.ui.bt_ingresar.clicked.connect(lambda: self.getPWD())			
        self.mainWindow.ui.bt_cerrar.clicked.connect(lambda: self.callm())
        self.adminWindow.ui.bt_cerrar.clicked.connect(lambda: self.callm())

    def callm(self):
        if self.isHidden():
            self.show()
            self.mainWindow.destroy()
            self.adminWindow.destroy()
    
    def getPWD(self):
        text = self.ui.users.text()
        text2 = self.ui.password.text()
        # login
        login = {'nick': text,'password':text2}
        x = requests.get(f'{base_url}/login', json = login)
        # print(x.text)
        if (x.status_code == 200): 
            user = x.json()
            for i in range(0,99):
                time.sleep(0.01)
                self.ui.progressBar.setValue(i)
                self.ui.cargando.setText('Cargando...')
            if self.isVisible():        
                self.hide()
                self.mainWindow.coins = int(user['monedas'])
                self.mainWindow.pwdUser = text2
                self.mainWindow.nameUser = str(user['nick'])
                self.mainWindow.idUser = str(user['id'])
                self.mainWindow.show()
        elif text == "admin" and text2 == "admin":
            for i in range(0,99):
                time.sleep(0.01)
                self.ui.progressBar.setValue(i)
                self.ui.cargando.setText('Cargando...')
            if self.isVisible():        
                self.hide()
                self.adminWindow.objeto = self.mainWindow.blockchain
                self.adminWindow.show()
        else:
            self.ui.usuario_incorrecto.setText('ERROR EN USUARIO')
            self.ui.contrasena_incorrecta.setText('ERROR EN PWD')

    def strartLogin():
        app = QApplication(sys.argv)
        mi_app = login()
        mi_app.show()
        sys.exit(app.exec_())	

if __name__ == "__main__":
    login.strartLogin()