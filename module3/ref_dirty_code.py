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

class Construccion:

    objetos = {
        'simple': {
            'poste': 2,
            'pared': 20
        },
        'grueso': {
            'poste': 4,
            'pared': 35
        },
        'apocalipsis': {
            'poste': 8,
            'pared': 80
        }
    }

    def __init__(self, ramas, tipo):
        self.ramas = ramas
        self.tipo = tipo
    
    # ¿Qué metodo de refactorización aplicamos aquí?
    def validarRamas(self, objeto, cantidad):
        if self.tipo not in Construccion.objetos:
            raise Exception('el tipo de poste no es válido')
        if Construccion.objetos[self.tipo][objeto] * cantidad < self.ramas:
            return True
        else:
            return False
    
    def construirObjeto(self, objeto, cantidad):
        if not self.validarRamas(objeto, cantidad):
            raise Exception(f'No sepuede construir {cantidad} {objeto} sin suficientes ramas')
        else:
            self.ramas -= Construccion.objetos[self.tipo][objeto] * cantidad
            return f'{cantidad} {objeto}s del tipo {self.tipo} creados'

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
            datetime.now() - self.__ultimo_alimento # Aplicar extract method
        )

    def comer(self):
        ''' Reinicia el tiempo que ha pasado sin alimento nuestro zombie '''
        self.__ultimo_alimento = datetime.now()
        self.__cerebros_devorados += 1

    @property
    def estado_de_animo(self):
        ''' Regresa el estado de ánimo de nuestro zombie basado en el tiempo
            que ha pasado sin comer '''
        if self.mas_de_10_segundos_sin_comer():
            # Aplicar inline variable
            estado = 'agresivo'
            return estado
        elif self.mas_de_20_segundos_sin_comer():
            return 'enfadado'
        elif self.mas_de_5_segundos_sin_comer():
            return 'normal'
        else:
            return 'contento'
    
    # Aplicar inline method
    def mas_de_10_segundos_sin_comer(self) -> bool:
        return datetime.now() - self.__ultimo_alimento > timedelta(seconds=10)
    
    def mas_de_20_segundos_sin_comer(self) -> bool:
        return datetime.now() - self.__ultimo_alimento > timedelta(seconds=20)
    
    def mas_de_5_segundos_sin_comer(self) -> bool:
        return datetime.now() - self.__ultimo_alimento > timedelta(seconds=5)
    
    # Aplicar extract variable
    @property
    def peligrosidad(self):
        ''' Regresa el nivel de peligrosidad del zombie en tres niveles
            alta, media o baja '''
        if not (self.__tipo == TipoZombie.ZOMBIEINSTEIN or self.__tipo == TipoZombie.ZOMBIEPULTA) and (self.estado_de_animo == 'contento' or self.estado_de_animo == 'normal') and self.__cerebros_devorados >= 1:
            return 'baja'
        elif not (self.__tipo == TipoZombie.ZOMBIEINSTEIN or self.__tipo == TipoZombie.ZOMBIEPULTA) and not (self.estado_de_animo == 'contento' or self.estado_de_animo == 'normal') and self.__cerebros_devorados >= 1:
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

    # Aplicar replace temp with query
    def ir(self, lugar, tiempo_del_recorrido: timedelta):
        ''' Regresa un mensaje con los detalles del recorrido, además de un valor
            boolean que indica si el zombie debería de ir a tal lugar basado en
            el tiempo de vida que le queda '''
        if self.tiempo_de_vida_total - (datetime.now() - self.__timestamp) >= tiempo_del_recorrido: # usar tiempo_de_vida_restante
            return f'Adelante, puede ir al {lugar}', True
        else:
            return f'No se recomienda ir al {lugar}. Desaparecerá antes', False
    
    # Aplicar Split temporary variable
    def buscar_cerebros(self, radio: int):
        ''' Regresa los detalles asociados a la búsqueda de cerebros. El
            radio está en kilómetros'''
        return f'''Detalles de la búsqueda
        perímetro: {2 * pi * radio} km
        radio    : {pi * pow(radio, 2)} km
        '''
    
    def construir_refugio(self, ramas, tipo):
        # Necesitamos 4 postes y 4 paredes
        self.refugio = Construccion(ramas, tipo)
        return 'Refugio {} construido. postes: {}, paredes: {}'.format(
            tipo,
            self.refugio.construirObjeto('poste', 4),
            self.refugio.construirObjeto('pared', 4)
        )

class ZombieBailarin(Zombie):
    def __init__(self, nombre):
        super().__init__(nombre, TipoZombie.ZOMBIEBAILARIN, 1.5)


if __name__ == "__main__":
    # Creamos al zombie
    zombie_bailarin = ZombieBailarin('Zombie bailarín 1')

    # Esperamos un poco antes de preguntar por sus detalles
    print('-I- Buscando cerebros...')
    sleep(4)
    print('-I- Encontramos uno, a comer...')
    zombie_bailarin.comer()
    print('-I- Buscando cerebros...')
    print(f'-I- {zombie_bailarin.buscar_cerebros(2)}')
    sleep(3)

    # Obtenemos los detalles de nuestro Zombie
    print(zombie_bailarin.info())

    # Hacemos uso de la propiedad estado_de_animo que a su vez reusa el código
    # dentro de la propiedad tiempo_sin_alimento
    print(f'-I- Nuestro zombie está {zombie_bailarin.estado_de_animo}')

    # Ahora obtenemos su peligrosidad
    print(f'-I- Peligrosidad: {zombie_bailarin.peligrosidad}')

    # Generemos un refugio, necesitamos 4 postes y 4 paredes de madera
    print('-I- Creando un refugio...')
    ramas = 1200
    print(zombie_bailarin.construir_refugio(ramas, 'apocalipsis'))

    # Veamos cuantas ramas nos sobran
    print(f'De las {ramas} ramas, despues de contruir quedan {zombie_bailarin.refugio.ramas}')