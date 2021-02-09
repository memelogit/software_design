# Aplicación de E-Commerce en donde se tiene un método para
# calcular el total de la orden con impuestos

class Producto:
    def __init__(self, descripcion, cantidad, precio):
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio # Asumiremos un precio en pesos

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
        total += total * self.tasa_impuestos()
        return total
    
    # Extraemos el código que determina la tasa de impuestos
    def tasa_impuestos(self):
        if self.pais == 'US':
            return 0.07
        elif self.pais == 'MX':
            return 0.20
        else:
            raise Exception('No se tiene el referencia de impuestos aún.')

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