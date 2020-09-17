from datetime import datetime

class Reporte:
    def __init__(self, basededatos):
        self.__basededatos = basededatos
    
    # Si se modifica el método de conexión, entonces se tendrá
    # que implementar lógica adicional al método Abrir
    def abir(self, fecha):
        print('[{}] {}'.format(
            fecha,
            self.__basededatos.conectar()
        ))

    def cerrar(self):
        pass

class MySQL:

    def __init__(self, cadena_conexion):
        self.detalles_conexion = cadena_conexion

    # Inicialmente usábamos la implementación de éste método para conectarnos
    # def conectar(self):
    #     return 'Conectado usando cadena de conexión {}'.format(
    #         self.detalles_conexion
    #     )
    
    # Ahora, suponiendo que el usuario se deba conectar usando el nombre del servicio.
    # Necesitamos modificar la clase Reporte para extraer el nombre del servicio
    # de la cadena de conexión
    def conectar(self):
        if ';' in self.detalles_conexion:
            raise Exception('Error: Se está usando el nombre del servicio para la conexión')
        return 'Conectado usando el nombre del servicio {}'.format(
            self.detalles_conexion
        )

    def insertar(self):
        pass

    def actualizar(self):
        pass

    def eliminar(self):
        pass

db_mysql = MySQL('ServiceName=myServiceName;Database=myDataBase;Uid=myUsername;Pwd=myPassword;')
reporte1 = Reporte(db_mysql)
reporte1.abir(datetime.now())