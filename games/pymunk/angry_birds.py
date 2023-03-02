from __future__ import annotations
from typing import List, Tuple
import pygame
from pymunk.pygame_util import DrawOptions
from pygame import Surface, mixer
from pygame.time import Clock
from pymunk import Body, Space
from colores import CatalogoColores
from objetos import Circulo, Rectangulo, Linea

class AngryBirds:
    ''' Clase principal del juego '''

    ANCHO:int              = 1400
    ALTO:int               =  800
    FRAMES_POR_SEGUNDO:int =   60
    GRAVEDAD_X:int         =    0
    GRAVEDAD_Y:int         =  400

    BORDES:dict = {
        'abajo': {'ancho': ANCHO, 'alto':20, 'pos_x': ANCHO/2, 'pos_y': ALTO - 10},
        'arriba': {'ancho': ANCHO, 'alto':20, 'pos_x': ANCHO/2, 'pos_y': 10},
        'izquierda': {'ancho': 20, 'alto':ALTO, 'pos_x': 10, 'pos_y': ALTO/2},
        'derecha': {'ancho': 20, 'alto':ALTO, 'pos_x': ANCHO - 10, 'pos_y': ALTO/2},
        'suelo': {'ancho': ANCHO, 'alto':1, 'pos_x': ANCHO/2, 'pos_y': 630}
    }

    def __init__(self) -> None:
        self.ventana:Surface = pygame.display.set_mode((AngryBirds.ANCHO, AngryBirds.ALTO))
        self.espacio:Space = Space()
        self.espacio.gravity = (AngryBirds.GRAVEDAD_X, AngryBirds.GRAVEDAD_Y)
        self.opciones_dibujo:DrawOptions = DrawOptions(self.ventana)

        # Interacción
        self.circulo:Circulo = None
        self.linea:Linea = Linea(3)

        pygame.display.set_caption('Diseño de Software - Angry Birds')
        self.logo = pygame.image.load(r"C:\ITESO\diseño de software\code\games\pymunk\background.jpg")
        self.logo = pygame.transform.scale(self.logo, (AngryBirds.ANCHO, AngryBirds.ALTO))

    def _dibujar(self) -> None:
        ''' Dibuja los objetos del espacio '''
        self.ventana.fill(str(CatalogoColores.BLANCO.value))
        
        # Background
        
        self.ventana.blit(self.logo, (0, 0))

        # logo
        logo = pygame.image.load(r"C:\ITESO\diseño de software\code\games\pymunk\logo.png")
        logo = pygame.transform.scale(logo, (200, 76))
        self.ventana.blit(logo, (40, 40))
        
        # Resortera
        logo = pygame.image.load(r"C:\ITESO\diseño de software\code\games\pymunk\resortera.png")
        logo = pygame.transform.scale(logo, (150, 150))
        self.ventana.blit(logo, (240, 480))

        # linea
        if self.linea.disponible:
            pygame.draw.line(self.ventana, CatalogoColores.NEGRO.value.nombre, self.linea.posicion_inicial, self.linea.posicion_final, 3)

        # Objetos
        self.espacio.debug_draw(self.opciones_dibujo)
        
        # Imagenes
        if self.circulo:
            pos_x, pos_y = self.circulo.forma.body.position
            self.ventana.blit(self.circulo.imagen, (pos_x - self.circulo.radio*1.5, pos_y - self.circulo.radio*1.5))
        pygame.display.update()
        self.espacio.step(1 / self.FRAMES_POR_SEGUNDO)

    def _inicializar_objetos(self) -> None:
        ''' Coloca los objetos iniciales sobre la superficie '''
        self._crear_bordes()
        Rectangulo(self.espacio, 20, 100, CatalogoColores.PANTONE652).colocar((1000, 550))
        Rectangulo(self.espacio, 20, 100, CatalogoColores.PANTONE652).colocar((1200, 550))
        Rectangulo(self.espacio, 20, 100, CatalogoColores.PANTONE652).colocar((1000, 450))
        Rectangulo(self.espacio, 20, 100, CatalogoColores.PANTONE652).colocar((1200, 450))

        Rectangulo(self.espacio, 240, 20, CatalogoColores.PANTONE652).colocar((1100, 400))

        Rectangulo(self.espacio, 20, 100, CatalogoColores.PANTONE652).colocar((1100, 250))
        Rectangulo(self.espacio, 20, 100, CatalogoColores.PANTONE652).colocar((1100, 350))
    
    def _crear_bordes(self) -> None:
        ''' Dibuja un borde que circunda la ventana '''
        
        for _, attr in AngryBirds.BORDES.items():
            rectangulo = Rectangulo(
                espacio=self.espacio,
                ancho=attr['ancho'],
                alto=attr['alto'],
                color=CatalogoColores.PANTONE541,
                estilo=Body.STATIC
            )
            rectangulo.elasticidad = 0.4
            rectangulo.friccion = 0.5
            rectangulo.colocar((attr['pos_x'], attr['pos_y']))

    def _boton_mouse_presionado(self) -> None:
        ''' Acciones generales del cuando se presiona el botón derecho del mouse '''
        if not self.circulo:
            self.circulo = Circulo(self.espacio, 20, estilo=Body.STATIC, color=CatalogoColores.ROJO)
            #self.circulo.colocar(pygame.mouse.get_pos())
            self.linea.posicion_inicial = pygame.mouse.get_pos()
            self.circulo.colocar((320, 500))
            self.linea.posicion_inicial = (320, 500)

    def _boton_mouse_liberado(self) -> None:
        ''' Acciones generales del cuando se libera el botón derecho del mouse '''
        if self.circulo:
            self.circulo.forma.body.body_type = Body.DYNAMIC
            if self.linea.disponible:
                self.circulo.forma.body.apply_impulse_at_local_point((self.linea.delta_x*50, self.linea.delta_y*50), (0, 0))
            self.linea.limpiar()

    def _mouse_en_movimiento(self) -> None:
        ''' Acciones generales del cuando se libera el botón derecho del mouse '''
        if self.circulo:
            self.linea.posicion_final = pygame.mouse.get_pos()
    
    def _reproducir_musica(self) -> None:
        ''' Abre el archivo mp3 y lo reproduce '''
        mixer.init()
        mixer.music.load(r'C:\ITESO\diseño de software\code\games\pymunk\cancion.mp3')
        mixer.music.set_volume(0.5)
        mixer.music.play()

    def correr(self) -> None:
        ''' Ejecuta el ciclo principal de PyGame '''
        activo:bool = True
        reloj:Clock = Clock()

        self._inicializar_objetos()
        self._reproducir_musica()

        while activo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    activo = False
                    break
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    self._boton_mouse_presionado()
                elif evento.type == pygame.MOUSEBUTTONUP:
                    self._boton_mouse_liberado()
                elif evento.type == pygame.MOUSEMOTION:
                    self._mouse_en_movimiento()
            
            self._dibujar()
            reloj.tick(AngryBirds.FRAMES_POR_SEGUNDO)
        
        pygame.quit()

if __name__ == '__main__':
    juego = AngryBirds()
    juego.correr()