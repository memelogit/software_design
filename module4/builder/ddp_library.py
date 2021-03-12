from abc import ABC, abstractmethod, abstractproperty
from enum import Enum

# 3.- Productos
# Los Productos son los objetos resultantes.
# Los productos construidos por distintos objetos constructores no tienen que
# pertenecer a la misma jerarquía de clases o interfaz.
class Estructura(ABC):
    def __init__(self, descripcion: str = None) -> None:
        self._partes = []
        self.color = 'base'
        self._descripcion = descripcion

    @property
    def descripcion(self) -> str:
        return self.descripcion
    
    @property
    def partes(self) -> list:
        return self._partes
    
    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    def agregar_parte(self, parte) -> None:
        print(f'-I- Colocando {parte}...')
        self._partes.append(parte)

    def __str__(self) -> None:
        return self._descripcion

class Auto(Estructura):
    def __init__(self):
        super().__init__('automovil')

class SUV(Estructura):
    def __init__(self):
        super().__init__('suv')

class Minivan(Estructura):
    def __init__(self):
        super().__init__('minivan')

class Motoneta(Estructura):
    def __init__(self):
        super().__init__('motoneta')

class MotoDeportiva(Estructura):
    def __init__(self):
        super().__init__('moto deportiva')

class Cuatrimoto(Estructura):
    def __init__(self):
        super().__init__('cuatrimoto')

# 1- Interface constructora (Builder)
# La interfaz Constructora declara pasos de construcción de producto que todos
# los tipos de objetos constructores tienen en común.
class Honda(ABC):
    @property
    def estructura(self):
        return self._estructura

    def agregar_llantas(self, llantas: int) -> None:
        self.estructura.agregar_parte(f'{llantas} llantas')
    
    def agregar_asientos(self, asientos: int) -> None:
        self.estructura.agregar_parte(f'{asientos} asientos')
    
    def agregar_motor(self, motor: str) -> None:
        self.estructura.agregar_parte(f'motor {motor}')
    
    def agregar_faros(self, tipo: str) -> None:
        self.estructura.agregar_parte(f'faros {tipo}')
    
    def pintar(self, color: str) -> None:
        print(f'-I- Pintando {self.estructura} de color {color}...')
        self._color = color
    
    def verificar(self) -> None:
        print(f'-I- Verificado últimos detalles de {self.estructura}....')
    
    def contenido(self) -> list:
        return self.estructura.partes

# 2.- Constructores concretos
# Los Constructores Concretos ofrecen distintas implementaciones de los pasos
# de construcción. Los constructores concretos pueden crear productos que no
# siguen la interfaz común.
class HondaAuto(Honda):

    class TipoAuto(Enum):
        AUTO    = Auto()
        SUV     = SUV()
        MINIVAN = Minivan()

    def __init__(self, tipo: TipoAuto) -> None:
        self._estructura = tipo.value
    
    def agregar_puertas(self, puertas: int) -> None:
        self.estructura.agregar_parte(f'{puertas} puertas')
    
    def agregar_sistema_audio(self, tipo: str) -> None:
        self.estructura.agregar_parte(f'sistema de audio {tipo}')

    def agregar_quemacocos(self) -> None:
        self.estructura.agregar_parte('quemacocos')

class HondaMoto(Honda):

    class TipoMoto(Enum):
        MOTONETA   = Motoneta()
        DEPORTIVA  = MotoDeportiva()
        CUATRIMOTO = Cuatrimoto()

    def __init__(self, tipo: TipoMoto) -> None:
        self._estructura = tipo.value

# 4.- Directores
# La clase Directora define el orden en el que se invocarán los pasos de
# construcción, por lo que puedes crear y reutilizar configuraciones específicas
# de los productos.
class Manufactura:

    def __init__(self, color = 'blanco') -> None:
        self._producto = None
        self._color = color

    @property
    def producto(self) -> Honda:
        return self._producto

    @producto.setter
    def producto(self, producto: Honda) -> None:
        self._producto = producto

    def descripcion(self, nombre_modelo):
        print('-' * 80)
        print(f'-I- Ensamblando producto con instrucciones para {nombre_modelo} '
              f'sobre una estructura de {self.producto.estructura}')

    def ensamblar_civic_ex(self) -> None:
        self.descripcion('civic modelo EX')
        self.producto.agregar_motor('2.0L')
        self.producto.agregar_puertas(4)
        self.producto.agregar_asientos(5)
        self.producto.agregar_faros('incandescentes')
        self.producto.agregar_llantas(4)
        self.producto.pintar(self._color)
        self.producto.verificar()
    
    def ensamblar_civic_touring(self) -> None:
        self.descripcion('civic modelo Touring')
        self.producto.agregar_motor('3.5L Turbo')
        self.producto.agregar_quemacocos()
        self.producto.agregar_puertas(4)
        self.producto.agregar_asientos(5)
        self.producto.agregar_faros('LED')
        self.producto.agregar_sistema_audio('bose')
        self.producto.agregar_llantas(5)
        self.producto.pintar(self._color)
        self.producto.verificar()
    
    def ensamblar_moto_cargo_150(self) -> None:
        self.descripcion('moto cargo 150')
        self.producto.agregar_motor('1.0L')
        self.producto.agregar_asientos(1)
        self.producto.agregar_faros('incandescentes')
        self.producto.agregar_llantas(2)
        self.producto.pintar(self._color)
        self.producto.verificar()
    
    class Instrucciones(Enum):
        CIVIC_EX       = 'self.ensamblar_civic_ex()'
        CIVIC_TOURING  = 'self.ensamblar_civic_touring()'
        MOTO_CARGO_150 = 'self.ensamblar_moto_cargo_150()'

    def iniciar_montaje(self, tipo: Instrucciones):
        print('-I- Iniciando proceso de manufactura')
        eval(tipo.value)
        print('-I- El proceso se completo satisfactoriamente')

if __name__ == "__main__":

    # Creación de productos usando un director
    planta_celaya = Manufactura()                                   # Director
    planta_celaya.producto = HondaAuto(HondaAuto.TipoAuto.MINIVAN)  # Constructor concreto
    planta_celaya.ensamblar_civic_ex()                              # Proceso del director

    planta_celaya.producto = HondaMoto(HondaMoto.TipoMoto.MOTONETA)
    planta_celaya.ensamblar_moto_cargo_150()

    planta_celaya.producto = HondaAuto(HondaAuto.TipoAuto.AUTO)
    planta_celaya.iniciar_montaje(planta_celaya.Instrucciones.CIVIC_TOURING)

    # Producto personalizado
    combi_iteso = HondaAuto(HondaAuto.TipoAuto.MINIVAN)
    print('-' * 80)
    print(f'-I- Ensamblando combi con sobre una estructura de {combi_iteso.estructura}')
    combi_iteso.agregar_asientos(12)
    combi_iteso.agregar_faros('xenón')
    combi_iteso.agregar_llantas(6)
    combi_iteso.agregar_motor('5.0L turbo cargado')
    combi_iteso.agregar_puertas(3)
    combi_iteso.agregar_quemacocos()
    combi_iteso.agregar_sistema_audio('Harman Kardon')
    combi_iteso.pintar('Azul')
    combi_iteso.verificar()
    print(combi_iteso.contenido())