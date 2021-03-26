from abc import ABC, abstractmethod

# 1.- Abstracción
# La Abstracción ofrece lógica de control de alto nivel
# Depende de que el objeto de la implementación haga el trabajo de bajo nivel.
class Empleado:
    def __init__(self, persona) -> None:
        self.persona = persona

    def pagar(self) -> str:
        return (f'-I- Pagando al empleado...\n'
                f'{self.persona.pagar()}')

    # Queremos delegar la llamada a traves del objeto persona
    # -->
    def pagar_profesor(self):
        ''' Pagamos al profesor por horas trabajadas'''

    def pagar_administrativo(self):
        ''' Pagamos al administrativo un salario fijo '''

    def pagar_empleado_confianza(self):
        ''' Pagamos al empleado de confianza un bono adicional '''
    # <---

    def ver_perfil(self):
        pass

    def correr(self):
        pass

# 2.- Implementación
# La Implementación declara la interfaz común a todas las implementaciones
# concretas. Una abstracción sólo se puede comunicar con un objeto de
# implementación a través de los métodos que se declaren aquí.
# La abstracción puede enumerar los mismos métodos que la implementación,
# pero normalmente la abstracción declara funcionalidades complejas que 
# dependen de una amplia variedad de operaciones primitivas declaradas
# por la implementación.
class Persona(ABC):
    @abstractmethod
    def pagar(self) -> str:
        pass

# 3.- Implementaciones concretas
# Las Implementaciones Concretas contienen código específico de plataforma.
class Profesor(Persona):

    PAGO_POR_HORA = 100

    def __init__(self, horas:int = 8):
        self.horas = horas

    def pagar(self) -> str:
        return (f'    La nómina ha sido depositada al Profesor\n'
                f'    {self.horas} horas x ${Profesor.PAGO_POR_HORA} pesos = ${self.horas * self.PAGO_POR_HORA}')

class Administrativo(Persona):
    def pagar(self) -> str:
        return ('    La nómina ha sido depositada al Administrativo\n'
                '    $50,0000 pesos como pago fijo')

# 4.- Abstracciones refinadas
# Las Abstracciones Refinadas proporcionan variantes de lógica de control
# Como sus padres, trabajan con distintas implementaciones a través de la
# interfaz general de implementación.
class EmpleadoConfianza(Empleado):
    def pagar(self) -> str:
        return ('-I- Pagando al empleado de confianza...\n'
                f'{self.persona.pagar()}\n'
                '    Bono adicional de $3,000 pesos')

if __name__ == "__main__":

    escuela = [
        Empleado(Profesor(4)),
        EmpleadoConfianza(Profesor()),
        Empleado(Administrativo()),
        Empleado(Profesor(12))
    ]

    # El pago de la nomina en el codigo del cliente resulta sumamente sencillo
    for empleado in escuela:
        print(empleado.pagar())