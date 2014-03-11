import pygsty
from pyglet.window import key
import models
import random
import data

class GameController(pygsty.controllers.BaseController):
    def __init__(self):
        self.map = data.generators.map.make_map(200, 200)
        self.map.build_batch()
        self.characters = []
        for i in range(0,100):
            self.characters.append(models.actors.Actor(position=(100, 100) ) )

        

    def draw(self):
        pygsty.models.render_models()
        models.statics.static_batch.draw()


    def update(self, dt):
        for c in self.characters:
            c.update(self.map)
        models.event_log.next_turn()



    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pygsty.stop()
