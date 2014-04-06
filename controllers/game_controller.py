import pygsty
from pyglet.window import key
import models
import random
import data

class GameController(pygsty.controllers.BaseController):
    def __init__(self):
        self.cursor = models.cursor.Cursor(position=(100, 100))
        self.assign_keys()

    def draw(self):
        pygsty.models.render_models()

    def update(self, dt):
        for c in models.characters:
            c.update(models.get_map())
        models.event_log.next_turn()

    def on_key_press(self, symbol, modifiers):
        if symbol in self._key_map:
            self._key_map[symbol]()

    def assign_keys(self):
        self._key_map = {
            key.ESCAPE: pygsty.stop,
            key.A: self.cursor.move_left,
            key.W: self.cursor.move_up,
            key.S: self.cursor.move_down,
            key.D: self.cursor.move_right,
            key.B: self.build_stockpile,
            key.T: self.build_wall,
            key.M: self.move_main_guy
        }

    def build_stockpile(self):
        models.buildings.append(models.stockpiles.Stockpile(self.cursor.x, self.cursor.y, 3, 3))

    def build_wall(self):
        if pygsty.models.model_repository.is_vacant((self.cursor.x, self.cursor.y)):
            models.buildings.append(models.statics.Wall(position=(self.cursor.x, self.cursor.y), wall_type="wood"))

        n = pygsty.models.model_repository.get_neighbors(self.cursor.x, self.cursor.y)
        for w in n:
            if type(w) is models.statics.Wall:
                w.update_sprite()

    def move_main_guy(self):
        models.move_main_guy_to(self.cursor.x, self.cursor.y)
