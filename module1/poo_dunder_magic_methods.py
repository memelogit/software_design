# Programación orientada a objetos > Conceptos básicos de POO y UML

from typing_extensions import LiteralString
from __future__ import annotations

class Animal:
    ''' Crea un objeto del tipo animal '''

    VIDAS = 1

    def __init__(self, nombre:str, edad:int, peso:float, color:str):
        self.nombre:str = nombre
        self.edad:int = edad
        self.peso:float = peso
        self.color:str = color
    
    def __repr__(self) -> str:
        return 'Animal({}, {}, {}, {})'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )
    
    def __str__(self) -> str:
        return self.detalles()
    
    def __add__(self, other:Animal) -> LiteralString:
        return 'juntos pesan {} kg.'.format(
            self.peso + other.peso
        )
    
    def detalles(self) -> str:
        ''' Regresa los detalles asociados a un animal '''
        return '{} es un animal de {} años color {} que pesa {} kilos.'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )

tom = Animal('Tom', 3, 7, 'café')
# Ahora en lugar de imprimir el puntero a la instancia, se imprime una
# representación personalizada del objeto
print(tom)

print(repr(tom))
print(str(tom))

# Ahora podemos sumar los pesos de nuestros animales
# Mas información en este link:
#   https://docs.python.org/2.0/ref/numeric-types.html
benji = Animal('Benji', 2, 10, 'capuchino')
print(tom + benji)

# Algunos dunder methos interesantes
# __len__
# __containts__ -> Cuando usamos el operador in, regresa un bool
# __add__, __iadd__
# __sub__, __mul__