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

    NORMAL   =  5
    ENFADADO = 10
    AGRESIVO = 20

    def __init__(self, nombre, tipo: TipoZombie):
        if not isinstance(tipo, TipoZombie):
            raise Exception('Tipo de Zombie inválido')
        self.__nombre = nombre
        self.__tipo = tipo
        self.__ultimo_alimento = datetime.now()
        self.__cerebros_devorados = 0

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
        self.__cerebros_devorados += 1

    @property
    def estado_de_animo(self):
        ''' Regresa el estado de ánimo de nuestro zombie basado en el tiempo
            que ha pasado sin comer '''
        if self.tiempo_sin_alimento > timedelta(seconds=self.AGRESIVO):
            return 'agresivo'
        elif self.tiempo_sin_alimento > timedelta(seconds=self.ENFADADO):
            return 'enfadado'
        elif self.tiempo_sin_alimento > timedelta(seconds=self.NORMAL):
            return 'normal'
        else:
            return 'contento'
    
    # EXTRACT VARIABLE
    # En lugar de tener expresiones complejas en las condicionales, usamos variables
    # temporales que facilitan el entendimiento.
    @property
    def peligrosidad(self):
        ''' Regresa el nivel de peligrosidad del zombie en tres niveles
            alta, media o baja '''
        tipo_agresivo = self.__tipo == TipoZombie.ZOMBIEINSTEIN or self.__tipo == TipoZombie.ZOMBIEPULTA
        con_buen_animo = self.estado_de_animo == 'contento' or self.estado_de_animo == 'normal'
        if not tipo_agresivo and con_buen_animo and self.__cerebros_devorados >= 1:
            return 'baja'
        elif not tipo_agresivo and not con_buen_animo and self.__cerebros_devorados >= 1:
            return 'media'
        else:
            return 'alta'

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
sleep(1)

# Obtenemos los detalles de nuestro zombie
print(zombie_bailarin.info())

# Prguntamos el estado de ánimo de nuestro zombie
print(f'-I- Nuestro zombie está {zombie_bailarin.estado_de_animo}')

# Ahora obtenemos su peligrosidad
print(f'-I- Peligrosidad: {zombie_bailarin.peligrosidad}')