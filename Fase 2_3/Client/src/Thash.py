import os


class NodeHash:
  def __init__(self, id, name) -> None:
    self.id = id
    self.name = name


class Hash:
  def __init__(self, m:int , min:int, max:int):
    # min,max ,n ,m= 0
    self.n = 0
    self.iterator = 0
    self.h = []
    self.m = m
    self.min = min
    self.max = max
    self.init()

  def division(self, k:int):
    return (int(k%self.m))

  def linear(self, k:int):
    return (int((k%3)+1)*self.iterator)
    # return (int((k+1)%self.m))

  def init(self):
    self.iterator = 0
    self.n = 0
    self.h = [None]*int(self.m)
    for i in range(int(self.m)):
      self.h[i] = NodeHash(-1,"")

  def insert(self, k:int , name:str):
    i = self.division(k)
    if (self.h[i].id == -1):
      if ((self.n*100/self.m) >= self.max):
        self.rehashing()
      else:
        # nodo = new NodeHash(k,name)
        self.h[i] = NodeHash(k,name)
        self.n+=1

    else:
      # self.n+=1
      self.iterator +=1
      nuevo = self.linear(k)
      nuevo = nuevo + self.iterator
      if(nuevo <= len(self.h)):
        if(self.h[nuevo].id == -1):
          # self.n+=1
          if ((self.n*100/self.m) >= self.max):
            self.rehashing()
          self.h[nuevo] = NodeHash(k,name)
          self.n+=1
        else:
          self.rehashing()
          # self.h[nuevo] = k
      else:
        self.rehashing()
        if ((self.n*100/self.m) >= self.max): self.rehashing()
        else:self.h[nuevo] = NodeHash(k,name)

    self.sout()
  # def insert(self, k:int):
  #   i = self.division(k)
  #   i = int(i)
  #   while (self.h[i] != -1):
  #     i = self.linear(i)
  #   self.h[i] = k
  #   self.n +=1
  #   self.rehashing()


  def rehashing(self):
    #Array copy
    # self.sout()
    temp = self.h
    # Rehash now
    mprev = self.m
    self.m = self.n*100/self.min
    self.init()
    for i in range(int(mprev)):
      if (temp[i].id != -1):
        self.insert(temp[i].id, temp[i].name)
    # self.sout()

  def sout(self):
    print('')
    # print('[',end=' ')
    # for i in range(int(self.m)):
    #   print(' '+str(self.h[i].id),end=' ')
    # print(']',self.n*100/self.m,'%')

  def grafica(self):
    text = '''digraph {
  node [ shape=none fontname=Helvetica ]\nn3 [ label = <
    <table border="1">
       <tr><td colspan="1" bgcolor="Peru">id</td><td colspan="1" bgcolor="Peru">name</td><td colspan="1" bgcolor="Peru">index</td></tr>'''
       
    for i in range(int(self.m)):
      if(self.h[i].id != -1):
        text+='<tr><td bgcolor="orange">'+str(self.h[i].id)+'</td><td bgcolor="orange">'+self.h[i].name+' </td><td bgcolor="yellow">'+str(i)+ '</td></tr>\n\t'

    text+='''\t</table> \n>]\n}'''
    dot = "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/{}_dot.txt".format('Tabl')
    with open(dot, 'w') as grafo:
        grafo.write(text)
    result = "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/{}.png".format('TablaHash')
    os.system("dot -Tpng " + dot + " -o " + result)
    # print(text)
if __name__ == "__main__":
  hashito = Hash(5,20,80)
  hashito.insert(5,"josue")
  hashito.insert(10,"dani")
  # hashito.insert(15,"kpngi")
  # hashito.insert(2,"luca")
  # hashito.insert(20,"jej")
  # hashito.insert(25,"vomit")
  # hashito.insert(30,"skrim")
  hashito.grafica()
  # hashito.insert(35)
  # hashito.insert(40)
  # hashito.insert(45)
  # hashito.insert(50)
  # hashito.insert(55)


