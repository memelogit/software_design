# Aplicación de E-Commerce en donde se tiene un método para
# calcular el total de la orden con impuestos

class Producto:
    def __init__(self, descripcion, cantidad, precio):
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio # Asumiremos un precio en pesos

# Extraemos el código y creamos una nueva clase para el manejo de impuestos
class Impuesto:

    mx = 0.20
    us = 0.07

    @classmethod
    def tasa_impuestos(cls, pais):
        if pais == 'US':
            return cls.mx
        elif pais == 'MX':
            return cls.us
        else:
            raise Exception('No se tiene el referencia de impuestos aún.')
    
    @classmethod
    def cambiar_valor(cls, pais, valor):
        pass

class Orden:
    def __init__(self, pais):
        self.pais = pais
        self.ordenes = []
    
    def agregar(self, producto):
        self.ordenes.append(producto)

    def total_orden(self):
        total = 0
        for orden in self.ordenes:
            total += orden.precio * orden.cantidad
        total += total * Impuesto.tasa_impuestos(self.pais)
        return total

victor = Orden('MX')
victor.agregar(Producto('Blusas azules', 5, 120))
victor.agregar(Producto('Bolsas Lacoste', 2, 4000))
victor.agregar(Producto('Reloj Michael Kors', 5, 8000))

print(victor.total_orden())

hugo = Orden('US')
hugo.agregar(Producto('Blusas azules', 5, 120))
hugo.agregar(Producto('Bolsas Lacoste', 2, 4000))
hugo.agregar(Producto('Reloj Michael Kors', 5, 8000))

print(hugo.total_orden())