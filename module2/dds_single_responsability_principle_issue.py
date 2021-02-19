# Estos asignando responsabilidades adicionales a la clase Empleado
# Rompemos el principio de responsabilidad única

class Empleado:
    def __init__(self, nombre:str):
        self._nombre = nombre
        self._tiempos = []
    
    def obtener_Nombre(self) -> str:
        return self._nombre
    
    def nuevo_tiempo(self, dia:int, horas:int) -> None:
        self._tiempos.append(f'El dia {dia} trabajó: {horas} horas.')
    
    def imprimir_reporte_tiempos(self) -> str:
        return '\n'.join(self._tiempos)

    def remover_tiempo(self, posicion:int):
        pass

victor = Empleado('Víctor Hugo')
victor.nuevo_tiempo('lunes', 8)
victor.nuevo_tiempo('martes', 8)
victor.nuevo_tiempo('miercoles', 6)
victor.nuevo_tiempo('jueves', 8)
victor.nuevo_tiempo('viernes', 2)
print(victor.imprimir_reporte_tiempos())