from zooAnimales.animal import Animal
class Anfibio (Animal):
    listado = []
    ranas = 0
    salamandras = 0

    def __int__(self, nombre= None, edad=0, habitat=None, genero=None, zona=None, colorPiel=None, venenoso= False):
        super().__init__(nombre, edad, habitat, genero, zona)
        super().totalAnimales +=1
        self.__colorPiel = colorPiel
        self.__venenoso = venenoso
        self.listado.append(self)

    def getListado(self):
        return self.listado

    def getColorPiel(self):
        return self.__colorPiel
    def setColorPiel(self, colorPiel):
        self.__colorPiel = colorPiel

    def isVenenoso(self):
        return self.__venenoso
    def setVenenoso(self, venenoso):
        self.__venenoso = venenoso

    def cantidadAnfibios(self):
        return len(self.listado)

    def movimiento(self):
        return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas +=1
        return Anfibio(nombre, edad, "selva", genero, "rojo",True)

    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras +=1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
