# Esta implementación utiliza la herencia, porque la clase adaptadora hereda
# de ambos objetos al mismo tiempo. Ten en cuenta que esta opción sólo puede
# implementarse en lenguajes de programación que soporten la herencia múltiple

# Clase principal en funcionamiento
class Entero:
    @classmethod
    def sumar(cls, *numeros:int) -> int:
        ''' Suma n cantidad de números enteros '''
        suma = 0
        for numero in numeros:
            suma += numero
        return suma

# Clase que queremos adaptar sin romper el código actual
class Binario:
    @classmethod
    def adicion(cls, binario_1:str, binario_2:str) -> str:
        ''' Suma dos números binarios representados como string '''
        return '{0:b}'.format(int(binario_1, 2) + int(binario_2, 2))

# Adapter
class BinarioToEntero(Entero, Binario):
    @classmethod
    def sumar(cls, *numeros:str):
        suma = '0'
        for numero in numeros:
            suma = cls.adicion(suma, numero)
        return int(suma, 2)

if __name__ == "__main__":
    print(f'La suma decimal 9 + 1 + 3 = {Entero.sumar(9, 1, 3)}')
    print(f'La suma binaria 1001 + 0001 + 0011 = {BinarioToEntero.sumar("1001", "0001", "0011")}')