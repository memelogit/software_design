from copy import deepcopy, copy
from math import pi, pow
from random import randint
from abc import ABC, abstractmethod

# Clase abstracta para figuras
class FiguraAbstracta(ABC):
    @abstractmethod
    def clonar(self):
        pass

    @abstractmethod
    def deep(self):
        pass

class Figura(FiguraAbstracta):
    def __init__(self, pos_x = 0, pos_y = 0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.__color = 'blanco'
        self.__id = randint(10000, 99999)
    
    @property
    def id(self):
        return self.__id
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color: str):
        self.__color = color
    
    def clonar(self):
        return copy(self)
    
    def deep(self):
        return deepcopy(self)

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
    
    def __copy__(self):
        ''' Dunder method usado para personalizar la copia '''
        return Rectangulo(self.ancho, self.alto)

    def area(self):
        return self.ancho * self.alto

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
    
    def area(self):
        return pi * (self.radio ** 2)

# Usamos el método clonar en el rectángulo
rect_o = Rectangulo(4, 3)

# Elegimos el tipo de copia
rect_c = rect_o.clonar()

# Imprimimos las diferencias
print('-' * 75)
print(f'{"RECTANGULO":^70}')
print('-' * 75)
print(f'{"nivel":^15}{"atributo":<20}{"original":^20}{"copia":^20}')
print('-' * 75)
print(f'{"subclase":^15}{"ancho":<20}{rect_o.ancho:^20}{rect_c.ancho:^20}')
print(f'{"subclase":^15}{"alto":<20}{rect_o.alto:^20}{rect_c.alto:^20}')
print(f'{"padre":^15}{"id":<20}{rect_o.id:^20}{rect_c.id:^20}')
print(f'{"padre":^15}{"color":<20}{rect_o.color:^20}{rect_c.color:^20}')
print('-' * 75)

# Mutable objects
arreglo_original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arreglo_copia = copy(arreglo_original)
arreglo_original[1][0] = 'X'
print(arreglo_original)
print(arreglo_copia)