import sys
import os
import requests

#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
#Importo la Clase

from new_admin import *
from new_user import NewBookWindow
# from callme import login
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets

CPATH='/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/images'
PATH='/home/ijosuer/images'
# loga = login
base_url = "http://localhost:5000"

class admin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)

        window1 = NewBookWindow(self)
        

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
        # self.ui.bt_shop.clicked.connect(lambda:print('yooo'))
        # self.ui.tableWidget.itemDoubleClicked.connect(lambda:print('MANITO'))
        self.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.cellDoubleClicked.connect(self.onSelection)
        # self.ui.tableWidget.selectionModel().selectionChanged.connect(self.onSelection)

        # self.ui.tableWidget.itemClicked.connect(lambda:print('MANITO'))
        #control barra de titulos
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(lambda: self.control_bt_maximizar() )
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())

        self.ui.bt_restaurar.hide()

        self.ui.bt_addUser.clicked.connect(lambda:self.openAdd(window1))

        #menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)

    def openAdd(self,window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
        

    def onSelection(self,row,column):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle(" ")
        dlg.buttonText(0)
        dlg.setButtonText(0,'YO')
        dlg.buttonText(1)
        # dlg.setStandardButtons(QtWidgets.QMessageBox.Ok )
        dlg.setButtonText(1,'NAA')
        dlg.setText("F no le diste xd")
        # btn = QtWidgets.QPushButton(dlg)
        dlg.exec_()

        print("Row %d and Column %d was clicked" % (row, column))
        item = self.ui.tableWidget.item(row, column)
        print(item.data(0))
        # for i in selected.indexes():
            # print('Selected Cell at row: {0}'.format(i.data()))

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
    
    def tableData(self):

        # dlg = QtWidgets.QMessageBox(self)
        # dlg.setWindowTitle(" ")
        # dlg.setText("F no le diste xd")
        # dlg.exec_()
        
        row = 0
        contador:int = 33

        users = requests.get(f'{base_url}/usuarios')
        self.ui.tableWidget.setRowCount(len(users.json()))
        for i in users.json():
            # btn = QtWidgets.QPushButton()
            icon = QIcon()
            icon.addFile(PATH+"/"+str(contador)+".png", QSize(), QIcon.Normal, QIcon.Off)
            imagen= QTableWidgetItem()
            imagen.setIcon(icon)

            self.ui.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(i['id'])))
            self.ui.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i["nick"]))
            self.ui.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i['monedas'])))
            self.ui.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(i['edad'])))
            # self.ui.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(imagen))
            row+=1
            contador+=1

if __name__ == "__main__":
    # inicio() 
    
    app = QApplication(sys.argv)
    mi_app = admin()
    mi_app.show()
    sys.exit(app.exec_())	
  
#   login.startLogin()

