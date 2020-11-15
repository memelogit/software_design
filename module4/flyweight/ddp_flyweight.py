from random import randint, choice

# -----------------------------------------------------------------------------
# 1.- Flyweight
# -----------------------------------------------------------------------------
# La clase Flyweight contiene la parte del estado del objeto original que pueden
# compartir varios objetos. El mismo objeto flyweight puede utilizarse en muchos
# contextos diferentes. El estado almacenado dentro de un objeto flyweight se
# denomina intrínseco.
# -----------------------------------------------------------------------------
class TipoArbol():
    
    def __init__(self, caracteristicas: str) -> None:
        self.caracteristicas = caracteristicas

# -----------------------------------------------------------------------------
# 2.- Fábrica flyweightx
# -----------------------------------------------------------------------------
# La Fábrica flyweight gestiona un grupo de objetos flyweight existentes.
# Con la fábrica, los clientes no crean objetos flyweight directamente. En lugar
# de eso, invocan a la fábrica, pasándole partes del estado intrínseco del objeto
# flyweight deseado.
# -----------------------------------------------------------------------------
class FabricaArboles():

    __tipo_arboles = {}

    def __init__(self, estados_iniciales: list) -> None:
        for estado in estados_iniciales:
            self.__tipo_arboles[self.generar_llave(estado)] = TipoArbol(estado)

    def generar_llave(self, estado: list) -> str:
        return "_".join(sorted(estado))

    def obtener(self, caracteristicas: list) -> TipoArbol:
        llave = self.generar_llave(caracteristicas)

        if not self.__tipo_arboles.get(llave):
            print('-W- El tipo de arbol no está definido. Creando uno nuevo...')
            self.__tipo_arboles[llave] = TipoArbol(caracteristicas)
        else:
            print('-E- El tipo de arbol ya existe')

        return self.__tipo_arboles[llave]

    def listar_tipos(self) -> None:
        print(f'-I- Lista de tipos de arboles, total: {len(self.__tipo_arboles)}')
        for arbol in self.__tipo_arboles.keys():
            print('    -', arbol)


# -----------------------------------------------------------------------------
# 3.- Contexto
# -----------------------------------------------------------------------------
# La clase Contexto contiene el estado extrínseco, único en todos los objetos
# originales. Cuando un contexto se empareja con uno de los objetos flyweight,
# representa el estado completo del objeto original.
# -----------------------------------------------------------------------------
class Arbol:
    def __init__(self, x:int, y:int, tipo:TipoArbol):
        self.x = x
        self.y = y
        self.tipo = tipo # asociación con la clase TipoArbol
    
class Bosque:
    def __init__(self, fabrica:FabricaArboles):
        self.__arboles = []
        self.__fabrica = fabrica
    
    def plantar(self, x:int, y:int, *tipo:list):
        self.__fabrica.obtener(tipo)
        self.__arboles.append(Arbol(x, y, tipo))
        print('-I- Plantando arbol "{}" en x:{}, y:{}'.format(
            self.__fabrica.generar_llave(tipo),
            x,
            y
        ))


if __name__ == "__main__":
    
    # Definimos los tipos de arboles disponibles
    tipos_arboles = [
        ['cerezo', 'hoja_caduca'],
        ['nogal', 'hoja_caduca'],
        ['pino', 'hoja_perene'],
        ['olivo', 'hoja_perene'],
        ['mango', 'frutal'],
        ['naranjo', 'frutal']
    ]

    # Arboles a plantar
    arboles_seleccionados = tipos_arboles[::2]

    # Agregamos los arboles a la fabrica
    almacen_arboles = FabricaArboles(arboles_seleccionados)

    # Creamos el bosque (Contexto)
    print('-I- Creando bosque...')
    colomos = Bosque(almacen_arboles)
    colomos.plantar(randint(0,1000), randint(0,1000), 'alcanfor', 'totoro', 'gigante')
    for _ in range(100):
        colomos.plantar(randint(0,1000), randint(0,1000), *choice(arboles_seleccionados))

    # Comprobemos cuantos tipos de arboles tenemos al final
    almacen_arboles.listar_tipos()

    # Generar UML como un archivo .dot
    # > pyreverse file.py