from __future__ import annotations

class Persona:
    ''' Clase A: Que representa al principal objeto que asocia al elemento de la clase B '''

    def __init__(self, nombre:str, empresa:Empresa) -> None:
        self.nombre:str = nombre
        self.empresa:Empresa = empresa # Relación de asociación
    
    def __str__(self) -> str:
        ''' Retorna el nombre de la persona '''
        return f'{self.nombre} trabaja en una empresa de {self.empresa.enfoque}, llamada {self.empresa}'

class Empresa:
    ''' Clase B: Que contine el objeto el cual será "asociado" a la clase a '''
    def __init__(self, nombre:str, enfoque:str) -> None:
        self.__nombre = nombre
        self.enfoque = enfoque
    
    def __str__(self) -> str:
        ''' Retorna el nombre de la empresa '''
        return f'Empresa: {self.__nombre}'

# Código Cliente
if __name__ == '__main__':
    iteso = Empresa('ITESO Universidad Jesuita de Guadalajara', "Educación")
    victor = Persona('Víctor Hugo', iteso)

    print(iteso)
    print(victor)