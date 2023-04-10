# DISEÑO DE SOFTWARE
# MODULO 4 - PATRONES DE DISEÑO ESTRUCTURALES
# COMPOSITE

from abc import ABC
from random import randrange

# Interfase del componente
class Elemento(ABC):
  ''' Interfase del elemento componente '''

  def costo(self) -> int:
    ''' Retorna el costo en entero del elemento en la estructura de arbol '''
    pass
  
  def mostrar(self, indent:int=0) -> str:
    ''' Muestra la estructura de arbol a partir de este elemento '''
    pass

# Hoja que es una clase concreta
class Persona(Elemento):
  ''' Clase que representa el último elemento de la estructura de arbol '''

  COSTO_MIN = 500
  COSTO_MAX = 2000

  def __init__(self, nombre:str) -> None:
    self.nombre = nombre
    self._costo = randrange(Persona.COSTO_MIN, Persona.COSTO_MAX)
  
  def costo(self) -> int:
    ''' Retorna el costo en entero del elemento en la estructura de arbol '''
    return self._costo
  
  def mostrar(self, indent:int=0) -> str:
    ''' Muestra la estructura de arbol a partir de este elemento '''
    #     - Victor $500\n
    #     - Hugo $500\n
    #     - Paco $500\n
    return ' ' * indent + '- ' + self.nombre + ' $' + str(self._costo) + '\n'

# Composite (Contenedor)
class Departamento(Elemento):
  ''' Clase composite que contiene elementos '''
  def __init__(self, nombre:str) -> None:
    self.nombre = nombre
    self.hijos:list = []
  
  def agregar(self, elemento:Elemento) -> None:
    ''' Agrega elementos a nuestra estructura de arbol '''
    self.hijos.append(elemento)
  
  def eliminar(self, elemento:Elemento) -> None:
    ''' Remueve elementos del composite '''
    self.hijos.remove(elemento)
  
  def costo(self) -> int:
    ''' Retorna el costo en entero del elemento en la estructura de arbol '''
    costo_total = 0
    for hijo in self.hijos:
      costo_total += hijo.costo()
    return costo_total
  
  def mostrar(self, indent: int = 0) -> str:
    ''' Muestra la estructura de arbol a partir de este elemento '''
    #     + DESI\n
    #       - Hugo $500\n
    detalle_hijos = ' ' * indent + '+ ' + self.nombre + '\n'
    for hijo in self.hijos:
      detalle_hijos += ' ' * indent + hijo.mostrar(indent + 2)
    return detalle_hijos

if __name__ == '__main__':
  victor = Persona('Víctor')
  
  iteso = Departamento('ITESO Rectoría')
  administracion = Departamento('Dirección de administración y finanzas')
  administracion.agregar(Persona('Pedrito'))
  administracion.agregar(Persona('Junito'))
  academico = Departamento('Dirección general académica')
  desi = Departamento('Departamento de electronica, sistemas e informática')
  academico.agregar(desi)
  academico.agregar(Persona('Rosita'))
  desi.agregar(victor)
  desi.agregar(Persona('Iván Villalón'))
  iteso.agregar(administracion)
  iteso.agregar(academico)

  print(desi.costo())
  print(desi.mostrar())
