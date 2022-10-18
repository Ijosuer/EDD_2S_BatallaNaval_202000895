import os
import random
import webbrowser
from Nodo_cabecera import Nodo_Cabecera
from Lista_Cabecera import Lista_Cabecera
from Nodo_interno import Nodos_internos

class Matriz():
    def __init__(self, capa):
        self.capa = capa
        self.filas = Lista_Cabecera('fila')
        self.columnas = Lista_Cabecera('columna')

     # (filas = x, columnas = y)
    def insert(self, pos_x, pos_y, caracter):
        nuevo = Nodos_internos(pos_x, pos_y, caracter) # se crea nodo interno
        # --- lo prinero sera buscar si ya existen los encabezados en la matriz
        nodo_X = self.filas.getCabecera(pos_x)
        nodo_Y = self.columnas.getCabecera(pos_y)

        if nodo_X == None: # --- comprobamos que el encabezado fila pos_x exista
             # --- si nodo_X es nulo, quiere decir que no existe encabezado fila pos_x
            nodo_X = Nodo_Cabecera(pos_x)
            self.filas.insertar_nodoCabecera(nodo_X)

        if nodo_Y == None: # --- comprobamos que el encabezado columna pos_y exista
            # --- si nodo_Y es nulo, quiere decir que no existe encabezado columna pos_y
            nodo_Y = Nodo_Cabecera(pos_y)
            self.columnas.insertar_nodoCabecera(nodo_Y)

        # ----- INSERTAR NUEVO EN FILA
        if nodo_X.acceso == None: # -- comprobamos que el nodo_x no esta apuntando hacia ningun nodoInterno
            nodo_X.acceso = nuevo
        else: # -- si esta apuntando, validamos si la posicion de la columna del NUEVO nodoInterno es menor a la posicion de la columna del acceso 
            if nuevo.coordenadaY < nodo_X.acceso.coordenadaY: # F1 --->  NI 1,1     NI 1,3
                nuevo.derecha = nodo_X.acceso              
                nodo_X.acceso.izquierda = nuevo
                nodo_X.acceso = nuevo
            else:
                #de no cumplirse debemos movernos de izquierda a derecha buscando donde posicionar el NUEVO nodoInterno
                tmp : Nodos_internos = nodo_X.acceso     # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5;
                while tmp != None:                      #NI 1,6
                    if nuevo.coordenadaY < tmp.coordenadaY:
                        nuevo.derecha = tmp
                        nuevo.izquierda = tmp.izquierda
                        tmp.izquierda.derecha = nuevo
                        tmp.izquierda = nuevo
                        break
                    elif nuevo.coordenadaX == tmp.coordenadaX and nuevo.coordenadaY == tmp.coordenadaY: #validamos que no haya repetidas
                        break
                    else:
                        if tmp.derecha == None:
                            tmp.derecha = nuevo
                            nuevo.izquierda = tmp
                            break
                        else:
                            tmp = tmp.derecha 
                             #         nodo_Y:        C1    C3      C5      C6
                             # nodo_X:F1 --->      NI 1,2; NI 1,3; NI 1,5; NI 1,6;
                             # nodo_X:F2 --->      NI 2,2; NI 2,3; NI 2,5; NI 2,6;

        # ----- INSERTAR NUEVO EN COLUMNA
        if nodo_Y.acceso == None:  # -- comprobamos que el nodo_y no esta apuntando hacia ningun nodoCelda
            nodo_Y.acceso = nuevo
        else: # -- si esta apuntando, validamos si la posicion de la fila del NUEVO nodoCelda es menor a la posicion de la fila del acceso 
            if nuevo.coordenadaX < nodo_Y.acceso.coordenadaX:
                nuevo.abajo = nodo_Y.acceso
                nodo_Y.acceso.arriba = nuevo
                nodo_Y.acceso = nuevo
            else:
                # de no cumplirse, debemos movernos de arriba hacia abajo buscando donde posicionar el NUEVO
                tmp2 : Nodos_internos = nodo_Y.acceso
                while tmp2 != None:
                    if nuevo.coordenadaX < tmp2.coordenadaX:
                        nuevo.abajo = tmp2
                        nuevo.arriba = tmp2.arriba
                        tmp2.arriba.abajo = nuevo
                        tmp2.arriba = nuevo
                        break;
                    elif nuevo.coordenadaX == tmp2.coordenadaX and nuevo.coordenadaY == tmp2.coordenadaY: #validamos que no haya repetidas
                        break;
                    else:
                        if tmp2.abajo == None:
                            tmp2.abajo = nuevo
                            nuevo.arriba = tmp2
                            break
                        else:
                            tmp2 = tmp2.abajo

        ##------ Fin de insercion
    def graficarDibujo(self, nombre,title):
        contenido = '''digraph G{bgcolor="powderblue"
        node[shape=box, width=0.7, height=0.7, fontname="Arial", fillcolor="white", style=filled]
        edge[style = "bold"]
        node[label = "''' + title +'''" fontsize=8 fillcolor="darkolivegreen1" pos = "-1,1!"]raiz;'''
        # --graficar nodos ENCABEZADO
        # --graficar nodos fila
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            contenido += '\n\tnode[label = "F{}" fillcolor="lightgoldenrod" pos="-1,-{}!" shape=box]x{};'.format(pivote.id, 
            posx, pivote.id)
            pivote = pivote.siguiente
            posx += 1
        pivote = self.filas.primero
        while pivote.siguiente != None:
            contenido += '\n\tx{}->x{};'.format(pivote.id, pivote.siguiente.id)
            contenido += '\n\tx{}->x{}[dir=back];'.format(pivote.id, pivote.siguiente.id)
            pivote = pivote.siguiente
        contenido += '\n\traiz->x{};'.format(self.filas.primero.id)

        # --graficar nodos columna
        pivotey = self.columnas.primero
        posy = 0
        while pivotey != None:
            contenido += '\n\tnode[label = "C{}" fillcolor="lightgoldenrod" pos = "{},1!" shape=box]y{};'.format(pivotey.id, 
            posy, pivotey.id)
            pivotey = pivotey.siguiente
            posy += 1
        pivotey = self.columnas.primero
        while pivotey.siguiente != None:
            contenido += '\n\ty{}->y{};'.format(pivotey.id, pivotey.siguiente.id)
            contenido += '\n\ty{}->y{}[dir=back];'.format(pivotey.id, pivotey.siguiente.id)
            pivotey = pivotey.siguiente
        contenido += '\n\traiz->y{};'.format(self.columnas.primero.id)

        #ya con las cabeceras graficadas, lo siguiente es los nodos internos, o nodosCelda
        pivote = self.filas.primero
        posx = 0
        while pivote != None:
            pivote_celda : Nodos_internos = pivote.acceso
            while pivote_celda != None:
                # --- buscamos posy
                pivotey = self.columnas.primero
                posy_celda = 0
                while pivotey != None:
                    if pivotey.id == pivote_celda.coordenadaY: break
                    posy_celda += 1
                    pivotey = pivotey.siguiente
                if pivote_celda.caracter == 'P':
                    contenido += '\n\tnode[label="P" fontcolor="black" fillcolor="maroon" pos="{},-{}!" shape=box]i{}_{};'.format( #pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'S':
                    contenido += '\n\tnode[label="S" fontcolor="white" fillcolor="navy" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                elif pivote_celda.caracter == 'B':
                    contenido += '\n\tnode[label="B"  fillcolor="teal" fontcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    )
                elif pivote_celda.caracter == 'D':
                    contenido += '\n\tnode[label="D" fontcolor="black" fillcolor="gray" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                elif pivote_celda.caracter == 'F':
                    contenido += '\n\tnode[label="X" fontcolor="black" fillcolor="red" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                else:
                    contenido += '\n\tnode[label=" " fontcolor="black" fillcolor="black" pos="{},-{}!" shape=box]i{}_{};'.format( # pos="{},-{}!"
                        posy_celda, posx, pivote_celda.coordenadaX, pivote_celda.coordenadaY
                    ) 
                    # pass
                pivote_celda = pivote_celda.derecha
            
            pivote_celda = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.derecha != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.derecha.coordenadaX, pivote_celda.derecha.coordenadaY)
                pivote_celda = pivote_celda.derecha
        
            contenido += '\n\tx{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\tx{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            posx += 1
        
        pivote = self.columnas.primero
        while pivote != None:
            pivote_celda : Nodos_internos = pivote.acceso
            while pivote_celda != None:
                if pivote_celda.abajo != None:
                    contenido += '\n\ti{}_{}->i{}_{};'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY)
                    contenido += '\n\ti{}_{}->i{}_{}[dir=back];'.format(pivote_celda.coordenadaX, pivote_celda.coordenadaY,
                    pivote_celda.abajo.coordenadaX, pivote_celda.abajo.coordenadaY) 
                pivote_celda = pivote_celda.abajo
            contenido += '\n\ty{}->i{}_{};'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            contenido += '\n\ty{}->i{}_{}[dir=back];'.format(pivote.id, pivote.acceso.coordenadaX, pivote.acceso.coordenadaY)
            pivote = pivote.siguiente
            
        contenido += '\n}'
        #--- se genera DOT y se procede a ecjetuar el comando
        dot = "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/{}_dot.txt".format(nombre)
        with open(dot, 'w') as grafo:
            grafo.write(contenido)
        result = "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/{}.png".format(nombre)
        os.system("neato -Tpng " + dot + " -o " + result)
        # webbrowser.open(result)

    def recorridoPorFila(self, fila):
        inicio : Nodo_Cabecera = self.filas.getCabecera(fila)
        if inicio == None:
            print('Esa coordenada de filas no existe')
            return None
        else:
            return True

        # tmp : Nodos_internos = inicio.getAcceso()
        # #tmp = self.filas.getCabecera(fila).getAcceso()
        # while tmp != None:
        #     print(tmp.caracter)
        #     tmp = tmp.getDerecha()

    
    def recorridoPorColumna(self, columna):
        inicio : Nodo_Cabecera = self.columnas.getCabecera(columna)
        if inicio == None:
            print('Esa coordenada de columna no existe')
            return None

        tmp : Nodos_internos = inicio.getAcceso()
        #tmp = self.filas.getCabecera(fila).getAcceso()
        while tmp != None:
            print(tmp.caracter)
            tmp = tmp.abajo


    def disparo(self, fila, columna):
        try:
            tmp : Nodos_internos = self.filas.getCabecera(fila).getAcceso()
            while tmp != None:
                if tmp.coordenadaX == fila and tmp.coordenadaY == columna:
                    return tmp
                tmp = tmp.derecha
            return None
        except:
            # print('Coordenada no encontrada')
            return None

    def ubicarCoordenada(self, fila, columna):
        try:
            tmp : Nodos_internos = self.filas.getCabecera(fila).getAcceso()
            while tmp != None:
                if tmp.coordenadaX == fila and tmp.coordenadaY == columna:
                    return tmp
                tmp = tmp.derecha
            return None
        except:
            # print('Coordenada no encontrada')
            return None
    def generarMatrizRandom(self, x):
        puerta = False
        barcos = int(((x-1)/10) + 1)
        iterator = barcos
        porta = barcos
        print(str(barcos)+" porta")
        barcos+=iterator
        sub = barcos
        print(str(sub)+" submarinos")
        barcos+=iterator
        destr = barcos
        print(str(destr)+" Destructores")
        barcos+=iterator
        buqes = barcos
        print(str(buqes)+" Buqes")
        i = 0     
        flag = False
        while flag==False:
            _x = (random.randint(1,x))
            _y = (random.randint(1,x))
            if(_x == x):
                pass
            elif(_y == x or _y == x-1 or _y == x-2 or _y == x-3):
                _y -=4
            else:
                pass
            if (self.ubicarCoordenada(_x,_y)==None):
                for i in range(porta):
                    puerta = False
                    while puerta == False:
                        if(self.ubicarCoordenada(_x,_y)==None):
                            if(self.ubicarCoordenada(_x,_y+1)==None):
                                if(self.ubicarCoordenada(_x,_y+2)==None):
                                    if(self.ubicarCoordenada(_x,_y+3)==None):
                                        print('si')
                                        self.insert(_x,_y,"P")
                                        self.insert(_x,_y+1,"P")
                                        self.insert(_x,_y+2,"P")
                                        self.insert(_x,_y+3,"P")
                                        puerta = True
                                        # _y +=1
                                        i+=1
                                        if(i == porta):
                                            flag = True
                                            break
                                    else:
                                        flag = False;    
                                        _x = (random.randint(1,x))
                                        _y = (random.randint(1,x))
                                        if(_x == x):
                                            pass
                                        elif(_y == x or _y == x-1 or _y == x-2 or _y == x-3):
                                            _y -=4
                                        else:
                                            pass
                                else:
                                    flag = False;    
                                    _x = (random.randint(1,x))
                                    _y = (random.randint(1,x))
                                    if(_x == x):
                                        pass
                                    elif(_y == x or _y == x-1 or _y == x-2 or _y == x-3):
                                        _y -=4
                                    else:
                                        pass
                            else:
                                flag = False;    
                                _x = (random.randint(1,x))
                                _y = (random.randint(1,x))
                                if(_x == x):
                                    pass
                                elif(_y == x or _y == x-1 or _y == x-2 or _y == x-3):
                                    _y -=4
                                else:
                                    pass
                        else:
                            flag = False;    
                            _x = (random.randint(1,x))
                            _y = (random.randint(1,x))
                            if(_x == x):
                                pass
                            elif(_y == x or _y == x-1 or _y == x-2 or _y == x-3):
                                _y -=4
                            else:
                                pass
            else:
                flag = False
                _x = (random.randint(1,x))
                _y = (random.randint(1,x))
                if(_x == x):
                    pass
                elif(_y == x or _y == x-1 or _y == x-2 or _y == x-3):
                    _y -=4
                else:
                    pass
        #B
        for j in range(buqes):
            flag = False
            while flag==False:
                _x = (random.randint(1,x))
                _y = (random.randint(1,x))
                if (self.ubicarCoordenada(_x,_y)==None):
                    if(self.ubicarCoordenada(_x,_y)==None):
                        self.insert(_x,_y,"B")
                        _x +=1
                        break
                    else:
                        flag = False;    
                else:
                    flag = False
        #S
        flag = False
        while flag==False:
            _x = (random.randint(1,x))
            _y = (random.randint(1,x))
            if(_y == x):
                pass
            elif(_x == x or _x == x-1 or _x == x-2 or _x == x-3):
                _x -=3
            else:
                pass
                for i in range(sub):
                    puerta = False
                    while puerta == False:
                        if (self.ubicarCoordenada(_x,_y)==None):
                            if(self.ubicarCoordenada(_x+1,_y)==None):
                                if(self.ubicarCoordenada(_x+2,_y)==None):
                                        self.insert(_x,_y,"S")
                                        self.insert(_x+1,_y,"S")
                                        self.insert(_x+2,_y,"S")
                                        # _x +=1
                                        puerta = True
                                        i+=1
                                        if(i == sub):
                                            flag = True
                                            break
                                else:
                                    flag = False;  
                                    _x = (random.randint(1,x))
                                    _y = (random.randint(1,x))
                                    if(_y == x):
                                        pass
                                    elif(_x == x or _x == x-1 or _x == x-2 or _x == x-3):
                                        _x -=3
                                    else:
                                        pass  
                            else:
                                flag = False;    
                                _x = (random.randint(1,x))
                                _y = (random.randint(1,x))
                                if(_y == x):
                                    pass
                                elif(_x == x or _x == x-1 or _x == x-2 or _x == x-3):
                                    _x -=3
                                else:
                                    pass  
                        else:
                            flag = False;    
                            _x = (random.randint(1,x))
                            _y = (random.randint(1,x))
                            if(_y == x):
                                pass
                            elif(_x == x or _x == x-1 or _x == x-2 or _x == x-3):
                                _x -=3
                            else:
                                pass  

        #D
        flag = False
        while flag==False:
            _x = (random.randint(1,x-2))
            _y = (random.randint(1,x-2))
            if (self.ubicarCoordenada(_x,_y)==None):
                for j in range(destr):
                    puerta = False
                    while puerta == False:
                        if(self.ubicarCoordenada(_x,_y)==None):
                            if(self.ubicarCoordenada(_x,_y+1)==None):
                                self.insert(_x,_y,"D")
                                self.insert(_x,_y+1,"D")
                                # _y +=1
                                puerta = True
                                j+=1
                                if(j == destr):
                                    flag = True
                                    break
                            else:
                                flag = False;    
                                _x = (random.randint(1,x-2))
                                _y = (random.randint(1,x-2))
                        else:
                            flag = False;    
                            _x = (random.randint(1,x-2))
                            _y = (random.randint(1,x-2))
            else:
                flag = False
                _x = (random.randint(1,x-2))
                _y = (random.randint(1,x-2))
        # self.graficarDibujo("dispersa","BATTLE SHIP")
        
# if __name__ == "__main__":
#     self = Matriz(0)   
#     muerte = 0
#     self.generarMatrizRandom(24)
#     while True:
#         xx = int(input('Ingrese en exis: '))
#         yy = int(input('Ingrese en ye: '))
#         # xx = (random.randint(1,x))
#         # yy = (random.randint(1,x))
#         ans = self.ubicarCoordenada(xx,yy)
#         if(ans == None):
#             self.insert(xx,yy," ")
#         else:
#             ans.caracter = "F"
#             muerte +=1
#         if(muerte == 4):
#             self.graficarDibujo("dispersa","BATTLE SHIP")
#             print(muerte)
#             break;
#         self.graficarDibujo("dispersa","BATTLE SHIP")

        
    # self.insert(9,9,"B")
    # self.insert(9,20,"B")
    # self.recorridoPorColumna(2)
   