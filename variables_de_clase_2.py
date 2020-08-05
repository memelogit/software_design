class Gato:

    # VARIABLE DE CLASE
    mult_de_dosis = 0.003

    # Recibimos la instancia como primer argumento
    # Podemos nombrar al argumento diferente pero por convención usamos self
    def __init__(self, nombre, edad, peso, color):
        # Definimos VARIABLES DE INSTANCIA
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
    
    def vacunar(self):
        return 'suministramos {} litros contra la rinotraqueitis'.format(
            # Las variables de clase se acceden usando la clase como tal
            # También se puede acceder a la variable usando la instancia
            #    self.mult_de_dosis
            self.peso * Gato.mult_de_dosis
        )

tom = Gato('Tom', 3, 7, 'café')
print(tom.vacunar())

# Podemos obtener el valor a pesar que no ser una variable de instancia
print('dosis:', tom.mult_de_dosis)

# Sin embargo, la variable mult_de_dosis no es parte del namespace
print(tom.__dict__)

# Al crear otra instancia y modificar el valor de mult_de_dosis, lo que en
# realidad hacemos es crear la variable de instancia mult_de_dosis
luna = Gato('Luna', 2, 5, 'gris')
luna.mult_de_dosis = 0.009
print(luna.__dict__)

# Para cambiar el valor de la variable de clase mult_de_dosis necesitamos
# acceder a la variable en la clase como tal
Gato.mult_de_dosis = 0.006

print('Modificación variable de clase', tom.vacunar())
print('Modificación variable de clase', tom.vacunar())