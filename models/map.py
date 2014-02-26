import random
import pygsty.models
import pygsty.graphics

class TileMap():
    def __init__(self):
        super().__init__()
        self.tiles = []

    def generate(self, w, h):
        self._width = w
        self._height = h
        for y in range(h):
            row = []
            for x in range(w):
                t = Tile((x, y), grass())
                row.append(t)
            self.tiles.append(row)


    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def getTile(self, x, y):
        return self.tiles[y][x]




class Tile():
    def __init__(self, position, terrain):
        self._position = position
        self._world_position = (position[0] * TILE_SIZE, position[1] * TILE_SIZE)
        self._terrain = terrain
        self._rect = pygsty.graphics.Rectangle( self._world_position, 
                (self._world_position[0] + TILE_SIZE, self._world_position[1] + TILE_SIZE) )
        self.add_to_batch(pygsty.models.default_batch)

    @property
    def terrain(self):
        return self._terrain

    @property
    def rect(self):
        return self._rect;

    def add_to_batch(self, batch):
        p = self.rect.to_primitive(self.terrain.color)
        p.add_to_batch(batch)

class Terrain():
    pass

def grass():
    t = Terrain()
    green = random.randint(120, 200)
    t.color = (0, green, 0, 255)
    return t

TILE_SIZE = 5
