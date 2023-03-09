# https://www.ursinaengine.org/api_reference.html

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/stone.aiff', loop = False, autoplay = False)
grass_sound = Audio('assets/grass2.wav', loop = False, autoplay = False)

block_pick = 1

window.fps_counter.visible = False
window.exit_button.visible = False
window.fullscreen = True

def update():
    global block_pick

    if held_keys['left mouse'] or held_keys['left mouse']:
        hand.active()
    else:
        hand.pasive()

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4


class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            scale = 0.5,
            highlight_color = color.lime,
        )
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: Voxel(position = self.position + mouse.normal, texture = dirt_texture)
                
            if key == 'right mouse down':
                grass_sound.play()
                destroy(self)

class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150, -10, 0),
            position = Vec2(0.4, -0.6)
        )
    
    def active(self):
        self.position = Vec2(0.3, -0.5)
    
    def pasive(self):
        self.position = Vec2(0.4, -0.6)

for z in range(20):
    for x in range(20):
        voxel = Voxel(
            position = (x, 0, z),
            texture = grass_texture
        )

Audio('assets/musica.mp3', loop = True, automplay = True)
player = FirstPersonController()
sky = Sky()
hand = Hand()
Text('Presiona Alt+F4 para salir', origin=(.5,0), position=(-.55,.4))

app.run()