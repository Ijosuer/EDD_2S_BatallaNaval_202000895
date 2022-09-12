import sys
from PyQt5 import QtWidgets, uic
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets

from  login_template import *
from sistema import inicio
menu = inicio

class login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.other = inicio()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        #eliminar barra y de titulo - opacidad
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        self.ui.pushButton.clicked.connect(lambda: self.getPWD())			
        self.other.ui.bt_cerrar.clicked.connect(lambda: self.callm())

    def callm(self):
         if self.isHidden():
                self.show()
                self.other.destroy()

    def getPWD(self):
        text = self.ui.lineEdit.text()
        text2 = self.ui.lineEdit_2.text()
        if (text == '' and text2 == ''): 
            if self.isVisible():
                print('entra')
                self.hide()
                self.other.show()
                if(self.other.ui.bt_inicio):
                    print('BR INICIO')
        else:
            print("F")

    def strartLogin():
        app = QApplication(sys.argv)
        mi_app = login()
        mi_app.show()
        sys.exit(app.exec_())	

if __name__ == "__main__":
    login.strartLogin()