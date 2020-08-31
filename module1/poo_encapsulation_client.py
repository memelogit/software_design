import poo_encapsulation_library as encap

class Aeropuerto:
    def aceptar(self, transporteAereo):
        return isinstance(transporteAereo, encap.TransporteAereo)

volaris747 = encap.Avion('GDL', 'OAK', 416)
avioncito = encap.AvionPapel()
benitoJuarez = Aeropuerto()
print(benitoJuarez.aceptar(volaris747))
print(benitoJuarez.aceptar(avioncito))