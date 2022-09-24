class Nodos_internos():

    def __init__(self,coordenadaX,coordenadaY,caracter):
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.caracter = caracter
        self.arriba = None
        self.abajo = None
        self.derecha = None  # self.siguiente
        self.izquierda = None  # self.anterior