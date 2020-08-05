from abc import ABC

class TransporteAereo(ABC):
    def __init__(self, origen, destino, pasajeros):
        self.origen = origen
        self.destino = destino
        self.pasajeros = pasajeros

    def volar(self):
        return 'volando de {} a {} con {} pasajeros...'.format(
            self.origen,
            self.destino,
            self.pasajeros
        )

class Helicoptero(TransporteAereo):
    # Opcionalmente podemos modificar el constructor
    # def __init__(self, origen, destino, pasajeros):
    #     super().__init__(origen, destino, pasajeros)

    def volar(self):
        return 'en helicóptero {}'.format(
            super().volar()
        )

class Avion(TransporteAereo):
    def volar(self):
        return 'en avión {}'.format(
            super().volar()
        )

class DronParaHumanos(TransporteAereo):
    def volar(self):
        return 'en un dron para humanos {}'.format(
            super().volar()
        )

class AvionPapel():
    def volar(self):
        return 'no podemos volar en un avion de papel'

# En caso de que ejecutemos la librería en vez de importarla
if __name__ == '__main__':
    transporte = DronParaHumanos('GDL', 'OAK', 180)
    print(transporte.volar())