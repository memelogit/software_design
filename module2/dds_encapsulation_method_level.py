# Principios del diseño de software

from __future__ import annotations
from enum import Enum, unique

class Producto:
    ''' Define a un producto y adicionalmente nos dice la cantidad de productos necesarios para una orden '''
    def __init__(self, descripcion:str, cantidad:int, precio:float) -> None:
        self.descripcion:str = descripcion
        self.cantidad:int = cantidad
        self.precio:float = precio

class Orden:

    @unique
    class Pais(Enum):
        MEXICO = 'MX'
        USA    = 'US'

    def __init__(self, pais:Pais) -> None:
        self.pais:Orden.Pais = pais
        self.productos:list = [] # 
    
    def agregar(self, producto:Producto) -> None:
        ''' Agrega productos al carrito de compras '''
        self.productos.append(producto)
    
    def total_orden(self) -> float:
        ''' Retorna el valor total de la orden al leer cada producto y aumentar el impuesto
        correspondiente a cada país '''
        total = 0
        for p in self.productos:
            total += p.precio * p.cantidad
        
        if self.pais == Orden.Pais.USA:
            total += total*0.07
        elif self.pais == Orden.Pais.MEXICO:
            total += total*0.20
        else:
            raise RuntimeError('El país no está definido')
        
        return total

# Código Cliente
if __name__ == '__main__':
    carrito = Orden(Orden.Pais.MEXICO)
    carrito.agregar(Producto('Blusas azules', 4, 1200))
    carrito.agregar(Producto('Reloj Michael Kors', 1, 5800))
    carrito.agregar(Producto('Blusas Lacoste', 6, 799))

    print(carrito.total_orden())