from asyncio import sleep
import sys
import os
import time
import requests
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/src/')

from game_template2 import *
from Matriz_Dispersa import Matriz
import otherPlayer
import Shopcar
# from batalla import *

from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation
from PySide2 import QtCore, QtGui, QtWidgets

CPATH='/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client'
PATH = '/home/ijosuer/images'
GPATH = '/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos'

base_url = "http://localhost:5000"

class inicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.coins = 0
        self.vidas = 3
        self.name = ''
        # self.matriz = None
        self.matriz =None
        self.matriz2v2 = None
        self.listaAdy = None
        self.len = 10
        self.tutlen = 0
        self.barcos2v2 = 0
        self.window1 = otherPlayer.NewGameWindow(self)
        self.window2 = Shopcar.NewCarListWindow(self)
        self.dic = {'P':0,'S':0,'D':0,'B':0}
        self.S = 0		
        self.D = 0		
        self.B = 0		
        self.P = 0	
        # window1.disparo()
        self.ui.label_coins.setText(str(self.vidas)+" VIDAS")
        
        
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
        self.ui.bt_uno.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_uno))
        self.ui.bt_dos.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_dos))	
        self.ui.bt_dos.clicked.connect(lambda: self.tableData())	
        self.ui.bt_tres.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tres))
        self.ui.pushButton_3.clicked.connect(lambda: self.verGrafica())

        self.ui.bt_cuatro.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cuatro))			
        self.ui.bt_cinco.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_cinco))
        self.ui.bt_seis.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_seis))
        self.ui.bt_seis.clicked.connect(lambda: self.toggle_window(self.window1))

        self.ui.btnCarrito.clicked.connect(lambda: self.toggle_shoplist(self.window2))
        
        #control barra de titulos
        self.ui.bt_minimizar.clicked.connect(self.control_bt_minimizar)		
        self.ui.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.ui.bt_maximizar.clicked.connect(lambda: self.control_bt_maximizar() )
        self.ui.bt_cerrar.clicked.connect(lambda: self.close())
        self.ui.bt_restaurar.hide()
        #menu lateral
        self.ui.bt_menu.clicked.connect(self.mover_menu)
        
        # --PETICIONES--
        # Boton comprar ID 
        self.ui.bt_comprar.clicked.connect(self.comprarBarco)

        # ---->JUGAR<---
        self.ui.bt_tamanio.clicked.connect(self.generarRandom)
        self.ui.bt_tamanio2.clicked.connect(self.generarRandom2v2)
        self.ui.bt_Disparo.clicked.connect(self.getDisparo)
        self.ui.bt_Disparo2.clicked.connect(self.sendDisparo)


        # EDITAR USUARIO
        self.ui.addButton.clicked.connect(self.editarUser)

        #tutorial
        self.ui.pushButton_2.clicked.connect(self.tutorialR)

    def tutorialR(self):
        pass

    #     self.matriz = Matriz(0)
    #     self.matriz.generarMatrizRandom(num)
    #     for j in x.json():
    #         if(self.vidas ==0):
    #             dlg = QtWidgets.QMessageBox(self)
    #             dlg.setWindowTitle(" ")
    #             dlg.setText(":( HAS PERDIDO !")
    #             dlg.exec_()
    #             break
    #         x = j['x']
    #         y = j['y']
    #         if (int(x)>num or int(y)>num ):
    #             dlg = QtWidgets.QMessageBox(self)
    #             dlg.setWindowTitle(" ")
    #             dlg.setText("INGRESE VALORES CORRECTOS!")
    #             dlg.exec_()
    #             sleep(1)
    #         elif (int(x)<1 or int(y)<1):
    #             dlg = QtWidgets.QMessageBox(self)
    #             dlg.setWindowTitle(" ")
    #             dlg.setText("INGRESE VALORES CORRECTOS!")
    #             dlg.exec_()
    #             sleep(1)
    #         else:
    #             ans = self.matriz.ubicarCoordenada(int(x),int(y))
    #             if(ans == None): 
    #                 self.vidas -=1
    #                 self.matriz.insert(int(x),int(y)," ")
    #                 self.matriz.graficarDibujo("dispersa","BATTLE SHIP")
    #                 self.ui.label_4.setPixmap(QtGui.QPixmap(GPATH+"/dispersa.png")) 
    #                 sleep(1)
    #             else:
    #                 dlg = QtWidgets.QMessageBox(self)
    #                 dlg.setWindowTitle(" ")
    #                 dlg.setText("DISPARO!")
    #                 ans.caracter = "F"
    #                 dlg.exec_()
    #                 self.matriz.graficarDibujo("dispersa","BATTLE SHIP")
    #                 self.ui.label_4.setPixmap(QtGui.QPixmap(GPATH+"/dispersa.png")) 
    #                 sleep(1)
    def ganador(self):
        self.listaAdy = self.window1.matriz2
        self.listaAdy.self = self.listaAdy
        self.listaAdy.listaAdyacencia = Matriz(0)
        self.listaAdy.recorridoPorFila(1,"Josuep")
        self.listaAdy.crearGrafo("ganador","Lista de\nAdyacencia")
        self.toggle_window(self.window1)

    def grafica(self):
        self.matriz2v2.graficarDibujo("dispersa","BATTLE SHIP")
        self.ui.label_11.setPixmap(QtGui.QPixmap(GPATH+"/dispersa.png"))

    def editarUser(self):
        oldn = self.ui.oldnickLineEdit.text()
        newn = self.ui.newnickLineEdit.text()
        pwd = self.ui.pwdLineEdit.text()
        edad = self.ui.edadLineEdit.text()
        ans = {"old":oldn,"new":newn,"pwd":pwd,"edad":edad}
        # ans = {"id":id,"monedas":str(self.coins)}
        x = requests.post(f'{base_url}/editarUser',json=ans)
        if (x.status_code == 200):
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText("Tus datos se han cambiado "+newn+"! :D")
            dlg.exec_()
        else:
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText("OCURRIO UN ERROR")
            dlg.exec_()


    def sendDisparo(self):
        x = self.ui.lineEdit_x2.text()
        y = self.ui.lineEdit_y2.text()
        if (int(x) > self.len or int(y) > self.len or int(x) < 1 or int(y) < 1):
            print('error coordenada')
        else:
            ans = self.window1.matriz2.ubicarCoordenada(int(x),int(y))

            if (ans == None):
                self.window1.matriz2.insert(int(x),int(y)," ")
            else:
                if(ans.caracter == 'D'):
                    self.D +=1
                    if(self.D == 2):
                        self.dic['D']+=1
                        self.D = 0
                        self.barcos2v2-=1
                    ans.caracter = "F"
                    self.ventana('>> Disparo!!!')
                elif (ans.caracter == 'B'):
                    self.barcos2v2-=1
                    self.dic['B']+=1
                    self.B +=1
                    ans.caracter = "F"
                    self.ventana('>> Disparo!!!')
                elif (ans.caracter == 'S'):
                    self.S +=1
                    if(self.S == 3):
                        self.dic['S']+=1
                        self.barcos2v2-=1
                        self.S = 0
                    ans.caracter = "F"
                    self.ventana('>> Disparo!!!')
                elif (ans.caracter == 'P'):
                    self.P +=1
                    if(self.P == 4):
                        self.barcos2v2-=1
                        self.P = 0
                        self.dic['P']+=1
                    self.ventana('>> Disparo!!!')
                    ans.caracter = "F"
            self.window1.grafica()
            if(self.barcos2v2 == 8):#cambiar pendiente
                self.ventana('GANASTE LA PARTIDA!!!')
                self.ventana('HAS DESTRUIDO:\n'+str(self.dic['P'])+' PortaAviones\n'+str(self.dic['B'])+' Buques\n'+str(self.dic['D'])+' Destructores\n' +str(self.dic['S'])+' Subamarinos\n')
                self.ganador()

    def ventana(self, text):
        dlg = QtWidgets.QMessageBox(self)
        dlg.setWindowTitle(" ")
        dlg.setText(text)
        dlg.exec_()

    def getDisparo(self):
        if(self.vidas ==0):
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText(":( HAS PERDIDO !")
            dlg.exec_()
            self.close()
        x = self.ui.lineEdit_x.text()
        y = self.ui.lineEdit_y.text()
        print(self.len)
        if (int(x)>self.len or int(y)>self.len ):
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText("INGRESE VALORES CORRECTOS!")
            dlg.exec_()
        elif (int(x)<1 or int(y)<1):
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText("INGRESE VALORES CORRECTOS!")
            dlg.exec_()
        else:
            ans = self.matriz.ubicarCoordenada(int(x),int(y))
            if(ans == None):
                self.coins -= 20
                self.vidas -=1
                self.matriz.insert(int(x),int(y)," ")
                self.ui.label_tokens.setText("TOKENS -> "+str(self.coins))
                self.ui.label_coins.setText(str(self.vidas)+" VIDAS")
            else:
                self.coins += 20
                dlg = QtWidgets.QMessageBox(self)
                dlg.setWindowTitle(" ")
                dlg.setText("DISPARO!")
                ans.caracter = "F"
                dlg.exec_()
                self.ui.label_tokens.setText("TOKENS -> "+str(self.coins))


        self.matriz.graficarDibujo("dispersa","BATTLE SHIP")
        self.ui.label_5.setPixmap(QtGui.QPixmap(GPATH+"/dispersa.png"))

    def generarRandom(self):
        # from Matriz_Dispersa import Matriz
        self.matriz = Matriz(0)
        x = self.ui.sizeLineEdit.text()
        self.len = int(x)
        self.matriz.generarMatrizRandom(self.len)
        self.matriz.graficarDibujo("dispersa","BATTLE SHIP")
        self.ui.label_5.setPixmap(QtGui.QPixmap(GPATH+"/dispersa.png"))
    
    def generarRandom2v2(self):
        self.window1.label.setText('  '+self.ui.combo.currentText()+'  ') 
        self.matriz2v2 = Matriz(0)
        x = self.ui.sizeLineEdit2.text()
        self.len = int(x)
        self.window1.len = int(x)
        self.matriz2v2.generarMatrizRandom(self.len)
        self.matriz2v2.graficarDibujo("dispersa","BATTLE SHIP")
        self.ui.label_11.setPixmap(QtGui.QPixmap(GPATH+"/dispersa.png"))
        self.barcos2v2 = self.matriz2v2.total

        # LA OTRA MATRIZ
        self.window1.barcos2v2 = self.barcos2v2 
        self.window1.matriz2 = Matriz(0)
        self.window1.matriz2.generarMatrizRandom(self.len)
        self.window1.matriz2.graficarDibujo("dispersa2","BATTLE SHIP")
        self.window1.label_4.setPixmap(QtGui.QPixmap(GPATH+"/dispersa2.png"))


    def verGrafica(self):
        # print('entraasaaaa')
        x = requests.get(f'{base_url}/graficaAVL')
        if(x.status_code == 200):
            self.ui.label_3.setPixmap(QtGui.QPixmap(GPATH+"/AVL.png"))

    def comprarBarco(self):
        id = self.ui.comprarlineEdit.text()
        ans = {"id":id,"monedas":str(self.coins)}
        x = requests.post(f'{base_url}/comprarBarco',json=ans)
        

        if(x.status_code == 200):
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText("COMPRA REALIZADA!")
            dlg.exec_()
            a = x.json()
            self.coins = a['monedas']
            self.ui.label_coins.setText(str(self.coins))
        else:
            # self.ui.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("hi"))
            self.window2.tableWidget.setRowCount(5)
            self.window2.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("hi"))
            
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle(" ")
            dlg.setText("NO se puedo realizar la compra D:")
            dlg.exec_()
            
    def tableData(self):
        self.ui.label_coins.setText(str(self.coins))
        self.ui.label_tokens.setText("TOKENS -> "+str(self.coins))
        row = 0
        contador:int = 33

        users = requests.get(f'{base_url}/articulos')
        self.ui.tableWidget.setRowCount(len(users.json()))
        for i in users.json():
            # btn = QtWidgets.QPushButton()
            icon = QIcon()
            icon.addFile(i['src'], QSize(), QIcon.Normal, QIcon.Off)
            imagen= QTableWidgetItem()
            imagen.setIcon(icon)
            
            self.ui.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(i['id'])))
            self.ui.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i["nombre"]))
            self.ui.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i['categoria'])))
            self.ui.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(i['precio'])))
            self.ui.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(imagen))
            # self.ui.tableWidget.setCellWidget(row,5,(btn))
            row+=1
            contador+=1

    def getUsuarios(self):
        res = requests.get(f'{base_url}/usuarios') 
        data = res.json() #convertimos la respuesta en dict
        print(data)

    def addUsuario(self):
        usuario = {'nick': 'NUEVO ','password':'new','monedas':'45','edad':'56'}
        x = requests.post(f'{base_url}/guardar_usuario', json = usuario)
        print(x.text)
    

# --------------------------------------|
# --------------------------------------|
# --------------------------------------|
    def control_bt_minimizar(self):
        self.showMinimized()		

    def  control_bt_normal(self): 
        self.showNormal()		
        self.ui.bt_restaurar.hide()
        self.ui.bt_maximizar.show()

    def  control_bt_maximizar(self): 
        self.showMaximized()
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
    def toggle_window(self, window):
        self.ui.combo.addItem('Josue')
        self.ui.combo.addItem('Dan')
        self.ui.combo.addItem('Mike')
        self.ui.combo.addItem('Saul')
        
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def toggle_shoplist(self, window):
        
        if window.isVisible():
            window.hide()
        else:
            window.show()

    def startMenu(self):
        app2 = QApplication(sys.argv)
        mi_app2 = otherPlayer()
        mi_app2.show()
        sys.exit(app2.exec_())	

if __name__ == "__main__":
    # inicio() 
    app = QApplication(sys.argv)
    mi_app = inicio()
    mi_app.show()
    sys.exit(app.exec_())	
  
#   login.startLogin()

