import pygsty.models
import data
from models.map import TILE_SIZE
_cursor = None

def get_cursor():
    return _cursor

class Cursor(pygsty.models.BaseModel):
    def __init__(self, position):
        super().__init__(position=position)
        self.screen_offset_x = TILE_SIZE
        self.screen_offset_y = TILE_SIZE
        self.initSprite(data.cursors["default"], pygsty.graphics.hud_group)
        global _cursor
        _cursor = self
