from dp_library import AgeOfEmpire

mundo = AgeOfEmpire.crearMundo(AgeOfEmpire.Civilizaciones.AZTECA)
aldeano1 = mundo.crear_aldeano()
arquero1 = mundo.crear_arquero()
milicia1 = mundo.crear_milicia()
aldeano1.recolectar()
milicia1.atacar()