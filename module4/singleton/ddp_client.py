from ddp_library_class import Sesion

s1 = Sesion('usuario1')
s2 = Sesion('usuario2')

print('-I- usuario en la sesion:', Sesion.obtener_sesion().usuario)

# Eliminamos a la instancia mediante el método logout
print('logout')
print('-' * 80)
s1.logout()

s3 = Sesion('usuario3')
s4 = Sesion('usuario4')
s5 = Sesion('usuario5')
print('-I- usuario en la sesion:', Sesion.obtener_sesion().usuario)