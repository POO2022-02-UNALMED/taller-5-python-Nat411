from zooAnimales.Animal import Animal
class Reptil (Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __int__(self, nombre= None, edad=0, habitat=None, genero=None, zona=None, colorEscamas = None, largoCola = 0):
        super().__init__(nombre, edad, habitat, genero, zona)
        super().totalAnimales +=1
        self.__colorEscamas = colorEscamas
        self.__largoCola = largoCola
        self.listado.append(self)

    def getListado(self):
        return self.listado

    def getColorEscamas(self):
        return self.__colorEscamas
    def setColorEscamas(self, colorEscamas):
        self.__colorEscamas = colorEscamas

    def getLargoCola(self):
        return self.__LargoCola
    def setLargoCola(self, LargoCola):
        self.__LargoCola = LargoCola

    def cantidadReptiles(self):
        return len(self.listado)
    
    def movimiento(self):
        return "reptar"


    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas +=1
        return Reptil(nombre, edad, "humedal", genero, "verde",3)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes +=1
        return Reptil(nombre, edad, "jungla", genero, "blanco",1)