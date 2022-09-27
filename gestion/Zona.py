from gestion.Zoologico import Zoologico
from zooAnimales.animal import Animal
class Zona:

    def __init__(self, nombre = None, zoo = None, animal = []) :
        self.__nombre = nombre
        self.__zoo = zoo
        self.__animal = animal

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getZoo(self):
        return self.__zoo
    def setZoo(self, zoo):
        if isinstance(zoo, Zoologico):
            self.__zoo = zoo
        
    def getAnimal(self):
        return self.__animal
    def setAnimal(self, animal):
        self.__animal = animal

    def agregarAnimales(self, animal):
        if isinstance(animal, Animal):
            self.__animal.append(animal)

    def cantidadAnimales(self):
        return len(self.__animal)
