from abc import ABC, abstractmethod

# -----------------------------------------------------------------------------
# 1.- Interface (Componente)
# -----------------------------------------------------------------------------
# Es opcional
# El Componente declara la interfaz común tanto para wrappers como para objetos
# envueltos
# -----------------------------------------------------------------------------
class Enmascarado(ABC):
    @abstractmethod
    def usar(self) -> str:
        pass

# -----------------------------------------------------------------------------
# 2.- Componentes Concretos
# -----------------------------------------------------------------------------
# Componente Concreto es una clase de objetos envueltos. Definen el
# comportamiento básico, que los decoradores pueden alterar
# -----------------------------------------------------------------------------
class Link(Enmascarado):
    def usar(self) -> str:
        return "Link"
    
    def andar(self) -> str:
        return "Caminando..."

class SkullKid(Enmascarado):
    def usar(self) -> str:
        return "Skull Kid"
    
    def andar(self) -> str:
        return "Volando..."

# -----------------------------------------------------------------------------
# 3.- Clase Decoradora
# -----------------------------------------------------------------------------
# La clase Decoradora Base tiene un campo para referenciar un objeto envuelto.
# El tipo del campo debe declararse como la interfaz del componente para que
# pueda contener tanto los componentes concretos como los decoradores.
# La clase decoradora base delega todas las operaciones al objeto envuelto.
# -----------------------------------------------------------------------------
class Decorator(Enmascarado):

    def __init__(self, mascara: Enmascarado) -> None:
        self._mascara = mascara

    @property
    def mascara(self) -> str:
        return self._mascara

# -----------------------------------------------------------------------------
# 4.- Decoradores Concretos
# -----------------------------------------------------------------------------
# Los Decoradores Concretos definen funcionalidades adicionales que se pueden
# añadir dinámicamente a los componentes. Los decoradores concretos sobrescriben
# métodos de la clase decoradora base y ejecutan su comportamiento, ya sea antes
# o después de invocar al método padre.
# -----------------------------------------------------------------------------
class MascaraDeku(Decorator):
    def usar(self) -> str:
        '''
        Habilidades: Entrar en flores deku y salir despedidos para volar durante
        un tiempo limitado. También podremos disparar burbujas de agua en primera
        persona, hacer ataques dando vueltas sobre nuestro propio eje y dar hasta
        cinco saltos sobre el agua.
        '''
        return f"MascaraDeku({self.mascara.usar()})"

class MascaraGoron(Decorator):
    def usar(self) -> str:
        '''
        Ganamos en fuerza bruta y podremos pegar puñetazos, saltar y dar un golpe
        fuerte en el suelo o empezar a rodar para acabar saliendo despedidos a gran
        velocidad, algo ideal para hacer saltos de gran distancia.
        '''
        return f"MascaraGoron({self.mascara.usar()})"
    
    def punetazo(self):
        print('-I- Pengando un puñetazos...')

class MascaraZora(Decorator):
    def usar(self) -> str:
        '''
        Podemos andar sin problemas dentro del mar.
        '''
        return f"MascaraGoron({self.mascara.usar()})"

# -----------------------------------------------------------------------------
# Cliente
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    link = Link()
    print('-I- Link:', link.andar())
    skull_kid = SkullKid()
    print('-I- Skull Kid:', skull_kid.andar())
    print(f'-I- Eligimos a un personaje que usa mascaras: {link.usar()}')
    print('*' * 80)

    # Decorators (Mascaras)
    mascara_deku = MascaraDeku(link)
    print('-I- Usando mascara: ', mascara_deku.usar())
    mascara_goron = MascaraGoron(link)
    print('-I- Usando mascara: ', mascara_goron.usar())
    mascara_goron.punetazo()
    print('-I- Enmascarando a: ', mascara_goron.mascara)
    print('*' * 80)

    # Ahora Skull Kid roba las mascaras
    mascara_goron = MascaraGoron(skull_kid)
    print('-I- Usando mascara: ', mascara_goron.usar())
    mascara_goron.punetazo()
    print('-I- Enmascarando a: ', mascara_goron.mascara)
    print('-I- Es momento de irnos.', mascara_goron.mascara.andar())