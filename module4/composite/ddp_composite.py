from abc import ABC, abstractmethod
from typing import List
from random import randrange
from enum import Enum

# -----------------------------------------------------------------------------
# 1.- Componente (Interface)
# -----------------------------------------------------------------------------
# La interfaz Componente describe operaciones que son comunes a
# elementos simples y complejos del árbol.
class Elemento(ABC):

    @property
    def base(self): # -> Elemento
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @abstractmethod
    def mostrar(self, indent: int = 0) -> str:
        pass

    @abstractmethod
    def costo(self) -> str:
        pass

# -----------------------------------------------------------------------------
# 2.- Hoja (Clase Concreta)
# -----------------------------------------------------------------------------
# La Hoja es un elemento básico de un árbol que no tiene subelementos.
class Persona(Elemento):

    COSTO_MIN = 500
    COSTO_MAX = 1000

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._costo = randrange(self.COSTO_MIN, self.COSTO_MAX)

    def costo(self) -> int:
        return self._costo
    
    def mostrar(self, indent: int = 0):
        return ' ' * indent + '- ' + self.nombre + ' $' + str(self._costo) + '\n'


# -----------------------------------------------------------------------------
# 3.- Contenedor (Clase Concreta)
# -----------------------------------------------------------------------------
# Es un elemento que tiene subelementos: hojas u otros contenedores.
class Departamento(Elemento):
    def __init__(self, nombre: str) -> None:
        self.hijos = []
        self.nombre = nombre

    def agregar(self, elemento: Elemento) -> None:
        self.hijos.append(elemento)
        elemento.base = self

    def eliminar(self, elemento: Elemento) -> None:
        self.hijos.remove(elemento)
        elemento.base = None

    def es_componente(self) -> bool:
        return True

    def costo(self) -> int:
        costo_total = 0
        for hijo in self.hijos:
            costo_total += hijo.costo()
        return costo_total
    
    def mostrar(self, indent: int = 0):
        detalle_hijos = ' ' * indent + '+ ' + self.nombre + '\n'
        for hijo in self.hijos:
            detalle_hijos += ' ' * indent + hijo.mostrar(indent + 2)
        return detalle_hijos

if __name__ == "__main__":
    
    class Moneda(Enum):
        PESOS_MEXICANOS = 1
        DOLARES         = 0.05

    def calcular_costo(costo, moneda: Moneda = Moneda.PESOS_MEXICANOS):
        print('${:,.2f} {}\n'.format(
            costo * moneda.value,
            moneda.name.capitalize()
        ))

    # Suponemos que queremos crear un solo elemento de la hoja
    # y obtener su costo
    victor = Persona('Víctor')
    print('-I- ¿Cuál sería el costo de contratar a Víctor? (Una sola hoja)')
    calcular_costo(victor.costo(), Moneda.DOLARES)

    # Ahora... vamos creando algo mas complejo
    iteso = Departamento('Rectoría')

    administracion = Departamento('Dirección de administración y finanzas')
    administracion.agregar(Persona('Pedro'))
    administracion.agregar(Persona('Rogelio'))

    academia = Departamento('Dirección general académica')
    desi = Departamento('Departamento de electrónica, sistemas e informática')
    desi.agregar(Persona('Iván Villalón'))
    desi.agregar(Persona('Francisco Cervantes'))
    dfh = Departamento('Departamento de formación humana')
    dfh.agregar(Persona('Juan Pablo'))
    academia.agregar(desi)
    academia.agregar(dfh)

    iteso.agregar(administracion)
    iteso.agregar(academia)

    print('-I- ¿Cuál sería el costo de la nómina del ITESO? (Una arbol)')
    calcular_costo(iteso.costo())

    print('-I- Ahora mostremos el detalle de nuestro árbol')
    print(iteso.mostrar())