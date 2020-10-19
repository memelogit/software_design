class Sesion:

    # Aquí guardaremos la única instancia permitida
    __instancia = None

    def __init__(self, usuario: str):
        if Sesion.__instancia == None:
            self.usuario = usuario
            Sesion.__instancia = self
        else:
            print('-W- Ya existe un usuario en la sesión')
    
    @classmethod
    def obtener_sesion(cls):
        return cls.__instancia
    
    def logout(self):
        Sesion.__instancia = None