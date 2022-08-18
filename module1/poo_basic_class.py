# Programación orientada a objetos > Conceptos básicos de POO y UML

class Gato:
    ''' Crea un objeto del tipo gato con características básicas '''
    # Recibimos la instancia como primer argumento
    # Podemos nombrar al argumento diferente pero por convención usamos self
    def __init__(self, nombre:str, edad:int, peso:float, color:str):
        # VARIABLES DE INSTANCIA
        self.nombre:str = nombre
        self.edad:int = edad
        self.peso:float = peso
        self.color:str = color
    
    # El argumento self se pasa de manera automática
    def detalles(self) -> str:
        ''' Muestra los detalles del objeto tipo gato '''
        # A continuación se utiliza el método format para reemplazar valores de
        # variables en un string
        return '{} es un gato de {} años color {} que pesa {} kilos.'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )

# Creamos el objeto del tipo gato
tom = Gato('Tom', 3, 7, 'café')
print(tom.detalles())

# Incluso podemos acceder al método detalles y pasar la INSTANCIA 'tom'
print(Gato.detalles(tom))