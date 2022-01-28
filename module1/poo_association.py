# RELACIONES ENTRE CLASES Y OBJETOS

from __future__ import annotations

# A
class Persona:
    def __init__(self, nombre:str, empresa:Empresa) -> None:
        self.nombre = nombre
        self.empresa = empresa # <- Aquí se da la asociación
    def __str__(self) -> str:
        return f'{self.nombre} trabaja en una empresa de {self.empresa.enfoque} llamada {self.empresa}'

# B
class Empresa:
    def __init__(self, nombre:str, enfoque:str) -> None:
        self.nombre = nombre
        self.enfoque = enfoque
    def __str__(self) -> str:
        return self.nombre

iteso = Empresa('ITESO', 'educación')
victor = Persona('Víctor', iteso)
print(victor)