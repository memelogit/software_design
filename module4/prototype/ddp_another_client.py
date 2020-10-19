from ddp_library import Circulo, Rectangulo, FiguraAbstracta

# En este caso, el cliente no sabe cual es el tipo de objeto
# a clonar. Tampoco conoce sus métodos o atributos, solamente
# quiere clonar objetos
def maquina_clonadora(figura: FiguraAbstracta, copias: int = 1):
    for i in range(0, copias):
        clon = figura.deepcopy()
        print(f'-I- Clonando {i+1} de {copias} -> {clon}')
    
maquina_clonadora(Circulo(2), 3)