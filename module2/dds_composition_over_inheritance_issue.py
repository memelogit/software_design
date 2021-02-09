# Problemas con la herencia
# Se debe implementar todos los métodos abstractos de una clase padre.
# Cuando se sobreescriben un métodos, se debe asegurar de que el nuevo comportamiento sea compatible con la clase base.
# Las subclases están estrechamente ligadas a las superclases
# Intentar reutilizar el código a través de la herencia puede conducir a la creación de jerarquías de herencia paralelas.

from abc import ABC, abstractmethod

class Transporte(ABC):
    
    def __init__(self, capacidadCarga):
        self.capacidadCarga = capacidadCarga

    # @abstractmethod
    def entregar(self, destino, carga):
        pass

    # @abstractmethod
    def numero_llantas(self):
        pass

# Camión
class Camion(Transporte):
    def numero_llantas(self):
        info = 'Es un camión de 8 llantas'
        return info

class CamionElectrico(Camion):
    def numero_llantas(self):
        return 6

class CamionCombustion(Camion):
    def numero_llantas(self):
        info = 'Es un camión de 8 llantas'
        return info

class AutopilotoCamionElectrico(CamionElectrico):
    pass

class AutopilotoCamionCombustion:
    pass

# Automovil
class Automovil(Transporte):
    pass

class AutomovilElectrico(Automovil):
    pass

class AutomovilCombustion(Automovil):
    pass

class AutopilotoAutomovilElectrico(AutomovilElectrico):
    pass

class AutopilotoAutomovilCombustion(AutomovilCombustion):
    pass

tesla = AutopilotoAutomovilCombustion(100)