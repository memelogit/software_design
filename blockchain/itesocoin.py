############################################################################################################
#
#  ItesoCoin - Una Simulación de Blockchain
#
#  Este archivo contiene las definiciones de clases y funciones relacionadas con ItesoCoin, una
#  criptomoneda ficticia basada en la tecnología blockchain.
#
#  Clase Block:
#  - Representa un bloque en la cadena de bloques de ItesoCoin.
#  - Contiene atributos como la marca de tiempo, las transacciones, el bloque previo, el incremento
#    y el hash.
#  - Proporciona métodos para calcular el hash del bloque y realizar la minería.
#
#  Clase Transaction:
#  - Utilizada para representar transacciones en ItesoCoin con información de origen, destino y cantidad.
#
#  Clase Blockchain:
#  - Representa la infraestructura de ItesoCoin y permite la gestión de transacciones, minería de
#    bloques y validación de la cadena.
#  - Incluye métodos para crear bloques, realizar transacciones, calcular el saldo y validar la cadena.
#
#  Nota: Este código es una simulación con fines educativos y no se debe considerar funcional para
#  una criptomoneda real.
#
############################################################################################################

from __future__ import annotations

import hashlib
import datetime

class Block:
    '''
    Clase que representa un bloque en una cadena de bloques.

    Atributos:
        - timestamp (datetime): La marca de tiempo que indica cuándo se creó el bloque.
        - transacciones (list[Transaction]): Lista de transacciones incluidas en el bloque.
        - bloque_previo (Block, opcional): El bloque previo en la cadena de bloques. None si es el bloque génesis.
        - incremento (int): Un número que se incrementa para calcular el hash del bloque.
        - hash (str): El hash del bloque calculado a partir de sus datos.

    Métodos:
        - calcular_hash(datos: str, timestamp: datetime, incremento: int) -> str: Calcula el hash del bloque.
        - minar(repeticiones: int) -> None: Realiza la minería del bloque para encontrar un hash con el número deseado de ceros iniciales.
        - __str__() -> str: Devuelve una representación en cadena de los atributos del bloque.
    '''

    def __init__(self, timestamp: datetime, transacciones: list[Transaction], bloque_previo:Block = None) -> None:
        '''
        Inicializa un nuevo bloque con los datos proporcionados.

        Args:
            - timestamp (datetime): La marca de tiempo que indica cuándo se creó el bloque.
            - transacciones (list[Transaction]): Lista de transacciones incluidas en el bloque.
            - bloque_previo (Block, opcional): El bloque previo en la cadena de bloques. None si es el bloque génesis.

        Retorna:
            None
        '''
        self.timestamp: datetime = timestamp
        self.transacciones: list[Transaction] = transacciones
        self.bloque_previo: Block = bloque_previo
        self.incremento: int = 1
        self.hash = self.calcular_hash(transacciones, timestamp, self.incremento)

    def calcular_hash(self, datos:str, timestamp:datetime, incremento:int) -> str:
        '''
        Calcula el hash del bloque en función de los datos proporcionados.

        Args:
            - datos (str): Datos del bloque en forma de cadena.
            - timestamp (datetime): La marca de tiempo que indica cuándo se creó el bloque.
            - incremento (int): Un número que se incrementa para calcular el hash del bloque.

        Retorna:
            str: El hash calculado como una cadena hexadecimal.
        '''
        entrada = str(datos) + str(timestamp) + str(incremento)
        entrada = entrada.encode()
        hash = hashlib.sha256(entrada)
        return hash.hexdigest()

    def minar(self, repeticiones: int) -> None:
        '''
        Realiza la minería del bloque para encontrar un hash con el número deseado de ceros iniciales.

        Args:
            - repeticiones (int): El número de ceros iniciales requeridos en el hash.

        Retorna:
            None
        '''
        check = "0" * repeticiones
        while self.hash[:repeticiones] != check:
            self.hash = self.calcular_hash(self.transacciones, self.timestamp, self.incremento)
            self.incremento += 1
    
    def __str__(self) -> str:
        '''
        Devuelve una representación en cadena de los atributos del bloque.

        Retorna:
            str: Una cadena que representa los atributos del bloque.
        '''
        return str(self.__dict__)

class Transaction:
    '''
    Clase utilizada para representar transacciones como objetos.

    Atributos:
        - origen (str): La dirección del remitente en la transacción.
        - destino (str): La dirección del destinatario en la transacción.
        - cantidad (float): La cantidad de la transacción.

    Método:
        - __init__(self, origen: str, destino: str, cantidad: float): Inicializa una nueva transacción con los datos proporcionados.
    '''

    def __init__(self, origen: str, destino: str, cantidad: float):
        '''
        Inicializa una nueva transacción con los datos proporcionados.

        Args:
            - origen (str): La dirección del remitente en la transacción.
            - destino (str): La dirección del destinatario en la transacción.
            - cantidad (float): La cantidad de la transacción.

        Retorna:
            None
        '''
        self.origen: str = origen
        self.destino: str = destino
        self.cantidad: float = cantidad

