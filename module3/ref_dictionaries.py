import json
import random
from datetime import datetime


class Restaurant:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.path = None
        self.meseros = []

    def asignar_mesero(self):
        return random.choice(self.meseros)

    def detalle_meseros(self):
        detalles = ''
        for mesero in self.meseros:
            detalles += '{0:<10} {1:>5} {2:>10}\n'.format(
                mesero.nombre,
                mesero.edad,
                mesero.propina
            )
        return detalles
    
    def guardar(self):
        restaurant = {
            'negocio': {
                'nombre': self.nombre
            }
        }
        path_guardar = f'saved_{self.path}'
        with open(path_guardar, 'w') as outfile:
            json.dump(restaurant, outfile)
        print(f'Archivo guardado en {path_guardar}')
    
    @property
    def nombre(self):
        return self.__nombre

    @classmethod
    def from_json(cls, json):
        restaurant = cls(json['negocio']['nombre'])
        for mesero in json['meseros']:
            restaurant.meseros.append(Mesero.from_json(mesero))
        return restaurant

    @classmethod
    def from_json_file(cls, json_file_path):
        with open(json_file_path) as json_file:
            restaurant = Restaurant.from_json(json.load(json_file))
            restaurant.path = json_file_path
        return restaurant


class Mesero:
    def __init__(self, nombre, edad, fecha_de_ingreso):
        self.__nombre = nombre
        self.__edad = edad
        self.__fecha_de_ingreso = fecha_de_ingreso
        self.__propina = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def propina(self):
        return self.__propina

    def dejar_propina(self, monto: int):
        self.__propina += monto

    @classmethod
    def from_json(cls, json):
        return cls(json['nombre'], json['edad'], json['fecha_de_ingreso'])

    def __str__(self):
        return f'Hola soy {self.__nombre}, encantado de atenderte'


# Leemos la información de nuestro restauran desde un archivo json
la_mestiza = Restaurant.from_json_file('ref_mestiza.json')

# Agregamos un mesero en runtime
la_mestiza.meseros.append(Mesero.from_json({
    'nombre': 'Mike',
    'edad': 16,
    'fecha_de_ingreso': datetime.now()
}))

# Asignamos un mesero de manera aleatoria
mi_mesero = la_mestiza.asignar_mesero()
print(mi_mesero)

# Dejamos propina a nuestro mesero
mi_mesero.dejar_propina(12.50)
mi_mesero.dejar_propina(6.85)

print(la_mestiza.detalle_meseros())

# Guardamos los datos del restaurant
la_mestiza.guardar()