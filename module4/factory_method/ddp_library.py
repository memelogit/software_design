# DISEÑO DE SOFTWARE
# MODULO 4 - PATRONES DE DISEÑO
# FACTORY METHOD
# 27 DE MARZO 2023

from abc import ABC, abstractmethod
from enum import Enum

# 1.- Interface para productos
class Bloque(ABC):
    def colocar(self) -> str:
        ''' Coloca un nuevo tipo de bloque en el mapa '''
        pass

# 2.- Productos Concretos
class Piedra(Bloque):
    def colocar(self) -> str:
        ''' Coloca un nuevo tipo de bloque en el mapa '''
        return 'El bloque del tipo piedra fue insertado'

class Granito(Bloque):
    def colocar(self) -> str:
        ''' Coloca un nuevo tipo de bloque en el mapa '''
        return 'El bloque del tipo granito fue insertado'

class Pasto(Bloque):
    def colocar(self) -> str:
        ''' Coloca un nuevo tipo de bloque en el mapa '''
        return 'El bloque del tipo pasto fue insertado'

class Horno(Bloque):
    def colocar(self) -> str:
        ''' Coloca un nuevo tipo de bloque en el mapa '''
        return 'El bloque del tipo horno fue insertado'

class CamaPiedra(Bloque):
    def colocar(self) -> str:
        ''' Coloca un nuevo tipo de bloque en el mapa '''
        return 'El bloque del tipo cama_de_piedra fue insertado'

# 3.- Factory (Clase creadora)
class Mundo:
    @abstractmethod
    def crear_bloque(self, tipo) -> Bloque:
        ''' Crea un nuevo tipo de bloque desde el inventario de productos '''
        return tipo.value

    def colocar(self, tipo) -> str:
        ''' Coloca un nuevo tipo de bloque en el mapa '''
        return self.crear_bloque(tipo).colocar()

# 4.- Fabricas concretas
class ModoCreativo(Mundo):

    class TipoBloque(Enum):
        # name           # value
        PIEDRA           = Piedra()
        GRANITO          = Granito()
        PASTO            = Pasto()
        CAMA_DE_PIEDRA   = CamaPiedra()

class ModoSupervivencia(Mundo):
    class TipoBloque(Enum):
        PIEDRA           = Piedra()
        GRANITO          = Granito()
        PASTO            = Pasto()
        HORNO            = Horno()

if __name__ == '__main__':
    mundo = ModoCreativo()

    p1 = mundo.crear_bloque(mundo.TipoBloque.CAMA_DE_PIEDRA)
    print(p1.colocar())