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

    ENFADADO = 10
    AGRESIVO = 20

    def __init__(self, nombre:str, tipo:TipoZombie):
        if not isinstance(tipo, TipoZombie):
            raise Exception('-E- Tipo de Zombie inválido')
        self._nombre = nombre
        self._tipo = tipo
        self._ultimo_alimento = datetime.now()

    def __str__(self) -> str:
        return self.info()

    # Esta propiedad era parte del método INFO.
    # Ahora podemos usar la propiedad con libertad sin tener duplicar
    # el código.
    @property
    def tiempo_sin_alimento(self) -> timedelta:
        ''' Regresa el tiempo transcurrido desde la última vez que nuestro zombie comió '''
        return datetime.now() - self._ultimo_alimento
    
    # EXTRACT METHOD:
    # 1.- Agrupamos el código que regresa la información y determina el tiempo
    #     que ha pasado desde el último cerebro.
    # 2.- Creamos el métodos tiempo_sin_alimento que se puede reusar en un futuro.
    # 3.- Reemplazamos el código anterior con una llamada al método.
    def info(self) -> str:
        ''' Retorna los detalles de nuestro Zombie incluyendo cuanto tiempo ha pasado desde su último cerebro.'''
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
    
    # Reusamos el código usado para determinar el tiempo que nuestro zombie ha
    # pasado son alimento a través de la propiedad tiempo_sin_alimento
    @property
    def estado_de_animo(self) -> str:
        ''' Regresa el estado de ánimo de nuestro zombie basado en el tiempo que ha pasado sin comer '''
        if self.tiempo_sin_alimento > timedelta(seconds=self.ENFADADO):
            return 'enfadado'
        if self.tiempo_sin_alimento > timedelta(seconds=self.AGRESIVO):
            return 'agresivo'
        else:
            return 'contento'

class ZombieBailarin(Zombie):
    def __init__(self, nombre):
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
    sleep(11)

    # Obtenemos los detalles de nuestro Zombie
    print(zombie_bailarin.info())

    # Hacemos uso de la propiedad estado_de_animo que a su vez reusa el código
    # dentro de la propiedad tiempo_sin_alimento
    print(f'-I- Nuestro zombie está {zombie_bailarin.estado_de_animo}')