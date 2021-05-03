from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Curso(ABC):
    @abstractmethod
    def aceptar(self, visitor: Visitor) -> None:
        pass

    def descargar_lista_estudiantes(self):
        return 'Descargando lista de estudiantes'

class DDS(Curso):
    def aceptar(self, visitor: Visitor) -> None:
        print('-I- Curso diseno de software (DDS)')
        visitor.visitar_dds(self)

    def descargar_codigos(self) -> str:
        return 'Descargando codigos de GitHub'

class DB(Curso):
    def aceptar(self, visitor: Visitor):
        print('-I- Curso bases de datos (DB)')
        visitor.visitar_db(self)

    def montar_db(self) -> str:
        return 'Montando MongoDB'

# Visitor
class Visitor(ABC):
    @abstractmethod
    def visitar_dds(self, element: DDS) -> None:
        pass

    @abstractmethod
    def visitar_db(self, element: DB) -> None:
        pass

class Profesor(Visitor):
    def visitar_dds(self, element) -> None:
        print(f'-I- Profesor: {element.descargar_lista_estudiantes()}')
        # print(f'-I- Profesor: {element.descargar_codigos()}')

    def visitar_db(self, element) -> None:
        print(f'-I- Profesor: {element.descargar_lista_estudiantes()}')
        # print(f'-I- Profesor: {element.montar_db()}')


class Estudiante(Visitor):
    def visitar_dds(self, element) -> None:
        print(f'-I- Estudiante: {element.descargar_codigos()}')

    def visitar_db(self, element) -> None:
        print(f'-I- Estudiante: {element.montar_db()}')


def canvas(components: List[Curso], visitor: Visitor) -> None:
    for component in components:
        component.aceptar(visitor)


if __name__ == "__main__":
    components = [DDS(), DB()]

    print('Bienvenido a Canvas')
    visitor1 = Profesor()
    canvas(components, visitor1)

    print('\nBienvenido a Canvas')
    visitor2 = Estudiante()
    canvas(components, visitor2)