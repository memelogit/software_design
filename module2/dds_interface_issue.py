# En este ejemplo, nuestro gato solamente puede alimentar salchichas.
# ¿Qué pasaría si queremos crecer el menu?

class Salchicha:
    def __init__(self, energia = 18):
        self.__energia = energia
    
    def obtener_energia(self):
        return self.__energia

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__energia = 100
    
    def alimentar(self, salchicha):
        self.__energia += salchicha.obtener_energia()
        if self.__energia > 100:
            self.__energia = 100
    
    def jugar(self):
        self.__energia -= 30
    
    def __str__(self):
        return 'a {} le queda {} porciento de energía'.format(
            self.nombre,
            self.__energia
        )

salchicha1 = Salchicha()
tom = Gato('Tomás')
tom.jugar()
print(tom)

tom.alimentar(salchicha1)
print(tom)