from collections.abc import Iterable, Iterator
from enum import Enum

# -----------------------------------------------------------------------------
# 2.- Iterador concreto
# -----------------------------------------------------------------------------
class Iterador(Iterator):

    class Tipo(Enum):
        KEY_1 = 0,
        KEY_1_REV = 1
        KEY_2 = 2
        KEY_2_REV = 3
        KEY_3 = 4

    INDICE = 0

    def __init__(self, coleccion: dict, tipo: Tipo = Tipo.KEY_1):
        # el metodo "Sorted" entrega una tupla
        if tipo == self.Tipo.KEY_1:
            self._coleccion = sorted(coleccion.items())
        elif tipo == self.Tipo.KEY_1_REV:
            self._coleccion = sorted(coleccion.items(), reverse=True)
        elif tipo == self.Tipo.KEY_2:
            self._coleccion = sorted(coleccion.items(), key=lambda kv:(kv[1], kv[0]))
        elif tipo == self.Tipo.KEY_2_REV:
            self._coleccion = sorted(coleccion.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)
        else:
            raise NotImplementedError('La forma de recorrer el diccionarion no esta aun implementado')

    def __next__(self):
        try:
            elemento = self._coleccion[self.INDICE]
            self.INDICE += 1
        except IndexError:
            raise StopIteration() # Importante para detener el ciclo
        return elemento

# -----------------------------------------------------------------------------
# 4.- Colecciones Concretas
# -----------------------------------------------------------------------------
class Calificaciones(Iterable):

    def __init__(self, coleccion: dict = {}):
        self._coleccion = coleccion

    def __iter__(self):
        return Iterador(self._coleccion)

    def calificacion_mas_alta_primero(self):
        return Iterador(self._coleccion, Iterador.Tipo.KEY_2_REV)

    def registrar(self, alumno, calificacion):
        self._coleccion[alumno] = calificacion

class Productos(Iterable):

    def __init__(self, productos: dict = {}):
        self._productos = productos
    
    def __iter__(self):
        return Iterador(self._productos)

    def precio_mas_bajo_primero(self):
        return Iterador(self._productos, Iterador.Tipo.KEY_2)

    def registrar(self, producto, precio):
        self._productos[producto] = precio

if __name__ == "__main__":

    diseno_de_software = Calificaciones()
    diseno_de_software.registrar('Victor', 9.6)
    diseno_de_software.registrar('Juan Pedro', 8.62)
    diseno_de_software.registrar('Ulises', 6.1)
    diseno_de_software.registrar('Corina', 8.6)
    diseno_de_software.registrar('Rosita', 10)

    print('-I- Mostrando las calificaciones en order alfabetico de los alumnos')
    for registro in diseno_de_software:
        print(registro)
    print()

    print('-I- Mostrando las calificaciones primero las mas altas')
    for registro in diseno_de_software.calificacion_mas_alta_primero():
        print(registro)
    print()
    
    # Incluso podemos seguir usando el mismo iterador concreto en otras clases
    lista_de_compras = Productos()
    lista_de_compras.registrar('Sandia', 21.20)
    lista_de_compras.registrar('Jitomate', 10.50)
    lista_de_compras.registrar('Platano', 7.00)

    print('-I- Mostrando los productos en orden alfabetico')
    for producto in lista_de_compras:
        print(producto)
    print()

    print('-I- Mostrando los productos primero el mas barato')
    for producto in lista_de_compras.precio_mas_bajo_primero():
        print(producto)