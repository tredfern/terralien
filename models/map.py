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
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.tiles[y][x]

    def getNeighbors(self, x, y):
        self.validateCoordinates(x,y)

        n = []
        for j in range(-1, 2):
            for h in range(-1, 2):
                if (j !=0 or h!=0):
                    t = self.getTile(x + j, y + h)
                    if t:
                        n += [t]

        return n

    def validateCoordinates(self, x,y):
        if x < 0 or x >= self.width or \
            y < 0 or y >= self.height:
            raise OutOfBoundsError("{} are not valid coordinates".format((x,y)))

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

    def __repr__(self):
        return "Tile( {} {} )".format(self._position, self.terrain.name)

class Terrain():
    def __init__(self, name="UNKNOWN", color=(255,0,255,255) ):
        self.name = name
        self.color = color

def grass():
    green = random.randint(165, 175)
    return Terrain(name="GRASS", color=(0, green, 0, 255))

class OutOfBoundsError(Exception):
    pass
