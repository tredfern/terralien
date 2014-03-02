import pygsty.models

import pygsty.graphics
import pygsty.geometry
import models.map
from models.map import TILE_SIZE

class Actor(pygsty.models.VisibleModel):
    def __init__(self, position=(0, 0)):
        super().__init__(position=position)
        r = pygsty.geometry.Rect(1, 1, 3, 3)
        p = pygsty.graphics.rect_to_primitive(r, (255, 255, 255, 25) )
        p.add_to_batch(self.batch, self.render_group)

    @property
    def screen_x(self):
        return self.x * TILE_SIZE

    @property
    def screen_y(self):
        return self.y * TILE_SIZE
