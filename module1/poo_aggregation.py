# RELACIONES ENTRE CLASES Y OBJETOS

from __future__ import annotations

# A
class Superheroe:
    def __init__(self, nombre:str, ataque:int, armas:list=[], equipo:str = '') -> None:
        self.nombre = nombre
        self.ataque = ataque
        self.equipo = equipo # [Un elemento] Asociación, relación 1 a 1
        self.armas = armas   # [Lista de elementos] Asociación -> Agregación, relación 1 a muchos
        self.salud = 100
    def __str__(self) -> str:
        return f'-I- nombre={self.nombre}, salud={self.salud}, armas={len(self.armas)}'
    def __del__(self) -> str:
        print(f'-I- Nuestro personaje murió {self.nombre}')
    def atacar(self, otro:Superheroe):
        print(f'-I- {self.nombre} está peleando con {otro.nombre}')
        for arma in self.armas:
            print(f'    Atacando con {arma.nombre}')
            otro.salud -= self.ataque + arma.destruccion
            arma.resistencia -= 1

# B
class Arma:
    def __init__(self, nombre:str, resistencia:int, destruccion:int) -> None:
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion
    def __str__(self) -> str:
        return self.nombre

# Componentes
martillo = Arma(
    nombre='Martillo',
    resistencia=6,
    destruccion=6
)
rayo = Arma(
    nombre='Rayo',
    resistencia=1,
    destruccion=10
)
arco = Arma(
    nombre='Arco',
    resistencia=4,
    destruccion=3
)

# Contenedores: En la composición un contenedor "usa o tiene" componentes
thor = Superheroe(
    nombre='Thor',
    ataque=20,
    armas=[rayo, martillo] # Asociación -> Agregación
)
ojo_halcon = Superheroe(
    nombre='Ojo de Halcón',
    ataque=18,
    armas=[arco] # Asociación -> Agregación
)

# Pongámoslos a pelear
print(ojo_halcon)
thor.atacar(ojo_halcon)
print(ojo_halcon)

# Al eliminar a los superheroes aun se siguen conservando las armas
del thor
print(f'-I- Resistencia del martillo: {martillo.resistencia}')
