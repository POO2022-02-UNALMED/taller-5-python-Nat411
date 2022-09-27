class Zoologico:
    pass

    def __init__(self, nombre = None, ubicacion = None, zonas = []):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__zonas = zonas

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getUbicacion(self):
        return self.__ubicacion
    def setZoo(self, ubicacion):
        self.__ubicacion = ubicacion

    def getZonas(self):
        return self.__zonas
    def setZonas(self, zonas):
        self.__zonas = zonas

    def agregarZonas(self, zona):
        self.__zonas.append(zona)

    def cantidadTotalAnimales(self):
        c = 0
        for i in self.__zonas:
            c += self.__zonas[i].cantidadAnimales()
        return c


