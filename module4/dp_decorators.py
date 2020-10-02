import time

def timer(f):
    def wrapper(*args, **kwargs):
        comienzo = time.time()
        retorno = f(*args, **kwargs)
        total = time.time() - comienzo
        print('Tiempo: ', total)
        return retorno
    
    return wrapper

# Creamos un decorador para nuestra función
@timer
def consumo_tiempo(delta):
    time.sleep(delta)
    return delta

print('Delta: {} segundos'.format(consumo_tiempo(2)))