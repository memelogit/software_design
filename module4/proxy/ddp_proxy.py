# Creamos la clase de servicio
# Esta clase de servicio normalmente ya esta creada y nosotros no
# podemos abrir su código (modificarlo)
from abc import ABC
from typing import List

class MongoDB():
    '''
    Clase del cliente para manejo de operaciones de MongoDB
    Se supone que esta clase ya existe y no es posible modificarla

    tabla_usuarios: {'ID': {'nombre': NOMBRE, 'role':ROLE, 'nivel_acceso':NIVEL}}
    tabla_roles: {'ROL': ['1234', '1235']}
    '''
    def __init__(self) -> None:
        self._tabla_usuarios:dict = {}
        self._tabla_roles:dict = {}

    def insertar_usuario(self, id:str, **datos:dict) -> None:
        '''
        Inserta un nuevo usario en la tabla de usuarios basado
        en el id dado como argumento
        '''
        self._tabla_usuarios[id] = {
            'nombre': datos['nombre'],
            'nivel_acceso': datos['nivel_acceso']
        }
        if self._tabla_roles.get(datos['role']) is None:
            self._tabla_roles[datos['role']] = []
        self._tabla_roles[datos['role']].append(id)

    
    def obtener_usuarios(self, role:str) -> str:
        '''
        Retorna la lista de usuarios asociada a un role
          - Victor
          - Juanito
        '''
        lista_usuarios:List[str] = []
        for user_id in self._tabla_roles[role]:
            lista_usuarios.append(self._tabla_usuarios[user_id]['nombre'])
            
        return '\n-'.join(lista_usuarios)
    
    def obtener_nivel_acceso(self, id:str) -> int:
        '''
        Obtiene el nivel de acceso de un usuario
        0 - Cuando el usuario no existe
        1 - Publico
        2 - Confidential
        3 - Top secret
        '''
        if self._tabla_usuarios.get(id) is None:
            return 0
        else:
            return self._tabla_usuarios[id]['nivel_acceso']

# Interfase de servicio
class Operaciones(ABC):
    '''
    Interfase de servicio usada para mantener los métodos comunes a 
    los clientes o usuarios
    '''
    def obtener_usuarios(self, role:str) -> str:
        '''
        Retorna la lista de usuarios asociada a un role
          - Victor
          - Juanito
        '''
        pass

# Proxy
class ProxyTopSecret(Operaciones):
    '''
    Clase proxy que mantiene el control de acceso a los métodos definidos
    en la interfase de servicio
    '''
    def __init__(self, db:MongoDB) -> None:
        self._db:MongoDB = db
    
    def validar_acceso(self, user_id:str) -> bool:
        '''
        Returna True si el nivel de acceso del user_id corresponde
        con el de la base de datos
        '''
        if int(self._db.obtener_nivel_acceso(user_id)) >= 3:
            return True
        else:
            return False
    
    def obtener_usuarios(self, role: str, user_id_request:int=0) -> str:
        '''
        Método modificado dentro de la clase proxy al que le 
        añadimos la validación del nivel de acceso
        '''
        if self.validar_acceso(user_id_request):
            return self._db.obtener_usuarios(role)
        else:
            raise RuntimeError('No tienes el nivel de acceso necesario para acceder a la información')

# Código del cliente
if __name__ == '__main__':
    db = MongoDB()
    db.insertar_usuario(
        '000001',
        nombre='Iván Villalón',
        role='Profesor',
        nivel_acceso='3'
    )
    
    db.insertar_usuario(
        '000002',
        nombre='Francisco Cervantes',
        role='Profesor',
        nivel_acceso='2'
    )
    
    db.insertar_usuario(
        '000003',
        nombre='Victor Martinez',
        role='Profesor',
        nivel_acceso='2'
    )

    proxy = ProxyTopSecret(db)
    print(proxy.obtener_usuarios('Profesor', '000002'))