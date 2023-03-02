from abc import ABC
from enum import Enum, unique
from typing import Tuple

class Color(ABC):
    ''' Interfase de colores '''
    @property
    def rgba(self) -> Tuple[int, int, int, int]:
        ''' Retorna una tupla con los colores rojo, verde, azul y la opacidad'''
        return (self.rojo, self.verder, self.azul, self.opacidad)

    def __str__(self) -> str:
        return self.nombre

class Blanco(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'white'
        self.rojo:int = 255
        self.verder:int = 255
        self.azul:int = 255
        self.opacidad:int = 100

class Negro(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'black'
        self.rojo:int = 0
        self.verder:int = 0
        self.azul:int = 0
        self.opacidad:int = 100

class Rojo(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'red'
        self.rojo:int = 255
        self.verder:int = 0
        self.azul:int = 0
        self.opacidad:int = 100

class Cafe(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'brown'
        self.rojo:int = 139
        self.verder:int = 69
        self.azul:int = 19
        self.opacidad:int = 100

class Gris(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'gray'
        self.rojo:int = 178
        self.verder:int = 190
        self.azul:int = 181
        self.opacidad:int = 100

class Pantone541(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'pantone541'
        self.rojo:int = 0
        self.verder:int = 66
        self.azul:int = 112
        self.opacidad:int = 100

class Pantone652(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'pantone652'
        self.rojo:int = 126
        self.verder:int = 155
        self.azul:int = 191
        self.opacidad:int = 100

class Pantone298(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'pantone298'
        self.rojo:int = 66
        self.verder:int = 180
        self.azul:int = 228
        self.opacidad:int = 100

class Transparente(Color):
    ''' Clase abstracta para el color rojo '''
    def __init__(self) -> None:
        self.nombre:str = 'transparent'
        self.rojo:int = 0
        self.verder:int = 0
        self.azul:int = 0
        self.opacidad:int = 50

@unique
class CatalogoColores(Enum):
    ''' Enumeracion de colores '''
    BLANCO       = Blanco()
    NEGRO        = Negro()
    ROJO         = Rojo()
    CAFE         = Cafe()
    GRIS         = Gris()
    PANTONE541   = Pantone541()
    PANTONE652   = Pantone652()
    PANTONE298   = Pantone298()
    TRANSPARENTE = Transparente()