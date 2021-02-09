''' poo_class.py
Programación orientada a objetos
Conceptos básicos de POO y UML
'''

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

    print(tom)
    print(luna)
