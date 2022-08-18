# Programación orientada a objetos > Conceptos básicos de POO y UML

class Gato:
    ''' Clase gato simple sin ningún atributo o método '''

if __name__ == '__main__':
    tom = Gato()
    luna = Gato()

    tom.nombre = 'Tom'
    tom.edad = 3
    tom.peso = 7
    tom.color = 'café'

    luna.nombre = 'Luna'
    luna.edad = 2
    luna.peso = 5
    luna.color = 'gris'

    # La siguiente linea muestra la referencia en memoria al objeto
    print(tom)

    # La siguiente linea muestra el valor del atributo asignado al objeto top
    print(tom.nombre)
    print(luna.nombre)
