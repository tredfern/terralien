import pygsty
import data
from models.map import TILE_SIZE

class Stockpile():
    def __init__(self, x, y, width, height):
        self._resources = []
        self.tiles = []
        for tx in range(x, x+width):
            for ty in range(y, y+height):
                self.tiles.append(StockpileTile(position=(tx, ty)))

    def add(self, resource):
        self._resources.append(resource)
        pygsty.logger.debug("{} added to stockpile.".format(resource))

    def __contains__(self, resource):
        return resource in self._resources

class StockpileTile(pygsty.models.BaseModel):
    def __init__(self, position):
        super().__init__(position)
        self.screen_offset_x = TILE_SIZE
        self.screen_offset_y = TILE_SIZE

        self.initSprite(data.tiles["stockpile"], pygsty.graphics.middleground_group)
