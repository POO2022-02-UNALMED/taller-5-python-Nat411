from zooAnimales.Animal import Animal
class Mamifero (Animal):
    listado = []
    caballos = 0
    leones = 0

    def __int__(self, nombre= None, edad=0, habitat=None, genero=None, zona=None, pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero, zona)
        super().totalAnimales +=1
        self.__pelaje = pelaje
        self.__patas = patas
        self.listado.append(self)

    def getListado(self):
        return self.listado

    def isPelaje(self):
        return self.__pelaje
    def setPelaje(self, pelaje):
        self.__pelaje = pelaje

    def getPatas(self):
        return self.__patas
    def setPatas(self, patas):
        self.__patas = patas

    def cantidadMamiferos(self):
        return len(self.listado)


    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        cls.caballos +=1
        return Mamifero(nombre, edad, "pradera", genero, True,4)

    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        cls.leones +=1
        return Mamifero(nombre, edad, "selva", genero, True,4)