class Gato:
    # Recibimos la instancia como primer argumento
    # Podemos nombrar al argumento diferente pero por convención usamos self
    def __init__(self, nombre, edad, peso, color):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.color = color
    
    # El argumento self se pasa de manera automática
    def detalles(self):
        return '{} es un gato de {} años color {} que pesa {} kilos.'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )

tom = Gato('Tom', 3, 7, 'café')
print(tom.detalles())

# Incluso podemos acceder al método detalles y pasar la INSTANCIA 'tom'
print(Gato.detalles(tom))