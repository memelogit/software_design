from __future__ import annotations
from abc import ABC, abstractmethod
from random import choice, randint
from typing import List

# Publisher
class Apple:
    _producto: str = None
    _suscriptores: List[Suscriptor] = []

    def suscribir(self, observer: Suscriptor) -> None:
        print("-I- Apple: suscriptor agregardo")
        self._suscriptores.append(observer)

    def cancelar_suscripcion(self, observer: Suscriptor) -> None:
        self._suscriptores.remove(observer)

    def notificar(self) -> None:
        for observer in self._suscriptores:
            observer.actualizar(self)

    def liberar_producto(self) -> None:
        self._producto = choice(['iphone', 'ipad', 'imac', 'iwatch', 'appletv'])
        print(f"-I- Apple: Se ha liberado un nuevo producto: {self._producto}")
        self.notificar()

# Interfaz suscriptores
class Suscriptor(ABC):
    @abstractmethod
    def actualizar(self, empresa: Apple) -> None:
        pass

# Suscriptores concretos
class AppleStore(Suscriptor):
    def actualizar(self, empresa: Apple) -> None:
      print(f"    AppleStore: Recibió al anuncio, pidiendo {randint(50, 100)} {empresa._producto}")

class Liverpool(Suscriptor):
    def actualizar(self, empresa: Apple) -> None:
        if empresa._producto in ['iphone', 'ipad']: # Solamente estamos interesados en estos productos
          print(f"    Liverpool: Recibió al anuncio, pidiendo {randint(10, 50)} productos")
        else:
          print("    Liverpool no esta interesado en este producto")

# Codigo del cliente
if __name__ == "__main__":


    apple_store_galerias = AppleStore()
    liverpool = Liverpool()
    
    empresa = Apple()
    empresa.suscribir(apple_store_galerias)
    empresa.suscribir(liverpool)

    empresa.liberar_producto()
    empresa.liberar_producto()

    empresa.cancelar_suscripcion(apple_store_galerias)
    empresa.liberar_producto()