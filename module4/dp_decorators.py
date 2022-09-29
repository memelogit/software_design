import time

def timer(función:object) -> None:
    ''' Función decorador que puedo anclar a mis métodos o funciones '''
    def wrapper(*args:list, **kwargs:dict) -> object:
        ''' Función encargada del comportamiento de mi decorador '''
        comienzo:float = time.time()
        retorno = función(*args, **kwargs)
        total:float = time.time() - comienzo
        print(f'Tiempo total de ejecución: {total}')
        return retorno
    return wrapper

@timer
def consumo_tiempo(delta_seg:int):
    ''' función simple que consume tiempo '''
    print('Comenzando')
    time.sleep(delta_seg)
    print('Terminado')
    return delta_seg

consumo_tiempo(2)