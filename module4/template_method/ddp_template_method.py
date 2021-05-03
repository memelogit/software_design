from abc import ABC, abstractmethod


class RedesNeuronales(ABC):
    def template_method(self) -> None:
        self.descargar_dataset()
        self.limpieza_de_datos()
        self.definir_set_entrenamiento()
        self.checkpoint1()
        self.definir_modelo()
        self.entrenar()
        self.checkpoint2()

    # Metodos con comportamientos por defecto
    def descargar_dataset(self) -> None:
        print('-I- Descargando dataset de imagenes desde https://www.kaggle.com/c/diabetic-retinopathy-detection/data/')

    def definir_set_entrenamiento(self) -> None:
        print('-I- 32,000 imagenes encontradas, definiendo 80% para entrenamiento y 20% para prueba')

    def entrenar(self) -> None:
        print('-I- Entrenando modelo')

    # Metodos abstractos a implementar en las subclases
    @abstractmethod
    def limpieza_de_datos(self) -> None:
        pass

    @abstractmethod
    def definir_modelo(self) -> None:
        pass

    # Metodos opcionales para implementar en las subclases
    def checkpoint1(self) -> None:
        pass

    def checkpoint2(self) -> None:
        pass

class Clasificacion(RedesNeuronales):
    def limpieza_de_datos(self) -> None:
        print('-I- Mofificando imagenes...')

    def definir_modelo(self) -> None:
        print('-I- Agregando capas: Conv2D, Conv2D, Conv2D, Densa, Densa')

class DeteccionObjetos(RedesNeuronales):
    def limpieza_de_datos(self) -> None:
        print('-I- Ajustando tamano y bandas de la imagen')

    def definir_modelo(self) -> None:
        print('-I- Agregando capas: Conv2D, Densa, Densa')

    def checkpoint1(self) -> None:
        print('-I- Revisando que cada imagen tenga un BBOX asociado')


if __name__ == "__main__":
    print('-I- Creando proyecto de clasificacion de imagenes')
    Clasificacion().template_method()
    
    print('\n-I- Creando proyecto de deteccion de objetos en imagenes')
    DeteccionObjetos().template_method()