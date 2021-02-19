class Empleado:
    def __init__(self, nombre):
        self._nombre = nombre
        self._tiempos = []
    
    def obtener_nombre(self) -> str:
        return self._nombre
    
    def nuevo_tiempo(self, dia:int, horas:int) -> str:
        self._tiempos.append(f'El dia {dia} trabajó: {horas} horas.')

    def remover_tiempo(self, posicion:int):
        pass

class ReporteTiempos:
    @staticmethod
    def imprimir(empleado):
        return '\n'.join(empleado._tiempos)
    
    @staticmethod
    def guardar():
        pass

    @staticmethod
    def cargar():
        pass

victor = Empleado('Víctor Hugo')
victor.nuevo_tiempo('lunes', 8)
victor.nuevo_tiempo('martes', 8)
victor.nuevo_tiempo('miercoles', 6)
victor.nuevo_tiempo('jueves', 8)
victor.nuevo_tiempo('viernes', 2)
print(ReporteTiempos.imprimir(victor))