from datetime import datetime, timedelta
from enum import Enum, unique
from time import sleep

@unique
class TipoZombie(Enum):
    ZOMBIEBAILARIN = 1
    ZOMBIEPULTA    = 2
    ZOMBIEINSTEIN  = 3
    ZOMBIEACUATICO = 4
    ZOMBIEVOLADOR  = 5

class Zombie:
    def __init__(self, nombre, tipo: TipoZombie):
        if not isinstance(tipo, TipoZombie):
            raise Exception('Tipo de Zombie inválido')
        self.__nombre = nombre
        self.__tipo = tipo
        self.__ultimo_alimento = datetime.now()

    def __str__(self):
        return self.info()

    @property
    def tiempo_sin_alimento(self):
        ''' Regresa el tiempo transcurrido desde la última vez que
            nuestro zombie comió
        '''
        return datetime.now() - self.__ultimo_alimento
    
    def info(self):
        ''' Retorna los detalles de nuestro Zombie incluyendo cuanto
            tiempo ha pasado desde su último cerebro.'''
        return '''
        Zombi
        --------------------
        Nombre:         {}
        Tipo:           {}
        Último cerebro: {}'''.format(
            self.__nombre,
            self.__tipo.name,
            self.tiempo_sin_alimento
        )
    
    def comer(self):
        ''' Reinicia el tiempo que ha pasado sin alimento nuestro zombie '''
        self.__ultimo_alimento = datetime.now()
    
    # INLINE METHOD
    # El contenido del método mas_de_10_segundos_sin_comer y
    # mas_de_20_segundos_sin_comer es más que obvio además de restrictivo.
    # Por lo tanto, podemos reemplazar las llamadas a los métodos con el
    # contenido de los mismos.
    @property
    def estado_de_animo(self):
        ''' Regresa el estado de ánimo de nuestro zombie basado en el tiempo
            que ha pasado sin comer '''
        if self.mas_de_10_segundos_sin_comer():
            return 'enfadado'
        if self.mas_de_20_segundos_sin_comer():
            return 'agresivo'
        else:
            return 'contento'
    
    # Este método restringe el tiempo a 10 segundos. Su contenido es más que
    # obvio. No tiene caso crear métodos específicos.
    def mas_de_10_segundos_sin_comer(self):
        return self.tiempo_sin_alimento > timedelta(seconds=10)
    
    def mas_de_20_segundos_sin_comer(self):
        return self.tiempo_sin_alimento > timedelta(seconds=20)

class ZombieBailarin(Zombie):
    def __init__(self, nombre):
        super().__init__(nombre, TipoZombie.ZOMBIEBAILARIN)
    

# Creamos al zombie
zombie_bailarin = ZombieBailarin('Zombie bailarín 1')

# Esperamos un poco antes de preguntar por sus detalles
print('-I- Buscando cerebros...')
sleep(4)
print('-I- Encontramos uno, a comer...')
zombie_bailarin.comer()
print('-I- Buscando cerebros...')
sleep(11)

# Obtenemos los detalles de nuestro Zombie
print(zombie_bailarin.info())

# Hacemos uso de la propiedad estado_de_animo que a su vez reusa el código
# dentro de la propiedad tiempo_sin_alimento
print(f'-I- Nuestro zombie está {zombie_bailarin.estado_de_animo}')