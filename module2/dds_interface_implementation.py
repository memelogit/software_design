# 8 de Febrero
# Principios del diseño de software (3)

from abc import ABC

# Interface
class Alimento(ABC):
    def obtener_energia(self):
        ''' Retorna el valor de la energia de la salchicha '''
        return self._energia

# Clases concretas
class Salchicha(Alimento):
    def __init__(self, energia:int=18) -> None:
        self._energia = energia
class Raton(Alimento):
    def __init__(self, energia:int=40) -> None:
        self._energia = energia

# Clase Gato
class Gato:
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
        self._energia = 100
    
    def alimentar(self, alimento:Alimento) -> None:
        self._energia += alimento.obtener_energia() # Polimorfismo
        if self._energia > 100: self._energia = 100
    
    def jugar(self) -> None:
        ''' Gasta energia '''
        self._energia -= 30
    
    def __str__(self) -> str:
        return f'A nuestro gato {self.nombre} le queda {self._energia}% de energía'

# Testing
if __name__ == '__main__':
    tom = Gato('Tomás') #100%
    tom.jugar() # 70%
    print(tom)
    tom.alimentar(Raton()) # +18%
    print(tom)