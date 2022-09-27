from zooAnimales.Animal import Animal
class Ave (Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __int__(self, nombre= None, edad=0, habitat=None, genero=None, zona=None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero, zona)
        super().totalAnimales +=1
        self.__colorPlumas = colorPlumas
        self.listado.append(self)

    def getListado(self):
        return self.listado

    def getColorPlumas(self):
        return self.__colorPlumas
    def setColorPlumas(self, colorPlumas):
        self.__colorPlumas = colorPlumas

    def movimiento(self):
        return "volar"

    def cantidadAves(self):
        return len(self.listado)


    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones +=1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas +=1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")