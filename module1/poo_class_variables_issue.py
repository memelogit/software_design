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
        return '{} es un gato de {} años color {} que pesa {} kilos.'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )
    
    def vacunar(self) -> str:
        ''' Regresa en un string cuantos litros de medicamento hay que suministrar a nuestro gato '''
        return 'suministramos {} litros contra la rinotraqueitis'.format(
            # Multiplicamos el peso por un valor fijo
            # ¿Qué pasaría si necesitamos cambiar el valor más adelante?
            self.peso * 0.003
        )

tom = Gato('Tom', 3, 7, 'café')
print(tom.vacunar())
