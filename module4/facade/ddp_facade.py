import ddp_framework as framework
from time import sleep

# -----------------------------------------------------------------------------
# Facade
# -----------------------------------------------------------------------------
# El patrón Celular proporciona un práctico acceso a una parte específica de la
# funcionalidad del subsistema. Sabe a dónde dirigir la petición del cliente
# y cómo operar todas las partes móviles
# -----------------------------------------------------------------------------
class Celular:
    
    def __init__(self) -> None:
        self.bateria = framework.Bateria(modelo='Niquel-Cadmio (NiCd)', capacidad=4800)
        self.cpu = framework.CPU('Apple A14 Bionic')
        self.servicios = [
            framework.GPS(),
            framework.Wifi()
        ]

    def encender(self):
        self.bateria.encender()
        self.cpu.encender()
        self.cpu.boot()
        for servicio in self.servicios:
            servicio.conectar()
    
    def apagar(self):
        for servicio in self.servicios:
            servicio.desconectar()
        self.cpu.apagar()
        self.bateria.apagar()

    def modo_avion(self):
        for servicio in self.servicios:
            servicio.desconectar()

class DebugCelular(Celular):
    def modo_debug(self):
        self.bateria.encender()
        self.cpu.encender()
        self.cpu.boot()
        print('-I- Ejecutando prueba, espere...')
        sleep(3)
        print('-I- Resultado: PASS')
        self.cpu.apagar()
        self.bateria.apagar()

# -----------------------------------------------------------------------------
# Cliente
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    iphone12 = Celular()
    print('-I- -------- ENCENDER -----------')
    iphone12.encender()
    print('-I- ------- MODO AVION ----------')
    iphone12.modo_avion()
    print('-I- --------- APAGAR ------------')
    iphone12.apagar()

    iphone12 = DebugCelular()
    print('-I- ---------- DEBUG -----------')
    iphone12.modo_debug()