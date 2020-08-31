from abc import ABC

class Transporte:
    def __init__(self, motor, chofer):
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
    
    def entregar(self, destino, carga):
        return 'Vamos a entregar una carga de {} kilos a {}.\n * {}\n * {}'.format(
            destino,
            carga,
            self.motor.mover(),
            self.chofer.manejar()
        )
    
    def __str__(self):
        return 'Es un transporte con {} el cual conduce un {}'.format(
            self.motor,
            self.chofer
        )

class Motor(ABC):
    def mover(self):
        return 'Moviéndonos...'    

class Chofer(ABC):
    def manejar(self):
        return 'Manejando...'

class MotorCombustion(Motor):
    def mover(self):
        return 'Moviéndonos con una máquina de combustión...'
    
    def __str__(self):
        return 'motor de combustión'
    
class MotorElectrico(Motor):
    def mover(self):
        return 'Moviéndonos con una máquina de eléctrica...'
    
    def __str__(self):
        return 'motor de eléctrico'
    
class Robot(Chofer):
    def manejar(self):
        return 'Un robot está manejando...'
    
    def __str__(self):
        return 'robot con autopilot'

class Humano(Chofer):
    def manejar(self):
        return 'Un humano está manejando...'
    
    def __str__(self):
        return 'Humano'

# Creamos el tipo de chofer que manejará el transporte
chofer = Robot()

# Creamos el objeto transporte
tesla = Transporte('eléctrico', chofer)

# Impriminos los detalles de nuestro transporte
print(tesla)
print(tesla.entregar('TIJ', '200'))