from __future__ import annotations

class Superheroe:
    ''' Clase A: Que representa al principal objeto que agrega elementos de la clase B '''

    def __init__(self, nombre:str, ataque:int=10, armas:list=[], equipo:str='') -> None:
        self.nombre:str = nombre
        self.ataque:int = ataque
        self.equipo:str = equipo
        self.armas:list = armas # <- Relación de agregación
        self.salud = 100
    
    def __str__(self) -> str:
        ''' Retorna los datos del superheroes '''
        return f'nombre={self.nombre}, salud={self.salud}, armas={len(self.armas)}'
    
    def __del__(self) -> str:
        print(f'Nuestro personaje llamado {self.nombre} murió')
        return f'Nuestro personaje llamado {self.nombre} murió'
    
    def atacar(self, otro:Superheroe) -> None:
        ''' Simula el ataque del superheroe a otro. Le reduce la vida '''
        print(f'{self.nombre} está peleandpo con {otro.nombre}')
        for arma in self.armas:
            print(f'  atacando con {arma.nombre}')
            otro.salud -= self.ataque + arma.destruccion
            arma.resistencia -= 1

class Arma:
    ''' Clase B: Que contine el objeto el cual será "agregado" a la clase A '''
    def __init__(self, nombre:str, resistencia:int, destruccion:int) -> None:
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion
    
    def __str__(self) -> str:
        ''' Retorna el nombre de la empresa '''
        return f'{self.nombre}'

# Código Cliente
if __name__ == '__main__':
    # Armas que son los componentes
    martillo = Arma(
        resistencia=6,
        nombre='Martillo',
        destruccion=7
    )
    
    rayo = Arma(
        resistencia=1,
        nombre='Rayo',
        destruccion=10
    )
    
    arco = Arma(
        resistencia=4,
        nombre='Arco',
        destruccion=3
    )

    # Superheroes que son los contenedores
    thor = Superheroe(
        nombre = 'Thor dios del trueno',
        ataque=20,
        armas=[martillo, rayo] # Asociación que se especializa en una "agregación"
    )

    ojo_de_halcón = Superheroe(
        nombre = 'Ojo de Halcón',
        ataque=14,
        armas=[arco] # Asociación que se especializa en una "agregación"
    )

    # Pongámoslos a pelear
    print(ojo_de_halcón)
    thor.atacar(ojo_de_halcón)
    print(ojo_de_halcón)

    del thor
    ojo_de_halcón.armas.append(martillo)
    print(ojo_de_halcón)