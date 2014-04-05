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
        self.move_x = 0
        self.move_y = 0
        global _cursor
        _cursor = self

    def update(self):
        self.moveTo(self.x + self.move_x, self.y + self.move_y)

    def move_up(self):
        self.move_y = 1

    def move_down(self):
        self.move_y = -1

    def move_right(self):
        self.move_x = 1

    def move_left(self):
        self.move_x = -1

    def stop_move_horz(self):
        self.move_x = 0

    def stop_move_vert(self):
        self.move_y = 0
