from abc import ABC, abstractmethod
from enum import Enum

# 1.- Productos abstractos
# Los Productos Abstractos declaran interfaces para un grupo de productos
# diferentes pero relacionados que forman una familia de productos.
class Arquero(ABC):
    @abstractmethod
    def tirar(self):
        pass

class Aldeano(ABC):
    @abstractmethod
    def recolectar(self):
        pass

class Milicia(ABC):
    @abstractmethod
    def atacar(self):
        pass

# 2.- Productos concretos
# Los Productos Concretos son implementaciones distintas de productos abstractos
# agrupados por variantes. Cada producto abstracto debe implementarse en todas
# las variantes dadas

# --- Arqueros (Producto concreto)
class ArqueroCelta(Arquero):
    def __init__(self):
        self.ataque = 4
        self.defensa = 6
        self.tiempo_entrenamiento = 3
        print('Arquero Celta creado...')

    def tirar(self):
        print(f'-I- El arquero Celta atacó con un daño de {self.ataque}')

class ArqueroChino(Arquero):
    def __init__(self):
        self.ataque = 2
        self.defensa = 7
        self.tiempo_entrenamiento = 1
        print('Arquero Chino creado...')

    def tirar(self):
        print(f'-I- El arquero Chino atacó con un daño de {self.ataque}')

class ArqueroAzteca(Arquero):
    def __init__(self):
        self.ataque = 3
        self.defensa = 5
        self.tiempo_entrenamiento = 2
        print('Arquero Azteca creado...')

    def tirar(self):
        print(f'-I- El arquero Azteca atacó con un daño de {self.ataque}')

# --- Aldeanos (Producto concreto)
class AldeanoCelta(Aldeano):
    def __init__(self):
        self.tiempo_entrenamiento = 1
        print('Aldeano Celta creado...')

    def recolectar(self):
        print(f'-I- El aldeano Celta está recolectando recursos en Irlanda')

class AldeanoChino(Aldeano):
    def __init__(self):
        self.tiempo_entrenamiento = 1
        print('Aldeano Chino creado...')

    def recolectar(self):
        print(f'-I- El aldeano Chino está recolectando recursos en China oriental')

class AldeanoAzteca(Aldeano):
    def __init__(self):
        self.tiempo_entrenamiento = 2
        print('Aldeano Azteca creado...')

    def recolectar(self):
        print(f'-I- El aldeano Azteca está recolectando recursos en México')

# --- Milicia (Producto concreto)
class MiliciaCelta(Milicia):
    def __init__(self):
        self.ataque = 12
        self.defensa = 8
        self.tiempo_entrenamiento = 3
        print('Milicia Celta creada...')

    def atacar(self):
        print(f'-I- La milicia Celta atacó con un daño de {self.ataque}')

class MiliciaChina(Milicia):
    def __init__(self):
        self.ataque = 14
        self.defensa = 5
        self.tiempo_entrenamiento = 3
        print('Milicia China creada...')

    def atacar(self):
        print(f'-I- La milicia China atacó con un daño de {self.ataque}')

class MiliciaAzteca(Milicia):
    def __init__(self):
        self.ataque = 11
        self.defensa = 10
        self.tiempo_entrenamiento = 4
        print('Milicia Azteca creada...')

    def atacar(self):
        print(f'-I- La milicia Azteca atacó con un daño de {self.ataque}')

# 3.- Fábrica abstracta
# La Fábrica Abstracta declara un grupo de métodos para crear cada uno de los
# productos abstractos.
class Civilizacion(ABC):
    @abstractmethod
    def crear_arquero(self):
        pass

    @abstractmethod
    def crear_aldeano(self):
        pass

    @abstractmethod
    def crear_milicia(self):
        pass

# 4.- Fábricas concretas
# Las Fábricas Concretas implementan métodos de creación de la fábrica
# abstracta. Cada fábrica concreta se corresponde con una variante específica
# de los productos y crea tan solo dichas variantes de los productos.
class Celtas(Civilizacion):
    def crear_arquero(self):
        return ArqueroCelta()

    def crear_aldeano(self):
        return AldeanoCelta()

    def crear_milicia(self):
        return MiliciaCelta()

class Chinos(Civilizacion):
    def crear_arquero(self):
        return ArqueroChino()

    def crear_aldeano(self):
        return AldeanoChino()

    def crear_milicia(self):
        return MiliciaChina()

class Aztecas(Civilizacion):
    def crear_arquero(self):
        return ArqueroAzteca()

    def crear_aldeano(self):
        return AldeanoAzteca()

    def crear_milicia(self):
        return MiliciaAzteca()

# 5.- Código para el cliente
class AgeOfEmpire:

    class Civilizaciones(Enum):
        CELTA        = Celtas()
        CHINA        = Chinos()
        AZTECA      = Aztecas()

    @classmethod
    def crearMundo(cls, tipo: Civilizaciones) -> Civilizacion:
        return tipo.value

# Codigo cliente
# Cuando yo llame al archivo con python ddp_library.py
if __name__ == "__main__":
    mundo = AgeOfEmpire.crearMundo(AgeOfEmpire.Civilizaciones.AZTECA)

    # El codigo del juego
    aldeano1 = mundo.crear_aldeano() # Boton de crear aldeano
    arquero1 = mundo.crear_arquero()
    milicia1 = mundo.crear_milicia()
    aldeano1.recolectar()
    milicia1.atacar()