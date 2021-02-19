class Rectangulo:
    def __init__(self, ancho, alto):
        self._alto = alto
        self._ancho = ancho

    @property
    def area(self) -> int:
        return self._ancho * self._alto

    def __str__(self) -> str:
        return f'ancho: {self.ancho}, alto: {self.alto}'

    @property
    def ancho(self) -> int:
        return self._ancho

    @ancho.setter
    def ancho(self, valor) -> None:
        self._ancho = valor

    @property
    def alto(self) -> int:
        return self._alto

    @alto.setter
    def alto(self, valor) -> None:
        self._alto = valor


class Cuadrado(Rectangulo):
    def __init__(self, tamaño):
        super().__init__(tamaño, tamaño)

    @Rectangulo.ancho.setter
    def ancho(self, valor) -> None:
        self._ancho = self._alto = valor

    @Rectangulo.alto.setter
    def alto(self, valor) -> None:
        self._ancho = self._alto = valor


def usar(rc):
    alto = rc.alto
    ancho = rc.ancho
    rc.ancho = 2 # Comportamiento no esperado
    expected = int(alto * ancho)
    print(f'Se espera un área de {expected}, se obtiene {rc.area}')


rectangulo1 = Rectangulo(2, 3)
cuadrado1 = Cuadrado(5)
usar(rectangulo1)

# Si Cuadrado es un subtipo de Rectángulo, entonces los objetos del tipo
# Rectángulo pueden ser remplazados con objetos del tipo Cuadrado sin 
# alterar el funcionamiento del programa
usar(cuadrado1)
