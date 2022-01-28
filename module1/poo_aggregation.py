from __future__ import annotations

class Superheroe:

    def __init__(self, nombre:str, ataque:int, armas:list = []):
        self.nombre = nombre
        self.ataque = ataque
        self.armas = armas
        self.salud = 100
    
    def __str__(self):
        return f'-I- nombre={self.nombre}, salud={self.salud}, armas={len(self.armas)}'
    
    def atacar(self, otro:Superheroe):
        ''' Atacta al oponente con todas las armas '''
        print(f'-I- {self.nombre} peleando con {otro.nombre}')
        for arma in self.armas:
            print(f'    Atacando con {arma.nombre}')
            otro.salud -= self.ataque + arma.destruccion
            arma.resistencia -= 1

class Arma:
    def __init__(self, nombre:str, resistencia:int, destruccion:int):
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion

    def __str__(self):
        return self.nombre

# Componentes
martillo = Arma('Martillo', 6, 6)
rayo = Arma('Rayo', resistencia=1, destruccion=10)
arco = Arma('Arco', 4, 3)

# Contenedores: En la composición un contenedor "usa o tiene" componentes
thor = Superheroe('Thor', 20, [martillo, rayo])
ojo_halcon = Superheroe('Ojo del Halcon', 18, [arco])

print(ojo_halcon)
thor.atacar(ojo_halcon)
print(ojo_halcon)

# Al eliminar a los superheroes aun conservamos las armas
del thor
print('resistencia del martillo:', martillo.resistencia)
