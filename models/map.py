import pygsty.graphics

class TileMap():
    def __init__(self):
        self.tiles = []

    def generate(self, w, h):
        self._width = w
        self._height = h
        for y in range(h):
            row = []
            for x in range(w):
                row.append(Tile((x, y), GRASS))
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
        self._terrain = terrain
        self._rect = pygsty.graphics.Rectangle((position), (position[0] + TILE_SIZE, position[1] + TILE_SIZE))

    @property
    def terrain(self):
        return self._terrain

    @property
    def rect(self):
        return self._rect;

class Terrain():
    pass

def grass():
    t = Terrain()
    t.color = (0, 200, 0, 255)

TILE_SIZE = 5
GRASS = grass()

