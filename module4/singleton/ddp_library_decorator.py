# Clase auxiliar que nos permite tener un control de las instancias unicas
# de cada clase
class Bucket:
    INSTANCES = {}

# Definicion del decorador. Es una funcion anidada.
def singleton(clase):
    def obtener_instancia(*args, **kwargs):
        if clase not in Bucket.INSTANCES:
            Bucket.INSTANCES[clase] = clase(*args, **kwargs)
        return Bucket.INSTANCES[clase]
    return obtener_instancia

@singleton
class Sesion:
    def __init__(self, usuario: str):
        self.usuario = usuario
    
    def __str__(self):
        return self.usuario
    
    def logout(self):
        print(Bucket.INSTANCES)
        print(self.__class__)
        del Bucket.INSTANCES[self.__class__]

if __name__ == '__main__':
    s1 = Sesion('usuario 1')
    s1.logout()
    s2 = Sesion('usuario 2')
    s3 = Sesion('usuario 3')

    print(s1)
    print(s2)
    print(s3)