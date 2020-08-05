from abc import ABC

class Animal:
    def __init__(self):
        pass

class CuatroPatas(ABC):
    def __init__(self):
        pass

    def respirar(self):
        return 'respirando...'

class Respirador(ABC):
    def __init__(self):
        pass

    def correr(self, destino = 'casa'):
        return 'corriendo a {}'.format(destino)

class Gato(Animal, CuatroPatas, Respirador):
    def __del__(self):
        print('el gatito murió')

tom = Gato()
print(tom.respirar())
print(tom.correr('callejón'))
