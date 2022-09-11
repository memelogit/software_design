class Canal:
    ''' Clase B: De la cual se usa el objeto dentro de la videocasetera '''

    def __init__(self, numero_de_canal:int) -> None:
        self.numero_de_canal:int = numero_de_canal
    
    def sintonizar(self) -> str:
        ''' Retorna el canal en el que estamos sintonizando '''
        return f'sintonizando el canal {self.numero_de_canal}'

class Videocasetera:
    ''' Clase A: Ejemplifica la relación de dependencia '''

    def __init__(self, nombre:str) -> None:
        self.__nombre:str = nombre
    
    def __str__(self) -> str:
        ''' Retorna la representación del objeto Videocasetera como una cadena de caracteres '''
        return self.__nombre
    
    # Getter (obtenemos información)
    @property
    def nombre(self) -> str:
        ''' Propiedad que retorna el valor del atributo "nombre" '''
        return self.__nombre

    # Setter (Asignamos valores a nuestros atributos)
    @nombre.setter
    def nombre(self, valor:str) -> str:
        ''' Propiedad que asigna un valor al atributo "nombre" '''
        if 'payaso' in valor:
            raise Exception('No se permite la palabra payaso para esta propiedad')
        self.__nombre = valor

    # Aqui se encuentra la relación de "dependencia".
    # Esta se da a nivel de método
    def iniciar(self, canal:Canal) -> str:
        ''' Retorna True si la videocasetera pudo inciar la película '''
        return f'reproduciendo... {canal.sintonizar()}'
    
    def parar(self) -> bool:
        ''' Retorna True si la videocasetera pudo detener la película '''
        pass

# Código Cliente
if __name__ == '__main__':
    vcr = Videocasetera('VCR_10')
    canal3 = Canal(3)
    print(vcr.iniciar(canal3))