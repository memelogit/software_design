import random

class Estrella:
    def __init__(self):
        self.forma = random.choice(['*', '.', '+'])
    
    def __str__(self):
        return self.forma

class Cielo:
    def __init__(self, numero_estrellas):
        self.estrellas = []
        for i in range(numero_estrellas):
            self.estrellas.append(Estrella())
    
    def mostrar_estrellas(self):
        for i in self.estrellas:
            print(i)

# El cielo está compuesto de estrellas. Al eliminar los objetos cielo1 y cielo2
# también eliminamos las estrellas
cielo1 = Cielo(5)
cielo2 = Cielo(8)
cielo1.mostrar_estrellas()