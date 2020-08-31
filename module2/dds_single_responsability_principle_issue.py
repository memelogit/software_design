# Estos asignando responsabilidades adicionales a la clase Empleado
# Rompemos el principio de responsabilidad única

class Empleado:
    def __init__(self, nombre):
        self._nombre = nombre
        self._tiempos = []
    
    def obtenerNombre(self):
        return self._nombre
    
    def nuevoTiempo(self, dia, horas):
        self._tiempos.append(f'El dia {dia} trabajó: {horas} horas.')
    
    def imprimirReporteTiempos(self):
        return '\n'.join(self._tiempos)

    def removerTiempo(self, posicion):
        pass

victor = Empleado('Víctor Hugo')
victor.nuevoTiempo('lunes', 8)
victor.nuevoTiempo('martes', 8)
victor.nuevoTiempo('miercoles', 6)
victor.nuevoTiempo('jueves', 8)
victor.nuevoTiempo('viernes', 2)
print(victor.imprimirReporteTiempos())