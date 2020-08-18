from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacerSonido(self):
        pass

class Gato(Animal):
    def hacerSonido(self):
        return 'Meow!'

class Perro(Animal):
    def hacerSonido(self):
        return 'Woof!'

tom = Gato()
benji = Perro()
bolsa = [tom, benji, Gato()]

for animal in bolsa:
    print(animal.hacerSonido())

# No se pueden instanciar clases abstractas
# vaca = Animal()