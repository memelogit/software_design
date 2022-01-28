from __future__ import annotations

class Videocasetera:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def iniciar(self) -> None:
        pass

    def parar(self) -> None:
        pass

    def rebobinar(self) -> None:
        pass

    def reproducirEn(self, canal:Canal) -> str:
        return f'reproduciendo... {canal.sintonizar()}'

class Canal:
    def __init__(self, numero_de_canal:int):
        self.numero_de_canal = numero_de_canal
    
    def sintonizar(self):
        return 'sintonizando canal {}'.format(
            self.numero_de_canal
        )

canal3 = Canal(3)
vcr1 = Videocasetera('VCR_1')
print(vcr1.reproducirEn(canal3))