from abc import ABC, abstractmethod
from getpass import getpass

# -----------------------------------------------------------------------------
# 4.- Clase receptora
# Normalmente una clase ya existente a la que incluso el cliente tiene acceso
# -----------------------------------------------------------------------------
class Supermercado:

    # Simulemos una base de datos
    productos = {
        'a0001': {'nombre': 'papitas', 'precio': 12.00},
        'a0002': {'nombre': 'tajin', 'precio': 9.50},
        'a0003': {'nombre': 'salsa valentina', 'precio': 10.00},
        'b0001': {'nombre': 'fabuloso 5L', 'precio': 33.40},
        'b0002': {'nombre': 'fabuloso 750ml', 'precio': 10.50},
        'b0003': {'nombre': 'suavitel 1L', 'precio': 25.20},
        'c0001': {'nombre': 'mango 1k', 'precio': 18.70},
        'c0002': {'nombre': 'sandia 1k', 'precio': 22.50},
        'c0003': {'nombre': 'platano 1k', 'precio': 8.20}
    }

    descuentos = {
        'a0003': 0.40,
        'b0002': 0.20
    }

    @classmethod
    def codigo_a_precio(cls, codigo: str) -> float:
        if cls.productos.get(codigo):
            return cls.productos[codigo]['precio']
        else:
            return None
    
    @classmethod
    def tiene_descuento(cls, codigo: str) -> bool:
        if cls.descuentos.get(codigo):
            return True
        else:
            return False
    
    @classmethod
    def obtener_descuento(cls, codigo) -> float:
        if cls.tiene_descuento(codigo):
            return cls.productos[codigo]['precio'] * cls.descuentos[codigo]
        else:
            return 0
    
    @classmethod
    def obtener_nombre(cls, codigo) -> str:
        return cls.productos[codigo]['nombre']

    @classmethod
    def agregar_producto(self, *detalles) -> None:
        pass

    @classmethod
    def modificar_producto(self, *detalles) -> None:
        pass

    @classmethod
    def eliminar_producto(self, *detalles) -> None:
        pass

# -----------------------------------------------------------------------------
# 2.- Interface
# -----------------------------------------------------------------------------
class Comando(ABC):

    db = Supermercado()
    history = []

    @abstractmethod
    def ejecutar(self) -> None:
        pass

# -----------------------------------------------------------------------------
# 3.- Comandos concretos
# Un metodo que se supone deba pertenecer a la clase Supermercado lo hacemos un
# comando para tener operaciones de control adicionales
# -----------------------------------------------------------------------------
class LimpiarLista(Comando):
    @classmethod
    def ejecutar(cls) -> None:
        cls.history = []
        print('*'*80)
        print('{:^80s}'.format('Abarrotes ITESO'))
        print('*'*80)
        print('  {:<10} {}'.format('Cajero:', 'Victor Martinez'))
        print('  {:<10} {}'.format('Hora:', '24 de noviembre del 2020'))
        print('  {:<10} {}'.format('Sucursal:', 'Tlaquepaque\n'))
    
    def guardar_copia_lista_previa(cls):
        pass

class ImprimirCuenta(Comando):
    @classmethod
    def ejecutar(cls) -> None:
        total = 0
        print('-'*80)
        print('{:<20} {:>10} {:>10} {:>10} {:>10}'.format(
            'nombre',
            'precio',
            'descuento',
            'cantidad',
            'total'
        ))
        print('-'*80)
        for producto in cls.history:
            total += float(producto.split()[4])
            print(producto)
        print('-'*80)
        print('{:>64}'.format(total))
    
    def enviar_por_correo(cls):
        pass

class AgregarProducto(Comando):
    @classmethod
    def ejecutar(cls, codigo: str, cantidad: int = 1):
        nombre = cls.db.obtener_nombre(codigo)
        precio = cls.db.codigo_a_precio(codigo)
        descuento = cls.db.obtener_descuento(codigo)
        item = '{:<20} {:>10} {:>10} {:>10} {:>10}'.format(
            nombre,
            precio,
            descuento,
            cantidad,
            (precio - descuento) * cantidad
        )
        cls.history.append(item)
    
    @classmethod
    def deshacer(cls):
        # Funciona mejor con el patron de diseño Memento
        del cls.history[-1]
        pass

    @classmethod
    def rehacer(cls):
        pass

# -----------------------------------------------------------------------------
# 1.- MaquinaRegistradora
# La maquina registradora usa comandos
# -----------------------------------------------------------------------------
class MaquinaRegistradora:

    def __init__(self, backup: bool = False, enviar_correo: bool = False):
        self.backup = backup
        self.enviar_correo = enviar_correo
        self.reiniciar()

    def reiniciar(self):
        if self.backup:
            LimpiarLista.guardar_copia_lista_previa()
        LimpiarLista.ejecutar()

    def cobrar(self):
        ImprimirCuenta.ejecutar()
        if self.enviar_correo:
            ImprimirCuenta.enviar_por_correo()
    
    def cancelar(self):
        password = getpass()
        if password == 'iteso123':
            AgregarProducto.deshacer()
        else:
            print('-E- Password incorrecto, no se puede cancelar la operacion')

    def capturar(self, codigo, cantidad):
        AgregarProducto.ejecutar(codigo, cantidad)


if __name__ == "__main__":
    
    caja2 = MaquinaRegistradora()
    caja2.capturar('b0002', 2)
    caja2.capturar('a0002', 1)
    caja2.capturar('a0001', 1)
    caja2.cancelar()
    caja2.capturar('a0003', 3)
    caja2.capturar('c0003', 1.25)
    caja2.cobrar()