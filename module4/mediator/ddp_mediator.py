# -----------------------------------------------------------------------------
# 1.- Componente
# -----------------------------------------------------------------------------
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.log = []
        self.sala = None # Referencia al objeto mediador

    def recibir(self, remitente, mensaje: str):
        entrada = f'{remitente.nombre:>15}: {mensaje:<30}'
        print(f'[Sesión de {self.nombre:<6}] {entrada}')
        self.log.append(entrada)

    def enviar_mensaje(self, mensaje):
        self.sala.broadcast(self, mensaje)

    def enviar_mensaje_privado(self, destinatario, mensaje):
        self.sala.mensaje(self, destinatario, mensaje)
    
    def __del__(self):
        if self.sala != None:
            self.sala.salir(self)

# -----------------------------------------------------------------------------
# 2.- Mediador
# -----------------------------------------------------------------------------
class SalaChat:
    def __init__(self):
        self.moderador = Persona('Moderador')
        self.personas = []

    def broadcast(self, remitente: Persona, mensaje: str) -> None:
        for persona in self.personas:
            persona.recibir(remitente, mensaje)

    def mensaje(self, remitente: Persona, destinatario: Persona, mensaje: str) -> None:
        for persona in self.personas:
            if persona == destinatario:
                persona.recibir(remitente, mensaje)

    def unir(self, persona: Persona) -> None:
        self.broadcast(self.moderador, f'{persona.nombre} se unio a la sala')
        persona.sala = self
        self.personas.append(persona)
    
    def salir(self, persona: Persona) -> None:
        self.broadcast(self.moderador, f'{persona.nombre} ha abandonado del chat')
        self.personas.remove(persona)

if __name__ == '__main__':
    sala = SalaChat()

    victor = Persona('Victor')
    sala.unir(victor)
    victor.enviar_mensaje('hola sala')

    ghazal = Persona('Ghazal')
    sala.unir(ghazal)
    ghazal.enviar_mensaje('oh, hola victor, no sabia que estabas conectado')

    # Se une el cemas
    cemas = Persona('Cemas')
    sala.unir(cemas)
    cemas.enviar_mensaje('Que ondas!')

    ghazal.enviar_mensaje_privado(cemas, 'Hey cemas, que bueno que te veo...')
