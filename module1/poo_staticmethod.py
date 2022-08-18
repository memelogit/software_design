# Programación orientada a objetos > Conceptos básicos de POO y UML
from __future__ import annotations

class Gato:
    ''' Crea un objeto del tipo gato con características básicas '''
    # VARIABLE DE CLASE
    MULT_DE_DOSIS = 0.003

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
            # Las variables de clase se acceden usando la clase como tal
            # También se puede acceder a la variable usando la instancia
            #    self.MULT_DE_DOSIS
            self.peso * Gato.MULT_DE_DOSIS
        )
    
    # La convención en métodos de clase es usar CLS en lugar de SELF
    @classmethod
    def modificar_mult(cls, valor:float) -> None:
        ''' Modifica el valor de la variable de clase MULT_DE_DOSIS '''
        cls.MULT_DE_DOSIS = valor
    
    # Un uso práctico de los métodos de clase es un constructor alternativo
    @classmethod
    def from_csv(cls, gato_csv:str) -> Gato:
        ''' Permite crear un objeto a partir de un string en formato CSV '''
        # Asignación múltiple
        nombre, edad, peso, color = gato_csv.split(',')
        # Retornamos la referencia al objeto creado
        return cls(nombre, edad, peso, color)
    
    # No pasamos la clase o la instancia como argumento en los métodos
    # estáticos
    @staticmethod
    def hora_de_jugar(HH24:int) -> bool:
        ''' Retorna un valor booleano indicando si nuestro gato está dispuesto para jugar '''
        if HH24 >= 8 and HH24 <= 20:
            return True
        else:
            return False

tom = Gato('Tom', 3, 7, 'café')
print(Gato.hora_de_jugar(12))