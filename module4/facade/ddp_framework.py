from abc import ABC, abstractmethod
from enum import Enum

class Bateria:
    def __init__(self, modelo:str, capacidad:int):
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__disponible = False
    
    def encender(self) -> str:
        self.__disponible = True
        print(f'-I- Bateria {self.__modelo} de {self.__capacidad}: Encendida')
    
    def apagar(self) -> str:
        self.__disponible = False
        print(f'-I- Bateria {self.__modelo} de {self.__capacidad}: Apagada')

class CPU:

    class estados(Enum):
        ENCENDIDA = 0
        APAGADO   = 1
        BOOT      = 2

    def __init__(self, modelo:str):
        self.__modelo = modelo
        self.__estado = CPU.estados.APAGADO

    def boot(self):
        self.__estado = CPU.estados.BOOT
        print(f'-I- CPU {self.__modelo}: {self.__estado.name.capitalize()}')
    
    def encender(self):
        self.__estado = CPU.estados.ENCENDIDA
        print(f'-I- CPU {self.__modelo}: {self.__estado.name.capitalize()}')
    
    def apagar(self):
        self.__estado = CPU.estados.APAGADO
        print(f'-I- CPU {self.__modelo}: {self.__estado.name.capitalize()}')

class ServiciosMobiles(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

class GPS(ServiciosMobiles):
    def __init__(self):
        self.__disponible = False

    def conectar(self):
        self.__disponible = True
        print('-I- GPS: Conectado')
    
    def desconectar(self):
        self.__disponible = False
        print('-I- GPS: Desconectado')

class Wifi(ServiciosMobiles):
    def __init__(self):
        self.__disponible = False

    def conectar(self):
        self.__disponible = True
        print('-I- WiFi: Conectado')
    
    def desconectar(self):
        self.__disponible = False
        print('-I- WiFi: Desconectado')