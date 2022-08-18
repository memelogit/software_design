# Programación orientada a objetos > Conceptos básicos de POO y UML

class Animal:
    ''' Crea un objeto del tipo animal '''

    VIDAS = 1

    def __init__(self, nombre:str, edad:int, peso:float, color:str):
        self.nombre:str = nombre
        self.edad:int = edad
        self.peso:float = peso
        self.color:str = color
    
    def detalles(self) -> str:
        ''' Regresa los detalles asociados a un animal '''
        return '{} es un animal de {} años color {} que pesa {} kilos.'.format(
            self.nombre,
            self.edad,
            self.color,
            self.peso
        )
    
    @classmethod
    def obtener_vidas(cls) -> int:
        ''' Retorna el número de vidas de un animal '''
        return cls.VIDAS

    def respirar(self) -> None:
        ''' Ejecuta la acción de respirar de un animal '''
        pass

class Gato(Animal):
    ''' Crea un objeto del tipo gatito '''

    # Podemos modificar variables de clase en una subclase
    VIDAS = 9

    def __init__(self, nombre:str, edad:int, peso:float, color:str, limpio:bool):
        # Cuando tenemos superclases, se puede invocar al constructor de la clase padre
        # a través de super()
        super().__init__(nombre, edad, peso, color)
        self.limpio:bool = limpio

    def meow(self) -> None:
        ''' Accion solamente asociada a los gatitos '''
        pass

class Perro(Animal):
    def ladrar(self) -> None:
        ''' Accion solamente asociada a nuestro cachorros '''
        pass

tom = Gato('Tom', 3, 7, 'café', limpio=True)
print(tom.detalles())
print(tom.obtener_vidas())

# Con el método isinstance() sabemos si una instancia pertenece a una clase
print(isinstance(tom, Animal))

# Con el método help() sabemos detalles adicionales de la herencia tales como
# el orden de resolución de métodos o las variables de clase
# print(help(tom))