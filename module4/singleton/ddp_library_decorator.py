def singleton(clase):
    instancias = {}
    def obtener_instancia(*args, **kwargs):
        if clase not in instancias:
            instancias[clase] = clase(*args, **kwargs)
        return instancias[clase]
    return obtener_instancia

@singleton
class Sesion:
    def __init__(self, usuario: str):
        self.usuario = usuario
    
    def __str__(self):
        return self.usuario

if __name__ == '__main__':
    s1 = Sesion('usuario1')
    s2 = Sesion('usuario1')

    print(s1)
    print(s2)