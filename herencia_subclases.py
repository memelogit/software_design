class Animal:

    vidas = 1

    def __init__(self, nombre, edad, peso, color):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
    
    def detalles(self):
        return '{} es un animal de {} años color {} que pesa {} kilos.'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )
    
    @classmethod
    def obtener_vidas(cls):
        return cls.vidas

    def respirar(self):
        pass

class Gato(Animal):

    # Podemos modificar variables de clase en una subclase
    vidas = 9

    def __init__(self, nombre, edad, peso, color, limpio):
        super().__init__(nombre, edad, peso, color)
        self.limpio = limpio

    def meow(self):
        pass

class Perro(Animal):
    def ladrar(self):
        pass

tom = Gato('Tom', 3, 7, 'café', limpio=True)
print(tom.detalles())
print(tom.obtener_vidas())

# Con el método isinstance() sabemos si una instancia pertenece a una clase
print(isinstance(tom, Animal))

# Con el método help() sabemos detalles adicionales de la herencia tales como
# el orden de resolución de métodos o las variables de clase
# print(help(tom))