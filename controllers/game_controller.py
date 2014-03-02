import pygsty
from pyglet.window import key
import models
import random

class GameController(pygsty.controllers.BaseController):
    def __init__(self):
        self.map = models.map.TileMap()
        self.map.generate(200, 200)
        self.characters = []
        for i in range(0,400):
            self.characters.append(models.actors.Actor(position=(100, 100) ) )

    def draw(self):
        pygsty.models.render_models()

    def update(self, dt):
        for c in self.characters:
            c.update()
            x, y = c.position
            x += random.randint(-1, 1)
            y += random.randint(-1, 1)
            c.moveTo(x, y)


    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pygsty.stop()
