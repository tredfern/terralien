import pygsty
from pyglet.window import key
import models
import random

class GameController(pygsty.controllers.BaseController):
    def __init__(self):
        self.map = models.map.TileMap()
        self.map.generate(200, 200)
        self.map.add_lakes()
        self.map.build_batch()
        self.characters = []
        for i in range(0,100):
            self.characters.append(models.actors.Actor(position=(100, 100) ) )

        self.static_entities = []
        for i in range(0, 3000):
            self.static_entities.append(
                models.statics.Tree(self.map.randomTile())
            )

    def draw(self):
        pygsty.models.render_models()
        models.statics.static_batch.draw()


    def update(self, dt):
        for c in self.characters:
            c.update(self.map)



    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pygsty.stop()
