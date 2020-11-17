from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# Singleto auxiliar
# -----------------------------------------------------------------------------
def singleton(clase):
    instancias = {}
    def obtener_instancia(*args, **kwargs):
        if clase not in instancias:
            instancias[clase] = clase(*args, **kwargs)
        return instancias[clase]
    return obtener_instancia

# -----------------------------------------------------------------------------
# 1.- Service Interface
# -----------------------------------------------------------------------------
class Operaciones(ABC):
    @abstractmethod
    def obtener_usuarios(self, role:str) -> list:
        pass

# -----------------------------------------------------------------------------
# 2.- Service
# -----------------------------------------------------------------------------
@singleton
class MongoMejorado(Operaciones):

    def __init__(self):
        self.__table_users = {}
        self.__table_roles = {}
    
    def llenar_datos(self):
        # Tabla usuarios, nivel de accesso: privado
        self.__table_users = {
            '11223344': {
                'nombre': 'Victor Martinez',
                'nivel_acceso': 3
            },
            '22334455': {
                'nombre': 'Pepe Pecas',
                'nivel_acceso': 2
            },
            '33445566': {
                'nombre': 'Sergio el bailador',
                'nivel_acceso': 1
            },
        }

        # Tabla roles, nivel de accesso: privado
        self.__table_roles = {
            'profesor': ['11223344', '33445566'],
            'investigador': ['11223344', '22334455']
        }

    def obtener_usuarios(self, role:str) -> None:
        '''
        Imprime la lista de usuarios asignados a un role
        '''
        for user_id in self.__table_roles[role]:
            print('  -', self.__table_users[user_id]['nombre'])
    
    def obtener_nivel_acceso(self, id:str) -> int:
        if self.__table_users.get(id) is None:
            print(f'-E- El usuario con el id {id} no existe')
            return 0
        else:
            return self.__table_users[id]['nivel_acceso']
    
    def insertar_usuario(self, id:str, **datos) -> None:
        self.__table_users[id] = {
            'nivel_acceso': datos['nivel_acceso'],
            'nombre': datos['nombre']
        }
        self.__table_roles[datos['role']].append(id)

# -----------------------------------------------------------------------------
# 3.- Proxy
# -----------------------------------------------------------------------------
class Proxy(Operaciones):
    def __init__(self, db: MongoMejorado) -> None:
        self.__db = db

    def obtener_usuarios(self, role:str, id_solicitante:str) -> None:
        if self.check_access(id_solicitante):
            self.log_access()
            self.__db.obtener_usuarios(role)
        else:
            print('-E- Permisos insuficientes para obtener datos')
            return None

    def check_access(self, id:str) -> bool:
        if self.__db.obtener_nivel_acceso(id) > 2:
            return True
        else:
            return False

    def log_access(self) -> None:
        print('-I- Insertando una entrada en el archivo de accesso...')


if __name__ == "__main__":
    print('-I- Ejecución de la consulta directamente usando el objeto MongoMejorado')
    db = MongoMejorado()
    db.llenar_datos()
    db.insertar_usuario('99887766', nombre='Ivan Villalon', role='profesor', nivel_acceso='2')
    db.obtener_usuarios('profesor')
    print('-' * 80)

    print('-I- Ejecución de la consulta usando un proxy a un nuevo objeto MongoMejorado')
    db2 = MongoMejorado()
    db2.llenar_datos()
    proxy = Proxy(db2)
    proxy.obtener_usuarios('profesor', '11223344')
    print('-' * 80)
    
    print('-I- Ejecución de la consulta usando un proxy a un objeto MongoMejorado existente')
    proxy = Proxy(db)
    proxy.obtener_usuarios('profesor', '11223344')