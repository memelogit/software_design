# RELACIONES ENTRE CLASES Y OBJETOS

from __future__ import annotations
import random

# B Componente
class Estrella:
    def __init__(self) -> None:
        self.forma = random.choice( ['*', '.', '+'] )
    def __str__(self) -> str:
        return self.forma
    def __del__(self) -> None:
        print('-I- estrella eliminada')

# A Contenedor
class Cielo:
    def __init__(self, numero_de_estrellas:int) -> None:
        self.estrellas = [] # Composición -> Asociación
        for i in range(numero_de_estrellas):
            self.estrellas.append(Estrella())

    def mostrar_estrellas(self) -> None:
        for estrella in self.estrellas:
            print(estrella)

cielo1 = Cielo(5)
print('-I- Cielo 1')
cielo1.mostrar_estrellas()
del cielo1