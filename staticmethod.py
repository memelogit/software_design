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
    
    # La convención en métodos de clase es usar CLS en lugar de SELF
    @classmethod
    def modificar_mult(cls, valor):
        cls.mult_de_dosis = valor
    
    # Un uso práctico de los métodos de clase es un constructor alternativo
    @classmethod
    def from_csv(cls, gato_csv):
        nombre, edad, peso, color = gato_csv.split(',')
        return cls(nombre, edad, peso, color)
    
    # No pasamos la clase o la instancia como argumento en los métodos
    # estáticos
    @staticmethod
    def hora_de_jugar(HH24) -> bool:
        if HH24 >= 8 and HH24 <= 20:
            return True
        else:
            return False

tom = Gato('Tom', 3, 7, 'café')
print(Gato.hora_de_jugar(12))