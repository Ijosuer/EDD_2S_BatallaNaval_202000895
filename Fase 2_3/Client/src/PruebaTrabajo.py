from datetime import datetime
import os
import json
from hashlib import sha256

class Blockchain:
  def __init__(self,Data,prefijo):
    self.data = Data
    self.previousHash = "0000"
    self.rootMerkle = ""
    self.index = 0
    self.prefijo = prefijo
    self.hash = ""
    self.nonce = 0
    self.time = ''
    self.PATH = '/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/blockchain/'
    self.listaBlock = []

  def generar(self):
    while True:
      self.nonce += 1
      self.hash=self.data+""+str(self.nonce)
      
      if(str(sha256(self.hash.encode('utf-8')).hexdigest()).find(self.prefijo)==0):
        # print(self.nonce, sha256(self.hash.encode('utf-8')).hexdigest())
        self.hash = sha256(self.hash.encode('utf-8')).hexdigest()
        break;
  
  # def add(self):
  #   print(self.hash)
  #   merkle.add('josue123 4:30')
  #   merkle.add('mikeas23 4:33')
  #   merkle.add('masmdfmas 4:40')
  #   merkle.auth()
  #   self.rootMerkle = merkle.tophash.hash
  #   self.writeBlock()

  def writeBlock(self):
    self.generar()
    date = datetime.now()
    timeok =str(date.year)+'-'+str(date.month)+'-'+str(date.day)+'::'+ str(date.hour)+':'+str(date.minute)+':'+str(date.second)
    bloque = {"INDEX":self.index,"TIME":timeok,"NONCE":self.nonce}
    
    bloque['DATA'] = []
    for i in range(3):
      bloque['DATA'].append({"Skin":str(i+1),"Value":str(i*100)})

    bloque["PREVIOUSHASH"] = self.previousHash
    bloque["ROOTMERKLE"] = self.rootMerkle
    bloque["HASH"] = self.hash
    self.listaBlock.append(bloque)
    self.previousHash = self.hash
    # Generar JSON
    times = timeok.replace(':','-')
    with open(self.PATH+'data'+str(self.index)+'_'+times+'.json', 'w') as file:
      json.dump(bloque, file, indent=4)
    self.index +=1

  def graficar(self):
    text = '''digraph G {
        rankdir=LR; 
        labelloc = "t;"label = "BLOCKCHAIN";'''
    itera = 0
    flag = False 
    for i in self.listaBlock:
      if(flag == True):
        text+='x'+str(itera)+'[shape = "record", label="Index = '+str(i['INDEX'])+'|PrevHash = '+str(i["PREVIOUSHASH"])+'|Hash = '+str(i['HASH'])+'"]\n'
      elif (len(self.listaBlock) == 1):
        text+='x'+str(itera)+'[shape = "record", label="Index = '+str(i['INDEX'])+'|PrevHash = '+str(i["PREVIOUSHASH"])+'|Hash = '+str(i['HASH'])+'"]\n'
      else:
        text+='x'+str(itera)+'[shape = "record", label="Index = '+str(i['INDEX'])+'|PrevHash = '+str(i["PREVIOUSHASH"])+'|Hash = '+str(i['HASH'])+'"]x'+str(itera)+'->x'+str(itera+1)+'\n'
        itera+=1
      if(itera+1 == len(self.listaBlock)):
        flag = True
    text+='}'
    dot = "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/blockchain/{}_dot.txt".format('BlockChain')
    with open(dot, 'w') as block:
        block.write(text)
    result = "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/blockchain/{}.png".format('BlockChain')
    os.system("dot -Tpng " + dot + " -o " + result)
    

# if __name__ == "__main__":
#   prueba = Blockchain('holasog123SIDccascxd',"0000")   
#   merkle.add('dani123 4:33')
#   merkle.add('kongiawdf2 4:40')
#   merkle.add('awdf2 4:20')
#   merkle.auth()
#   prueba.rootMerkle = merkle.tophash.hash
#   prueba.writeBlock()
#   prueba.writeBlock()
#   prueba.writeBlock()
  # prueba.graficar()
  # merkle.graficar()