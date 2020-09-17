from datetime import datetime, timedelta
from enum import Enum, unique
from time import sleep
from math import pi

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

    TIEMPO_DE_VIDA = timedelta(minutes=5)

    def __init__(self, nombre, tipo: TipoZombie, factor_supervicencia = 1):
        if not isinstance(tipo, TipoZombie):
            raise Exception('Tipo de Zombie inválido')
        self.__nombre = nombre
        self.__tipo = tipo
        self.__ultimo_alimento = datetime.now()
        self.__cerebros_devorados = 0
        self.__factor_supervivencia = factor_supervicencia
        self.__timestamp = datetime.now()

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
    
    @property
    def tiempo_de_vida_total(self):
        ''' Regresa el tiempo que el zombie tiene antes de desaparecer. Si se
            come un cerebro, entonces se suman 2 minutos'''
        return Zombie.TIEMPO_DE_VIDA * self.__factor_supervivencia + \
                timedelta(minutes=2) * self.__cerebros_devorados
    
    @property
    def tiempo_de_vida_restante(self):
        ''' Regresa el tiempo que le resta al zombie basado en el tiempo de vida
            total '''
        return self.tiempo_de_vida_total - (datetime.now() - self.__timestamp)

    def ir(self, lugar, tiempo_del_recorrido: timedelta):
        ''' Regresa un mensaje con los detalles del recorrido, además de un valor
            boolean que indica si el zombie debería de ir a tal lugar basado en
            el tiempo de vida que le queda '''
        if self.tiempo_de_vida_restante >= tiempo_del_recorrido:
            return f'Adelante, puede ir al {lugar}', True
        else:
            return f'No se recomienda ir al {lugar}. Desaparecerá antes', False
    
    # SPLIT TEMPORARY VARIABLE
    # En lugar de tener una única variable para guardar el resultado de
    # múltiples expresiones usamos variables con nombres más descriptivos
    def buscarCerebros(self, radio: int):
        ''' Regresa los detalles asociados a la búsqueda de cerebros. El
            radio está en kilómetros'''
        perimetro = 2 * pi * radio
        area = pi * pow(radio, 2)
        return '''Detalles de la búsqueda
        perímetro: {} km
        radio    : {} km'''.format(
            perimetro,
            area
        )

class ZombieBailarin(Zombie):
    def __init__(self, nombre):
        super().__init__(nombre, TipoZombie.ZOMBIEBAILARIN, 1.5)

# Creamos al zombie
zombie_bailarin = ZombieBailarin('Zombie bailarín 1')

# Esperamos un poco antes de preguntar por sus detalles
print('-I- Buscando cerebros...')
print(f'-I- {zombie_bailarin.buscarCerebros(10)}')
sleep(4)
print('-I- Encontramos uno, a comer...')
zombie_bailarin.comer()
print('-I- Buscando cerebros...')
print(f'-I- {zombie_bailarin.buscarCerebros(2)}')
sleep(3)

# Veamos si puede llegar al refugio para zombies. Primero vemos el tiempo
# de vida total que le queda
print(f'-I- Tiempo de vida total: {zombie_bailarin.tiempo_de_vida_total}')
print(f'-I- Tiempo de vida restante: {zombie_bailarin.tiempo_de_vida_restante}')

# Llamamos al método ir... veamos que nos dice
msg, puede_ir = zombie_bailarin.ir('refugio para zombies', timedelta(minutes=250))
if puede_ir:
    print(f'-I- {msg}')
else:
    print(f'-W- {msg}')