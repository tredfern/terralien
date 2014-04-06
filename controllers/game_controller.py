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
        self.cursor = models.cursor.Cursor(position=(100, 100))
        start = self.map.randomTile()
        while start.terrain == models.map.terrains["water"]:
            start = self.map.randomTile()

        self.characters.append(models.actors.Actor(start._position) )
        self.buildings.append(models.stockpiles.Stockpile(start.x, start.y, 3, 3))
        self.assign_keys()

    def draw(self):
        pygsty.models.render_models()

    def update(self, dt):
        self.cursor.update()
        for c in self.characters:
            c.update(self.map)
        models.event_log.next_turn()



    def on_key_press(self, symbol, modifiers):
        if symbol in self._key_map:
            self._key_map[symbol]()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.A or symbol == key.D:
            self.cursor.stop_move_horz()

        if symbol == key.W or symbol == key.S:
            self.cursor.stop_move_vert()


    def assign_keys(self):
        self._key_map = {
            key.ESCAPE: pygsty.stop,
            key.A: self.cursor.move_left,
            key.W: self.cursor.move_up,
            key.S: self.cursor.move_down,
            key.D: self.cursor.move_right,
            key.B: self.build_stockpile,
            key.T: self.build_wall,
        }

    def build_stockpile(self):
        self.buildings.append(models.stockpiles.Stockpile(self.cursor.x, self.cursor.y, 3, 3))

    def build_wall(self):
        if pygsty.models.model_repository.is_vacant((self.cursor.x, self.cursor.y)):
            self.buildings.append(models.statics.Wall(position=(self.cursor.x, self.cursor.y), wall_type="wood"))

        n = pygsty.models.model_repository.get_neighbors(self.cursor.x, self.cursor.y)
        for w in n:
            if type(w) is models.statics.Wall:
                w.update_sprite()
