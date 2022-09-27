from zooAnimales.anfibio import Anfibio
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil


class Animal:
    totalAnimales =0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, zona= None):
        totalAnimales += 1
        self.__nombre = nombre
        self.__edad = edad
        self.__habitat = habitat
        self.__genero = genero
        self.__zona = zona

    def getTotalAnimales(self):
        return self.totalAnimales

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad
    def setEdad(self, edad):
        self.__edad = edad

    def getHabitat(self):
        return self.__habitat
    def setHabitat(self, habitat):
        self.__habitat = habitat

    def getGenero(self):
        return self.__genero
    def setGenero(self, genero):
        self.__genero = genero

    def getZona(self):
        return self.__zona
    def setZona(self, zona):
        self.__zona = zona

    def totalPorTipo():
        return f"Mamiferos: {Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()}"
    

    def toString(self):
        if self.zona == None:
            return f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi genero es {self.__genero}"
        else:
            return f"Mi nombre es {self.__nombre}, tengo una edad de {self.__edad}, habito en {self.__habitat} y mi genero es {self.__genero}, la zona en la que me ubico es {self.__zona.getNombre()}, en el {self.__zona.getZoo().getNombre()}"

    def movimiento(self):
        return "desplazarse"
