from dp_library import ModoCreativo, ModoSupervivencia

# Supongamos que un jugador selecciona en modo creativo
creativo = ModoCreativo()
creativo.colocar(creativo.TipoBloque.GRANITO)

# Ahora, que otro jugador selecciona modo supervivencia
supervivencia = ModoSupervivencia()
supervivencia.colocar(supervivencia.TipoBloque.HORNO)
piedra1 = supervivencia.crearBloque(supervivencia.TipoBloque.PIEDRA)
piedra1.colocar()