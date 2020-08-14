class Avion:
    def __init__(self, velocidad, altitud, roll, pitch, yaw):
        self.velocidad = velocidad
        self.altitud = altitud
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        self.__pasajeros = 0
    
    def volar(self):
        return 'volando a {} metros de altitud y {} km/h.'.format(
            self.altitud,
            self.velocidad
        )

    # Python usa el mecanismo llamado "name mangling" para ocultar la variable
    # 'pasajeros'. Mas información aquí
    # https://docs.python.org/3/tutorial/classes.html#private-variables
    def establecerPasajeros(self, numero_pasajeros):
        self.__pasajeros = numero_pasajeros
    
    def obtenerPasajeros(self):
        return self.__pasajeros
    
    @property
    def pasajeros(self):
        return self.__pasajeros
    
    @pasajeros.setter
    def pasajeros(self, numero_pasajeros):
        # +1 porque necesitamos al menos un piloto
        self.__pasajeros = numero_pasajeros + 1

volaris747 = Avion(500, 2000, 0, 0, 0)
print(volaris747.volar())

volaris747.establecerPasajeros(100)
print(volaris747.obtenerPasajeros())

volaris747.pasajeros = 90
print(volaris747.pasajeros)