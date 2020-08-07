class Animal:

    vidas = 1

    def __init__(self, nombre, edad, peso, color):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
    
    def __repr__(self):
        return 'Animal({}, {}, {}, {})'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )
    
    def __str__(self):
        return self.detalles()
    
    def __add__(self, other):
        return 'juntos pesan {} kg.'.format(
            self.peso + other.peso
        )
    
    def detalles(self):
        return '{} es un animal de {} años color {} que pesa {} kilos.'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )

tom = Animal('Tom', 3, 7, 'café')
# Ahora en lugar de imprimir el puntero a la instancia, se imprime una
# representación personalizada del objeto
print(tom)

print(repr(tom))
print(str(tom))

# Ahora podemos sumar los pesos de nuestros animales
# Mas información en este link:
#   https://docs.python.org/2.0/ref/numeric-types.html
benji = Animal('Benji', 2, 10, 'capuchino')
print(tom + benji)