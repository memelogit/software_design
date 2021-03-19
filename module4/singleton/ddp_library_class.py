from __future__ import annotations

class Sesion:

    # Aquí guardaremos la única instancia permitida
    _INSTANCIA = None

    def __init__(self, usuario:str):
        if Sesion._INSTANCIA == None:
            self.usuario = usuario
            Sesion._INSTANCIA = self
        else:
            print('-E- Ya existe un usuario en la sesión')
    
    @classmethod
    def obtener_sesion(cls) -> Session:
        return cls._INSTANCIA
    
    def logout(self) -> None:
        Sesion._INSTANCIA = None