from __future__ import annotations

class Sesion:

    # Aquí guardaremos la única instancia permitida
    _INSTANCIA = None

    def __init__(self, usuario:str):
        if Sesion._INSTANCIA == None:
            self.usuario = usuario
            Sesion._INSTANCIA = self
            print(f'-I- {usuario}')
        else:
            print('-E- Ya existe un usuario en la sesión')
    
    @classmethod
    def obtener_sesion(cls) -> Sesion:
        return cls._INSTANCIA
    
    def logout(self) -> None:
        Sesion._INSTANCIA = None

if __name__ == '__main__':
    s1 = Sesion('usuario 1')
    s1.logout()
    s2 = Sesion('usuario 2')
    s3 = Sesion('usuario 3')