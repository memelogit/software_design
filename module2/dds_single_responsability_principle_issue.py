# SOLID en el diseño de software

from abc import ABC

class Empleado:
    def __init__(self, nombre:str) -> None:
        self._nombre = nombre
        self._tiempos = []
    
    def obtener_nombre(self) -> str:
        ''' '''
        return self._nombre
    
    def nuevo_tiempo(self, dia:str, horas:int) -> None:
        ''' Agrega a la lista de tiempos una nueva entrada '''
        self._tiempos.append(f'El dia {dia} trabajó {horas} horas')
    
    def imprimir_reporte_tiempos(self) -> str:
        ''' Desplegamos el reporte de tiempos, usamos el método join '''
        return '\n'.join(self._tiempos)
    
    def remover_tiempo(self, texto:str) -> None:
        ''' Elimina un entrada de la lista de tiempos '''
        self._tiempos.remove(texto)

# Testing
if __name__ == '__main__':
    victor = Empleado('Víctor Hugo')
    victor.nuevo_tiempo('lunes', 8)
    victor.nuevo_tiempo('martes', 8)
    victor.nuevo_tiempo('miercoles', 8)
    victor.nuevo_tiempo('jueves', 8)
    victor.nuevo_tiempo('viernes', 2)
    print(victor.imprimir_reporte_tiempos())