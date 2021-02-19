from datetime import datetime, timedelta
from enum import Enum, unique
from time import sleep

@unique
class TipoZombie(Enum):
    ''' Clase usada para especificar el tipo de Zombie '''
    ZOMBIEBAILARIN = 1
    ZOMBIEPULTA    = 2
    ZOMBIEINSTEIN  = 3
    ZOMBIEACUATICO = 4
    ZOMBIEVOLADOR  = 5

class Zombie:

    NORMAL   =  5
    ENFADADO = 10
    AGRESIVO = 20

    def __init__(self, nombre:str, tipo:TipoZombie):
        if not isinstance(tipo, TipoZombie):
            raise Exception('-E- Tipo de Zombie inválido')
        self._nombre = nombre
        self._tipo = tipo
        self._ultimo_alimento = datetime.now()
        self._cerebros_devorados = 0

    def __str__(self) -> str:
        return self.info()

    # INLINE VARIABLE
    # No es necesario hacer uso de una variable local temporal. Simplemente
    # retornamos el resultado de la expresión y nada mas.
    @property
    def tiempo_sin_alimento(self) -> timedelta:
        ''' Regresa el tiempo transcurrido desde la última vez que nuestro zombie comió '''
        return datetime.now() - self._ultimo_alimento

    def info(self) -> str:
        ''' Retorna los detalles de nuestro Zombie incluyendo cuanto
            tiempo ha pasado desde su último cerebro.'''
        return f'''
        Zombi
        --------------------
        Nombre:         {self._nombre}
        Tipo:           {self._tipo.name}
        Último cerebro: {self.tiempo_sin_alimento}
        '''

    def comer(self) -> None:
        ''' Reinicia el tiempo que ha pasado sin alimento nuestro zombie '''
        self._ultimo_alimento = datetime.now()
        self._cerebros_devorados += 1

    @property
    def estado_de_animo(self) -> str:
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
    def peligrosidad(self) -> str:
        ''' Regresa el nivel de peligrosidad del zombie en tres niveles alta, media o baja '''
        tipo_agresivo = self._tipo == TipoZombie.ZOMBIEINSTEIN or self._tipo == TipoZombie.ZOMBIEPULTA
        con_buen_animo = self.estado_de_animo == 'contento' or self.estado_de_animo == 'normal'
        if not tipo_agresivo and con_buen_animo and self._cerebros_devorados >= 1:
            return 'baja'
        elif not tipo_agresivo and not con_buen_animo and self._cerebros_devorados >= 1:
            return 'media'
        else:
            return 'alta'

class ZombieBailarin(Zombie):
    def __init__(self, nombre:str):
        super().__init__(nombre, TipoZombie.ZOMBIEBAILARIN)
    
if __name__ == "__main__":
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