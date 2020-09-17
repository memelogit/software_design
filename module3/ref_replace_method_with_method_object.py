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
    
    # Las variables en este método están entrelazadas con las del método
    # construirRefugio
    def construirPostes(self, ramas, tipo):
        poste_simple = 2
        poste_grueso = 4
        poste_apocalipsis = 8

        if tipo == 'simple':
            if ramas > poste_simple:
                return int(ramas / poste_simple)
            else:
                return 0
        elif tipo == 'grueso':
            if ramas > poste_grueso:
                return int(ramas / poste_grueso)
            else:
                return 0
        elif tipo == 'apocalipsis':
            if ramas > poste_apocalipsis:
                return int(ramas / poste_apocalipsis)
            else:
                return 0
        else:
            raise Exception('el tipo de poste no es válido')
    
    # Las variables en este método están entrelazadas con las del método
    # construirRefugio
    def construirPared(self, ramas, tipo):
        pared_simple = 20
        pared_grueso = 35
        pared_apocalipsis = 80

        if tipo == 'simple':
            if ramas > pared_simple:
                return int(ramas / pared_simple)
            else:
                return 0
        elif tipo == 'gruesa':
            if ramas > pared_grueso:
                return int(ramas / pared_grueso)
            else:
                return 0
        elif tipo == 'apocalipsis':
            if ramas > pared_apocalipsis:
                return int(ramas / pared_apocalipsis)
            else:
                return 0
        else:
            raise Exception('el tipo de poste no es válido')
    
    # Las variables en este método están entrelazadas con las del método
    # construirPared y construirPoste
    def construirRefugio(self, ramas, tipo):
        poste_simple = 2
        poste_grueso = 4
        poste_apocalipsis = 8
        pared_simple = 20
        pared_gruesa = 35
        pared_apocalipsis = 80

        # Necesitamos 4 postes y 4 paredes
        if tipo == 'simple':
            ramas_requeridas_postes = 4 * poste_simple
            ramas_requeridas_pared = 4 * pared_simple
            if ramas_requeridas_postes + ramas_requeridas_pared > ramas:
                return 'El refugio no se puede construir. Hacen falta mas ramas'
        elif tipo == 'gruesa':
            ramas_requeridas_postes = 4 * poste_grueso
            ramas_requeridas_pared = 4 * pared_gruesa
            if ramas_requeridas_postes + ramas_requeridas_pared > ramas:
                return 'El refugio no se puede construir. Hacen falta mas ramas'
        elif tipo == 'apocalipsis':
            ramas_requeridas_postes = 4 * poste_apocalipsis
            ramas_requeridas_pared = 4 * pared_apocalipsis
            if ramas_requeridas_postes + ramas_requeridas_pared > ramas:
                return 'El refugio no se puede construir. Hacen falta mas ramas'
        
        return 'Refugio {} construido. postes: {}, paredes: {}'.format(
            tipo,
            self.construirPostes(ramas_requeridas_postes, tipo),
            self.construirPared(ramas_requeridas_pared, tipo)
        )

class ZombieBailarin(Zombie):
    def __init__(self, nombre):
        super().__init__(nombre, TipoZombie.ZOMBIEBAILARIN, 1.5)

# Creamos al zombie
zombie_bailarin = ZombieBailarin('Zombie bailarín 1')

# Generemos un refugio, necesitamos 4 postes y 4 paredes de madera
print('-I- Creando un refugio...')
print(zombie_bailarin.construirRefugio(120, 'apocalipsis'))