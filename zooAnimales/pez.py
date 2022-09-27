from zooAnimales.animal import Animal
class Pez (Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __int__(self, nombre= None, edad=0, habitat=None, genero=None, colorEscamas = None, cantidadAletas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self.__colorEscamas = colorEscamas
        self.__cantidadAletas = cantidadAletas
        self.listado.append(self)

    def getListado(self):
        return self.listado

    def getColorEscamas(self):
        return self.__colorEscamas
    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self.__cantidadAletas
    def setCantidadAletas(self, cantidadAletas):
        self.__cantidadAletas = cantidadAletas

    def cantidadPeces(self):
        return len(self.listado)
    
    def movimiento(self):
        return "nadar"


    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones +=1
        return Pez(nombre, edad, "oceano", genero, "rojo",6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos +=1
        return Pez(nombre, edad, "oceano", genero, "gris",6)
