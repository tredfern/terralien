import random

import pygsty.models
import pygsty.graphics
import pygsty.geometry

import models.map
from models.map import TILE_SIZE


class Actor(pygsty.models.VisibleModel):
    def __init__(self, position=(0, 0)):
        super().__init__(position=position)
        self._goal = None
        self._setupGraphics()

    @property
    def screen_x(self):
        return self.x * TILE_SIZE

    @property
    def screen_y(self):
        return self.y * TILE_SIZE

    @property
    def goal(self):
        return self._goal

    def update(self):
        if (self.goal == None):
            self._goal = (random.randint(0, 200), random.randint(0, 200) )

        x, y = self.position
        x += random.randint(-1, 1)
        y += random.randint(-1, 1)
        self.moveTo(x, y)

    def _setupGraphics(self):
        r = pygsty.geometry.Rect(1, 1, 3, 3)
        p = pygsty.graphics.rect_to_primitive(r, (255, 255, 255, 25) )
        p.add_to_batch(self.batch, self.render_group)
