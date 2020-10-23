from abc import ABC

# Esta implementación utiliza el principio de composición de objetos: el
# adaptador implementa la interfaz de un objeto y envuelve el otro

# Interface principal en funcionamiento
class Entero(ABC):
    def sumar(self, *numeros) -> str:
        ''' Suma n cantidad de números enteros '''
        suma = 0
        for numero in numeros:
            suma += numero
        return suma

# Clase que queremos adaptar sin romper el código actual
class Binario:
    def adicion(self, binario_1:str, binario_2:str) -> str:
        ''' Suma dos números binarios representados como string '''
        return '{0:b}'.format(int(binario_1, 2) + int(binario_2, 2))

# Adapter
class BinarioToEntero(Entero):
    def __init__(self, binario: Binario) -> None:
        self.binario = binario

    def sumar(self, *numeros) -> str:
        suma = '0'
        for numero in numeros:
            suma = self.binario.adicion(suma, numero)
        return int(suma, 2)

if __name__ == "__main__":

    print(f'La suma decimal 9 + 1 + 3 = {Entero().sumar(9, 1, 3)}')
    print(f'La suma binaria 1001 + 0001 + 0011 = {BinarioToEntero(Binario()).sumar("1001", "0001", "0011")}')
    print('{}'.format(hex(int('D', 16) + int('1', 16))))