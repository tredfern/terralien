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
        self.buildings = []

        start = self.map.randomTile()
        while start.terrain == models.map.terrains["water"]:
            start = self.map.randomTile()

        self.characters.append(models.actors.Actor(start._position) )
        self.buildings.append(models.stockpiles.Stockpile(start.x, start.y, 3, 3))


    def draw(self):
        pygsty.models.render_models()


    def update(self, dt):
        for c in self.characters:
            c.update(self.map)
        models.event_log.next_turn()



    def on_key_press(self, symbol, modifiers):
        if symbol == key.ESCAPE:
            pygsty.stop()
