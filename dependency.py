class Videocasetera:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def iniciar(self):
        pass

    def parar(self):
        pass

    def rebobinar(self):
        pass

    def reproducirEn(self, canal):
        print('reproduciendo... {}'. format(
            canal.sintonizar()
        ))

class Canal:
    def __init__(self, numero_de_canal):
        self.numero_de_canal = numero_de_canal
    
    def sintonizar(self):
        return 'sintonizando canal {}'.format(
            self.numero_de_canal
        )

canal3 = Canal(3)
vcr1 = Videocasetera('VCR_1')
vcr1.reproducirEn(canal3)