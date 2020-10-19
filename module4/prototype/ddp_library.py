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
    def deepcopy(self):
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
    
    def deepcopy(self):
        return deepcopy(self)

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        super().__init__()
        self.ancho = ancho
        self.alto = alto
    
    def __copy__(self):
        print('-I- Personalizamos la copia del rectángulo')
        return Rectangulo(self.ancho + 1, self.alto + 1)
    
    def __deepcopy__(self, memo):
        print('-I- Personalizamos la copia produnda del rectángulo')
        return Rectangulo(self.ancho + 1, self.alto + 1)

    def area(self):
        return self.ancho * self.alto

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
    
    def area(self):
        return pi * (self.radio ** 2)