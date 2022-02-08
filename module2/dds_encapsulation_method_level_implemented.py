#8 de Febrero
# Principios del diseño de software (3)

class Producto:
    def __init__(self, descripcion:str, cantidad:int, precio:float) -> None:
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

class Orden:
    def __init__(self, pais:str) -> None:
        self.pais = pais
        self.productos = []
    
    def agregar(self, producto:Producto) -> None:
        ''' Agregamos productos a nuestra orden '''
        self.productos.append(producto)
    
    def total_orden(self):
        ''' Tomando en cuenta los impuestos, calcilams el toral de la orden '''
        total = 0
        for p in self.productos:
            total += p.precio * p.cantidad
        total += total * self.tasa_impuestos()
        return total

    def tasa_impuestos(self):
        ''' Retorna el valor del impuesto a aplicar o levanta un error si no encuentra el país '''
        if self.pais == 'US':
            return 0.07
        elif self.pais == 'MX':
            return 0.20
        elif self.pais == 'Canada':
            return 0.01
        else:
            raise Exception(f'El pais {self.pais} no está definido en el método tasa_impuestos')


if __name__ == '__main__':
    # Este código solamente se va a ejecutar si lo corremos desde el thread principal
    # python code.py

    # main.py
    # > import code
    # > from code import Orden
    # Este código no se corre
    victor = Orden('Canada')
    victor.agregar(Producto('Blusas rosas', 2, 120))
    victor.agregar(Producto('Bolsas', 3, 1500))
    victor.agregar(Producto('Reloj', 5, 2000))

    print(victor.total_orden())