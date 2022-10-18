from PySide2.QtWidgets import QWidget, QFileDialog
from PySide2.QtCore import Qt
from create_userTemplate import *
import requests
import os
import sys
#Anexo el Directorio en donde se encuentra la clase a llamar
sys.path.append('/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/Fase 2_3/Client/views/')
base_url = "http://localhost:5000"
class NewBookWindow(QWidget, NewBookForm):

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)


        self.addButton.clicked.connect(self.add_book)
        self.cancelButton.clicked.connect(self.close)
    
    def check_inputs(self):
        nick = self.titleLineEdit.text()
        pwd = self.categoryLineEdit.text()
        coins = self.pageQtySpinBox.value()
        age = self.filePathLineEdit.text()

        errors_count = 0
        
        if nick == "":
            print("El campo nickname es obligatorio")
            errors_count += 1
        if pwd == "":
            print("El campo pwd es obligatorio")
            errors_count +=1
        if coins == 0:
            print("El campo cantidad de monedas es obligatorio")
            errors_count +=1
        if age == "":
            print("Debe seleccionar un libro")
            errors_count +=1
        
        return (errors_count == 0)
            
        
    def add_book(self):
        nick = self.titleLineEdit.text()
        pwd = self.categoryLineEdit.text()
        coins = str(self.pageQtySpinBox.value())
        age = str(self.filePathLineEdit.text())

        if self.check_inputs():
            data = (nick, pwd, coins, age)
            self.clean_inputs()
            usuario = {'nick': nick,'password':pwd,'monedas':coins,'edad':age}
            x = requests.post(f'{base_url}/guardar_usuario', json = usuario)
            # dicc = {}
            if x.status_code ==200:
              self.parent.tableData()
              
              # print(users.json())
              # for i in users.json():
              #   print(i['id'])
            
          
    def clean_inputs(self):
        self.titleLineEdit.clear()
        self.categoryLineEdit.clear()
        self.pageQtySpinBox.setValue(0)
        self.filePathLineEdit.clear()




        