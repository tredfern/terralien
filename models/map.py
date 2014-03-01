import random
import pygsty.models
import pygsty.graphics

TILE_SIZE = 5

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
    def __init__(self, position, terrain, size=TILE_SIZE):
        self._position = position
        self._world_position = (position[0] * size, position[1] * size)
        self._terrain = terrain
        self._rect = pygsty.geometry.rect_from_coordinates( self._world_position[0],
                self._world_position[1],
                self._world_position[0] + size,
                self._world_position[1] + size )
        self.add_to_batch(pygsty.models.default_batch)

    @property
    def terrain(self):
        return self._terrain

    @property
    def rect(self):
        return self._rect;

    def add_to_batch(self, batch):
        p = pygsty.graphics.rect_to_primitive(self.rect, self.terrain.color)
        p.add_to_batch(batch)

class Terrain():
    pass

def grass():
    t = Terrain()
    green = random.randint(165, 175)
    t.color = (0, green, 0, 255)
    return t
