from __future__ import annotations
from abc import ABC

class Transporte:
    def __init__(self, motor:str, chofer:Chofer):
        """ motor: String
            chofer: Chofer
        """
        # Composición
        if motor == 'eléctrico':
            self.motor = MotorElectrico()
        elif motor == 'combustión':
            self.motor = MotorCombustion()
        else:
            raise Exception('El motor especificado es inválido')

        # Agregación
        self.chofer = chofer
    
    def entregar(self, destino:str, carga:str) -> str:
        ''' Consume los datos de la composición y la agregación'''
        return 'Vamos a entregar una carga de {} kilos a {}.\n * {}\n * {}'.format(
            destino,
            carga,
            self.motor.mover(),
            self.chofer.manejar()
        )
    
    def __str__(self) -> str:
        ''' Retorna la representación en texto del objeto '''
        return 'Es un transporte con {} el cual conduce un {}'.format(
            self.motor,
            self.chofer
        )

# Motores
class Motor(ABC):
    def mover(self) -> str:
        return 'Moviéndonos...'    

class MotorCombustion(Motor):
    def mover(self) -> str:
        return 'Moviéndonos con una máquina de combustión...'
    
    def __str__(self) -> str:
        return 'motor de combustión'
    
class MotorElectrico(Motor):
    def mover(self) -> str:
        return 'Moviéndonos con una máquina de eléctrica...'
    
    def __str__(self) -> str:
        return 'motor de eléctrico'

# Choferes
class Chofer(ABC):
    def manejar(self) -> str:
        return 'Manejando...'
    
class Robot(Chofer):
    def manejar(self) -> str:
        return 'Un robot está manejando...'
    
    def __str__(self) -> str:
        return 'robot con autopilot'

class Humano(Chofer):
    def manejar(self) -> str:
        return 'Un humano está manejando...'
    
    def __str__(self) -> str:
        return 'Humano'

if __name__ == '__main__':
    # Creamos el tipo de chofer que manejará el transporte
    chofer = Humano()

    # Creamos el objeto transporte
    tesla = Transporte('eléctrico', chofer)
    print(tesla)
    print(tesla.entregar('TIJ', '200'))