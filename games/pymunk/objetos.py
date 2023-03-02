from abc import ABC
import math
from typing import Tuple
import pygame
from pygame import Surface
from pymunk import Body, Circle, Poly, Shape, Space
from colores import CatalogoColores, Color

class Objeto(ABC):
    ''' Interface de la clase objeto '''

    def __init__(self, espacio:Space, color:Color = CatalogoColores.ROJO, estilo:int = Body.DYNAMIC) -> None:
        self.espacio:Space = espacio
        self.color:Color = color
        self.cuerpo:Body = Body(body_type=estilo)
        self.masa:int = 10
        self.elasticidad:float = 0.9
        self.friccion:float = 10.0

    def colocar(self, posicion:Tuple[int, int]) -> Circle:
        self.cuerpo.position:Tuple[int, int] = posicion
        self.forma.mass:int = self.masa
        self.forma.elasticity:float = self.elasticidad
        self.forma.friction:float = self.friccion
        self.forma.color:Color = self.color.value.rgba
        self.espacio.add(self.cuerpo, self.forma)
        return self.forma

class Circulo(Objeto):
    ''' Objeto concreto Circulo '''

    def __init__(self, espacio:Space, radio:int, color:Color = CatalogoColores.ROJO, estilo:int = Body.DYNAMIC) -> None:
        super().__init__(espacio, color, estilo)
        self.radio:int = radio
        self.forma:Shape = Circle(self.cuerpo, radio)
        self.imagen = pygame.image.load(r"C:\ITESO\diseño de software\code\games\pymunk\bird1.png")
        self.imagen = pygame.transform.scale(self.imagen, (radio*3, radio*3))

class Rectangulo(Objeto):
    ''' Objeto concreto Rectángulo '''

    def __init__(self, espacio:Space, ancho:int, alto:int, color:Color = CatalogoColores.ROJO, estilo:int = Body.DYNAMIC) -> None:
        super().__init__(espacio, color, estilo)
        self.ancho:int = ancho
        self.alto:int = alto
        self.forma:Shape = Poly.create_box(self.cuerpo, (self.ancho, self.alto), 1)

class Linea:
    def __init__(self, ancho:int = 1) -> None:
        self.posicion_inicial:Tuple[int, int] = None
        self.posicion_final:Tuple[int, int] = None
        self.ancho:int = ancho
    
    @property
    def disponible(self) -> bool:
        ''' Retorna True si las dos posiciones ya fueron definidas '''
        return self.posicion_inicial != None and self.posicion_final != None

    @property
    def delta_x(self) -> int:
        ''' Retorna el valor de la diferencia entre la posición inicial menos la final '''
        return self.posicion_inicial[0] - self.posicion_final[0] if self.disponible else None

    @property
    def delta_y(self) -> int:
        ''' Retorna el valor de la diferencia entre la posición inicial menos la final '''
        return self.posicion_inicial[1] - self.posicion_final[1] if self.disponible else None
    
    @property
    def magnitud(self) -> int:
        ''' Retorna la magnitud de la linea '''
        return int(math.sqrt(self.delta_x**2 + self.delta_y**2)) if self.disponible else None

    def limpiar(self) -> None:
        ''' Remueve los valores de las posiciones inicial y final '''
        self.posicion_inicial = None
        self.posicion_final = None