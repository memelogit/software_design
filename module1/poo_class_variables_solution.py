# Programación orientada a objetos > Conceptos básicos de POO y UML

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

tom = Gato('Tom', 3, 7, 'café')
print(tom.vacunar())

# Podemos obtener el valor a pesar que no ser una variable de instancia
print('dosis:', tom.MULT_DE_DOSIS)

# Sin embargo, la variable MULT_DE_DOSIS no es parte del namespace
print(tom.__dict__)

# Al crear otra instancia y modificar el valor de MULT_DE_DOSIS, lo que en
# realidad hacemos es crear la variable de instancia MULT_DE_DOSIS
luna = Gato('Luna', 2, 5, 'gris')
luna.MULT_DE_DOSIS = 0.009
print(luna.__dict__)

# Para cambiar el valor de la variable de clase MULT_DE_DOSIS necesitamos
# acceder a la variable en la clase como tal
Gato.MULT_DE_DOSIS = 0.006

print('Modificación variable de clase', tom.vacunar())
print('Modificación variable de clase', tom.vacunar())