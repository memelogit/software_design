from __future__ import annotations
from abc import ABC, abstractmethod

# Context
class TerminalBancaria():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def realizar_cargo(self, monto:int) -> None:
        print('TerminalBancaria: Ingreses su')
        self._strategy.cobrar(monto)

# Strategy
class Strategy(ABC):
    @abstractmethod
    def cobrar(self, cantidad:int):
        pass

# Concrete Strategies
class Contado(Strategy):
    def cobrar(self, cantidad:int) -> None:
        print(f'-I- Cobrando ${cantidad} pesos en un solo pago')

class Meses(Strategy):
    def cobrar(self, cantidad:int, meses:int=3) -> None:
        print(f'-I- Cobrando ${cantidad} pesos a meses. ${round(cantidad/meses, 2)} cada mes.')

class Puntos(Strategy):
    def cobrar(self, cantidad:int) -> None:
        print(f'-I- Cobrando ${cantidad} pesos en puntos. {cantidad*10} gastados.')

# Client code
if __name__ == "__main__":
    print('-I- Terminal BBVA')
    monto = float(input('monto: $'))
    print('-I- Opciones de pago:')
    print('    1.- Contado')
    print('    2.- 3 meses sin intereses')
    print('    3.- Puntos BBVA')
    opcion = int(input('opcion: '))
    if opcion == 1:
        strategy = Contado()
    elif opcion == 2:
        strategy = Meses()
    elif opcion == 3:
        strategy = Puntos()
    else:
        raise NotImplementedError('Opcion no definida')
    
    # Llamamos 
    TerminalBancaria(strategy).realizar_cargo(monto)