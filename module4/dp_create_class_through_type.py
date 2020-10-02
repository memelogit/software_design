class Prueba:
    pass

def funcion():
    pass

# Objeto del tipo funcion
print(type(funcion))

# Objeto del tipo Prueba
print(type(Prueba()))

# Nuestra clase es del tipo 'type'
print(type(Prueba))

# Dato nuestra clase Prueba es del tipo 'Type' entonces pasamos la información
# a esta clase
PruebaType = type('PruebaType', (), {})
print(type(PruebaType()))
print(type(PruebaType))

# Atributos
PruebaType = type('PruebaType', (), {'x': 5})
print(PruebaType().x)

# Herencia
class Foo:
    def info(self):
        return 'Hola mundo'
PruebaType = type('PruebaType', (Foo,), {})
print(PruebaType().info())

# Metdos
def metodo(self):
    self.attr = 11
PruebaType = type('PruebaType', (), {'metodo': metodo})
p = PruebaType()
p.metodo()
print(p.attr)