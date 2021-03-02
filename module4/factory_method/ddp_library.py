from abc import ABC, abstractmethod
from enum import Enum

# -----------------------------------------------------------------------------
# 1.- INTERFACE PARA LOS PRODUCTOS
# -----------------------------------------------------------------------------
class Bloque(ABC):
    @abstractmethod
    def colocar(self) -> str:
        pass

class Arma(ABC):
    @abstractmethod
    def usar(self) -> str:
        pass

# -----------------------------------------------------------------------------
# 2.- PRODUTOS CONCRETOS
# -----------------------------------------------------------------------------
class Piedra(Bloque):
    def colocar(self) -> str:
        print("-I- Bloque del tipo 'piedra' insertado")

class Granito(Bloque):
    def colocar(self) -> str:
        print("-I- Bloque del tipo 'granito' insertado")

class Pasto(Bloque):
    def colocar(self) -> str:
        print("-I- Bloque del tipo 'pasto' insertado")

class Horno(Bloque):
    def colocar(self) -> str:
        print("-I- Bloque del tipo 'horno' insertado")

class CamaPiedra(Bloque):
    def colocar(self) -> str:
        print("-I- Bloque del tipo 'cama de piedra' insertado")

# -----------------------------------------------------------------------------
# 3.- FACTORY (CREADOR)
# -----------------------------------------------------------------------------
class Mundo:
    @abstractmethod
    def crear_bloque(self, tipo) -> Bloque:
        pass

    def colocar(self, tipo) -> str:
        bloque = self.crear_bloque(tipo)
        return bloque.colocar()
    
    def minar(self, bloque) -> None:
        pass

# -----------------------------------------------------------------------------
# 4.- FACTORIES EN CONCRETO
# -----------------------------------------------------------------------------
class ModoCreativo(Mundo):

    class TipoBloque(Enum):
        PIEDRA         = Piedra()
        GRANITO        = Granito()
        PASTO          = Pasto()
        CAMA_DE_PIEDRA = CamaPiedra()

    def crear_bloque(self, tipo: TipoBloque) -> Bloque:
        return tipo.value

class ModoSupervivencia(Mundo):

    class TipoBloque(Enum):
        PIEDRA         = Piedra()
        GRANITO        = Granito()
        PASTO          = Pasto()
        HORNO          = Horno()

    def crear_bloque(self, tipo: TipoBloque) -> Bloque:
        return tipo.value