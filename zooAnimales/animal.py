class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona

    @classmethod
    def movimiento(cls):
        return "desplazarse"

    @classmethod
    def totalPorTipo(cls):
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.ave import Ave
        from zooAnimales.reptil import Reptil
        from zooAnimales.pez import Pez
        from zooAnimales.anfibio import Anfibio
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + '\n' + \
               "Aves : " + str(Ave.cantidadAves()) + '\n' + \
               "Reptiles : " + str(Reptil.cantidadReptiles()) + '\n' + \
               "Peces : " + str(Pez.cantidadPeces()) + '\n' + \
               "Anfibios : " + str(Anfibio.cantidadAnfibios())

    def getTotalAnimales(self):
        return self._totalAnimales

    def setTotalAnimales(self, total):
        self._totalAnimales = total

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    def toString(self):
        if self._zona is None:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero
        else:
            return "Mi nombre es " + self._nombre + ", tengo una edad de " + str(self._edad) + ", habito en " + self._habitat + " y mi genero es " + self._genero + ", la zona en la que me ubico es " + self._zona + ", en el " + self._zona.zoo