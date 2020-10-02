# Asegúrate de primero revisar el código de 'dp_create_class_through_type'

# Al crear la clase perro, en realidad lo que hacemos es pasar la información
# a una metaclase llamada 'type'
class Perro:
    pass

# Ahora tratemos de contruir una metaclase
class Meta(type):
    # __new__ antes de inicializar el método
    def __new__(self, nombre_clase, bases, atributos):
        print(atributos)

        # Nuestra metaclase nos permite modificar los atributos. En este caso
        # estamos cambiando todos los nombres de los atributos y métodos a
        # mayúsculas
        a = {}
        for nombre, valor in atributos.items():
            if nombre.startswith('__'):
                a[nombre] = valor
            else:
                a[nombre.upper()] = valor

        return type(nombre_clase, bases,  a)

class Perro(metaclass=Meta):
    vidas = 1

benji = Perro()

# Si tratamos de imprimir el valor de 'vidas' con minúsculas, Python nos
# mostraría un error debido a nuestra metaclase.
# print(benji.vidas)

# Sin embargo
print(benji.VIDAS)