from abc import ABC, abstractmethod
from datetime import datetime

class Reporte:
    def __init__(self, basededatos):
        self.__basededatos = basededatos
    
    # No hace falta modificar el llamado al método conectar
    def abir(self, fecha):
        print('[{}] {}'.format(
            fecha,
            self.__basededatos.conectar()
        ))

    def cerrar(self):
        pass

class Database(ABC):
    @abstractmethod
    def conectar(self):
        pass

    def insertar(self):
        pass

    def actualizar(self):
        pass

    def eliminar(self):
        pass

class MongoDB(Database):
    def __init__(self, cadena_conexion):
        self.detalles_conexion = cadena_conexion
    
    def conectar(self):
        return 'Conectado a MongoDB usando cadena de conexión {}'.format(
            self.detalles_conexion
        )
    
    def insertar(self):
        pass

    def actualizar(self):
        pass

    def eliminar(self):
        pass

class MySQL(Database):

    def __init__(self, nombre_del_servicio):
        self.detalles_conexion = nombre_del_servicio

    def conectar(self):
        if ';' in self.detalles_conexion:
            raise Exception('Error: Se está usando el nombre del servicio para la conexión')
        return 'Conectado a MySQL usando el nombre del servicio {}'.format(
            self.detalles_conexion
        )

    def insertar(self):
        pass

    def actualizar(self):
        pass

    def eliminar(self):
        pass

# Generamos un objeto del tipo MySQL usando el nombre del servicio para la conexión
db_mysql = MySQL('ServiceName=myServiceName')
reporte1 = Reporte(db_mysql)
reporte1.abir(datetime.now())

# Ahora generams un objeto del tipo MongoDB usando una cadena de conexión
db_mongo = MongoDB('ServiceName=myServiceName;Database=myDataBase;Uid=myUsername;Pwd=myPassword;')
reporte2 = Reporte(db_mongo)
reporte2.abir(datetime.now())