class Blockchain:
    '''
    La clase Blockchain representa la infraestructura de ItesoCoin, una criptomoneda ficticia. 
    Permite la gestión de transacciones, minería de bloques y verificación de la integridad de la cadena.

    Atributos:
    - chain (list): Una lista de bloques que conforman la cadena de bloques.
    - repeticiones (int): El número de repeticiones requeridas para la minería de un nuevo bloque.
    - transacciones_pendientes (list): Lista de transacciones pendientes de ser incluidas en un bloque.
    - recompensa (int): La recompensa otorgada al minero por añadir un nuevo bloque a la cadena.

    Métodos:
    - generar_bloque(): Genera un nuevo bloque con una marca de tiempo actual y un mensaje inicial.
    - ultimo_bloque(): Obtiene el último bloque en la cadena.
    - minar(destino: str): Realiza la minería de un nuevo bloque y lo agrega a la cadena.
    - validar(): Verifica la integridad de la cadena de bloques.
    - crear_transaccion(transaction): Crea una nueva transacción y la agrega a las transacciones pendientes.
    - balance(cartera: str): Calcula el saldo de una cartera específica en ItesoCoin.

    Ejemplo de uso:
    blockchain = Blockchain()
    bloque_previo = blockchain.ultimo_bloque()
    nueva_transaccion = Transaction("cartera_origen", "cartera_destino", 10)
    blockchain.crear_transaccion(nueva_transaccion)
    blockchain.minar("cartera_minero")
    balance_cartera = blockchain.balance("cartera_destino")
    '''

    def __init__(self) -> None:
        '''
        Inicializa una nueva instancia de la cadena de bloques de ItesoCoin.
        '''
        self.chain: list[Block] = [self.generar_bloque()]
        self.repeticiones: int = 5
        self.transacciones_pendientes: list = []
        self.recompensa: int = 1
    
    def generar_bloque(self) -> Block:
        '''
        Genera un nuevo bloque con una marca de tiempo actual y un mensaje inicial.
        Retorna el bloque recién creado.
        '''
        return Block(datetime.datetime.now(), "Primer Bloque")

    def ultimo_bloque(self) -> Block:
        '''
        Obtiene el último bloque en la cadena de bloques.
        Retorna el bloque más reciente.
        '''
        return self.chain[len(self.chain) - 1]

    def minar(self, destino:str) -> None:
        '''
        Realiza la minería de un nuevo bloque con las transacciones pendientes y lo agrega a la cadena.
        Parámetros:
        - destino (str): La dirección de cartera del destinatario de la recompensa de la minería.

        Este método también otorga una recompensa al minero por agregar un nuevo bloque a la cadena.
        '''
        bloque = Block(datetime.datetime.now(), self.transacciones_pendientes)
        bloque.minar(self.repeticiones)
        bloque.bloque_previo = self.ultimo_bloque()

        print("\nHash Previo " + bloque.bloque_previo.hash)
        for transaccion in bloque.transacciones:
            print('   ==>   origen: {0:<10}   destino: {1:<10}   cantidad: {2:<10}'.format(
                transaccion.origen,
                transaccion.destino,
                transaccion.cantidad
            ))

        self.chain.append(bloque)
        print("Hash: " + bloque.hash)

        transaccion = Transaction("iteso_network", destino, self.recompensa)
        self.transacciones_pendientes.append(transaccion)
        self.transacciones_pendientes = []

    def validar(self) -> bool:
        '''
        Verifica la integridad de la cadena de bloques ItesoCoin.
        Retorna True si la cadena es válida y False si no lo es.
        '''
        for i in range(1, len(self.chain)):
            bloque = self.chain[i]
            bloque_previo = self.chain[i - 1]

            if not bloque.bloque_previo or bloque.bloque_previo.hash != bloque_previo.hash:
                return False
        return True

    def crear_transaccion(self, transaction) -> None:
        '''
        Crea una nueva transacción y la agrega a la lista de transacciones pendientes.
        Parámetros:
        - transaction: La transacción a ser creada y agregada.
        '''
        self.transacciones_pendientes.append(transaction)

    def balance(self, cartera:str) -> float:
        '''
        Calcula el saldo de una cartera en ItesoCoin.
        Parámetros:
        - cartera (str): La dirección de la cartera para la que se desea calcular el saldo.
        Retorna el saldo de la cartera en ItesoCoin.
        '''
        balance: float = 0
        for block in self.chain:
            if block.bloque_previo == None :
                continue 
            for transaction in block.transacciones:
                if transaction.origen == cartera:
                    balance -= transaction.cantidad
                if transaction.destino == cartera:
                    balance += transaction.cantidad
        return round(balance, 8)

if __name__ == '__main__':
    itesocoin = Blockchain()

    # Se registran las primeras transacciones
    itesocoin.crear_transaccion(Transaction('Kury', 'Pablito', 5.2))
    itesocoin.crear_transaccion(Transaction('Kury', 'Daniela', 2.3))
    itesocoin.crear_transaccion(Transaction('Pablito', 'Santiago', 1.2))

    # Minamos un bloque con las transacciones pendientes
    itesocoin.minar('José Carlos')

    # Se registran transaccones adicionales
    itesocoin.crear_transaccion(Transaction('Omar', 'Kury', 2.2))
    itesocoin.crear_transaccion(Transaction('Jennifer', 'Pablito', 0.9))
    itesocoin.crear_transaccion(Transaction('Narda', 'Pablito', 1.4))

    # Minamos el segundo bloque con las transacciones pendientes
    itesocoin.minar('Emiliano')

    # Obtenemos los balances
    print('\n' + '=' * 80)
    print('Balance de Pablito: ', itesocoin.balance('Pablito'))
    print('¿La cadena es válida?: ', itesocoin.validar())

    # Vamos a corromper la cadena
    print('\nAlguien pretende introducir un bloque sin minar')
    bloque = Block(datetime.datetime.now(), [Transaction('Narda', 'Narda', 100)])
    itesocoin.chain.append(bloque)

    # Validamos la cadena
    print('¿La cadena es válida?: ', itesocoin.validar())