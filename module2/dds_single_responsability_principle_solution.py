class Empleado:
    def __init__(self, nombre):
        self._nombre = nombre
        self._tiempos = []
    
    def obtenerNombre(self):
        return self._nombre
    
    def nuevoTiempo(self, dia, horas):
        self._tiempos.append(f'El dia {dia} trabajó: {horas} horas.')

    def removerTiempo(self, posicion):
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
victor.nuevoTiempo('lunes', 8)
victor.nuevoTiempo('martes', 8)
victor.nuevoTiempo('miercoles', 6)
victor.nuevoTiempo('jueves', 8)
victor.nuevoTiempo('viernes', 2)
print(ReporteTiempos.imprimir(victor))