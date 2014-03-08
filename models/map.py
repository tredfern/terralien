import random
import pygsty.models
import pygsty.graphics
import pygsty.euclid
import data
import pyglet

TILE_SIZE = 16

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

    def add_lakes(self, number = 3):
        for l in range(number):
            cx = random.randint(0, 200)
            cy = random.randint(0, 200)
            nt = self.getTile(cx, cy)
            nt._terrain = water()
            size = 150
            for i in range(size):
                nt = None
                while not nt:
                    nx = random.randint(-2, 2)
                    ny = random.randint(-2, 2)
                    nt = self.getTile(cx + nx, cy + ny)
                nt._terrain = water()
                nb = self.getNeighbors(cx, cy)
                for ne in nb:
                    ne._terrain = water()
                cx = nt.point.x
                cy = nt.point.y


    def build_batch(self):
        for r in self.tiles:
            for t in r:
                t.add_to_batch(pygsty.models.default_batch)

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def array_width(self):
        return self.width - 1

    @property
    def array_height(self):
        return self.height - 1

    def getTile(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self.tiles[y][x]

    def randomTile(self):
        return self.getTile(random.randint(0, self.array_width), random.randint(0, self.array_height))

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
        self._worldPosition = (position[0] * size, position[1] * size)
        self._terrain = terrain
        self._rect = pygsty.geometry.rect_from_coordinates( self._worldPosition[0],
                self._worldPosition[1],
                self._worldPosition[0] + size,
                self._worldPosition[1] + size )

    @property
    def point(self):
        return pygsty.euclid.Point2(self._position[0], self._position[1])

    @property
    def terrain(self):
        return self._terrain

    @property
    def rect(self):
        return self._rect;

    def add_to_batch(self, batch):
        self._sprite = pyglet.sprite.Sprite(self.terrain.image, x=self._worldPosition[0], y=self._worldPosition[1], batch = batch, group = data.ordered_groups[0])

    def __repr__(self):
        return "Tile( {} {} )".format(self._position, self.terrain.name)

class Terrain():
    def __init__(self, name="UNKNOWN", color=(255,0,255,255), passable=True, image=None ):
        self.name = name
        self.color = color
        self.passable = passable
        self.image = image

def grass():
    green = random.randint(165, 175)
    return Terrain(name="GRASS", color=(0, green, 0, 255), image=data.get_floor_image(31,8))

def water():
    blue = random.randint(130, 155)
    return Terrain(name="WATER", color=(0,0, blue, 255), passable=False, image=data.get_floor_image(16, 15))

class OutOfBoundsError(Exception):
    pass
