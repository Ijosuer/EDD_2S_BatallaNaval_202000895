import sys
import os


import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2/Client/views/')
#Importo la Clase

from admin_template import *
# from callme import login
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets

CPATH='/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2/Client/images'
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
        self.ui.bt_inicio.clicked.connect(lambda: self.tableData())			
        self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))

        #control barra de titulos
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(lambda: self.control_bt_maximizar() )
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())

        self.ui.bt_restaurar.hide()

        #menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)

    def control_bt_minimizar(self):
        self.showMinimized()		

    def  control_bt_normal(self): 
        self.showNormal()		
        self.ui.bt_restaurar.hide()
        self.ui.bt_maximizar.show()

    def  control_bt_maximizar(self): 
        self.showMaximized()
        print('entra')
        self.ui.bt_maximizar.hide()
        self.ui.bt_restaurar.show()

    def mover_menu(self):
        self.ui.tableWidget.clear()
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
    def getImage(self):
        imagelabel = QtWidgets.QLabel(self.ui.centralwidget)
        imagelabel.setText("")
        imagelabel.setScaledContents(True)
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData("3","png")
    def tableData(self):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle(" ")
        dlg.setText("F no le diste xd")
        dlg.exec_()
        users = [{"ID":'1',"name":"josue","coins":'20',"age":"20"},{"ID":'2',"name":"mike","coins":'0',"age":"15"},{"ID":'3',"name":"dan","coins":'60',"age":CPATH+"/chip.png"}]
        row = 0
        icon = QIcon()
        icon.addFile(CPATH+"/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        imagen= QTableWidgetItem()
        imagen.setIcon(icon)
        self.ui.tableWidget.setRowCount(len(users))
        for i in users:
            self.ui.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i["ID"]))
            self.ui.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i["name"]))
            self.ui.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(imagen))
            row+=1
        
if __name__ == "__main__":
    # inicio() 
    
    app = QApplication(sys.argv)
    mi_app = inicio()
    mi_app.show()
    sys.exit(app.exec_())	
  
#   login.startLogin()

