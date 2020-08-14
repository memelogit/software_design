class Superheroe:

    def __init__(self, nombre, ataque, arma):
        self.nombre = nombre
        self.ataque = ataque
        self.arma = arma
        self.salud = 100
    
    def __str__(self):
        return self.nombre
    
    def atacar(self, otro):
        otro.salud -= self.ataque + self.arma.destruccion
        self.arma.resistencia -= 1

class Arma:

    def __init__(self, nombre, resistencia, destruccion):
        self.nombre = nombre
        self.resistencia = resistencia
        self.destruccion = destruccion

    def __str__(self):
        return self.nombre

# Al eliminar a los superheroes aun conservamos las armas
martillo = Arma('Martillo', 10, 6)
arco = Arma('Arco', 7, 3)

thor = Superheroe('Thor', 20, martillo)
ojo_halcon = Superheroe('Ojo del Halcon', 18, arco)

print('Salud de thor:', ojo_halcon.salud)
thor.atacar(ojo_halcon)
print('Salud de thor:', ojo_halcon.salud)
print('resistencia arco:', martillo.resistencia)