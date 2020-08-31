from abc import ABC, abstractmethod

class Comida(ABC):
    @abstractmethod
    def obtenerEnergia(self):
        pass

class Salchicha(Comida):
    def __init__(self, energia = 18):
        self.__energia = energia
    
    def obtenerEnergia(self):
        return self.__energia

class Raton(Comida):
    def __init__(self, energia = 40):
        self.__energia = energia
    
    def obtenerEnergia(self):
        return self.__energia + 1

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__energia = 100
    
    # Ahora nuestro gato se puede alimentar con cualquier tipo de comida
    def alimentar(self, comida):
        self.__energia += comida.obtenerEnergia()
        if self.__energia > 100:
            self.__energia = 100
    
    def jugar(self):
        self.__energia -= 30
    
    def __str__(self):
        return 'a {} le queda {} porciento de energía'.format(
            self.nombre,
            self.__energia
        )

salchicha1 = Salchicha()
tom = Gato('Tomás')
tom.jugar()
print(tom)

tom.alimentar(salchicha1)
print(tom)

# Ahora probamos con un ratón
gusgus = Raton()
tom.jugar()
print(tom)
tom.alimentar(gusgus)
print(tom)