class Empresa:

    def __init__(self, nombre, enfoque):
        self.nombre = nombre
        self.enfoque = enfoque
    
    def __str__(self):
        return self.nombre

class Persona:

    def __init__(self, nombre, empresa):
        self.nombre = nombre
        self.empresa = empresa
    
    def __str__(self):
        return '{} trabaja en una empresa de {} llamada {}'.format(
            self.nombre,
            self.empresa.enfoque,
            self.empresa
        )

oracle = Empresa('ITESO', 'educación')
victor = Persona('Victor', oracle)
print(victor)