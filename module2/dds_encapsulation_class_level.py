# Principios del diseño de software

from __future__ import annotations
from ast import Or
from enum import Enum, unique

class Producto:
    ''' Define a un producto y adicionalmente nos dice la cantidad de productos necesarios para una orden '''
    def __init__(self, descripcion:str, cantidad:int, precio:float) -> None:
        self.descripcion:str = descripcion
        self.cantidad:int = cantidad
        self.precio:float = precio

class Orden:

    # Encapsulamiento a nivel de clase en donde nosotros podemos definir
    # mas paises en un futuro "Encapsula lo que varía"
    @unique
    class Pais(Enum):
        #name      = value
        MEXICO     = 0.20
        USA        = 0.07
        COSTA_RICA = 0.12

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
        total += total * self.pais.value
        
        return total

# Código Cliente
if __name__ == '__main__':
    carrito = Orden(Orden.Pais.COSTA_RICA)
    carrito.agregar(Producto('Blusas azules', 4, 1200))
    carrito.agregar(Producto('Reloj Michael Kors', 1, 5800))
    carrito.agregar(Producto('Blusas Lacoste', 6, 799))

    print(carrito.total_orden())