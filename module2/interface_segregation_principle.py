from abc import ABC, abstractmethod

class Maquina(ABC):
    def imprimir(self, documento):
        raise NotImplementedError()

    def enviarFax(self, documento):
        raise NotImplementedError()

    def escanear(self, documento):
        raise NotImplementedError()


# Bien! Implementemos una clase para una impresora multifuncional
class ImpresoraMultifuncional(Maquina):
    def imprimir(self, documento):
        pass

    def enviarFax(self, documento):
        pass

    def escanear(self, documento):
        pass

# Para la impresora viejita no funciona adecuadamente la clase Maquina
class ImpresoraViejita(Maquina):
    def imprimir(self, documento):
        # ok - imprimimos cosas
        pass

    def enviarFax(self, documento):
        pass  # no hacemos nada

    def escanear(self, documento):
        """No soportado!"""
        raise NotImplementedError('La impresora no puede escanear!')

# Rompemos la interfaz Maquina en pequeñas interfaces granulares
class Impresora(ABC):
    @abstractmethod
    def imprimir(self, documento):
        pass

class Scanner(ABC):
    @abstractmethod
    def escanear(self, documento):
        pass

# ...lo mismo para fax, etc

class MiImpresora(Impresora):
    def imprimir(self, documento):
        return 'Imprimiendo documento...\n{}'.format(documento)

class Fotocopiadora(Impresora, Scanner):
    def imprimir(self, documento):
        return 'Imprimiendo documento...\n{}'.format(documento)

    def escanear(self, documento):
        return 'Escaneando documento...\n{}'.format(documento)

# Incluso podemos crear una clase para un equipo multifuncional
class EquipoMultifuncional(Impresora, Scanner):  # , Fax, etc
    @abstractmethod
    def imprimir(self, documento):
        pass

    @abstractmethod
    def escanear(self, documento):
        pass


impresora = ImpresoraViejita()
impresora.enviarFax(123)  # No pasa nada
impresora.escanear(123)   # oops!

copiadora = Fotocopiadora()
print(copiadora.escanear('Hola mundo'))