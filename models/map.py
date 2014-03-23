import random
import pygsty.models
import pygsty.graphics
import pygsty.euclid
import data
import pyglet

TILE_SIZE = 16

class TileMap():
    def __init__(self, width=0, height=0):
        self.tiles = []
        pygsty.models.set_repository_size(width, height)
        self._width = width
        self._height = height
        for y in range(height):
            row = []
            for x in range(width):
                t = Tile((x, y), terrains["unknown"])
                row.append(t)
            self.tiles.append(row)

    def build_batch(self):
        for r in self.tiles:
            for t in r:
                t.add_to_batch(pygsty.models.model_batch)

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
    def __init__(self, position, terrain = None, size=TILE_SIZE):
        self._position = position
        self._worldPosition = (position[0] * size, position[1] * size)
        self._terrain = terrain
        self._rect = pygsty.geometry.rect_from_coordinates( self._worldPosition[0],
                self._worldPosition[1],
                self._worldPosition[0] + size,
                self._worldPosition[1] + size )

    @property
    def x(self):
        return self._position[0]

    @property
    def y(self):
        return self._position[1]

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
        self._sprite = pyglet.sprite.Sprite(self.terrain.image, x=self._worldPosition[0], y=self._worldPosition[1], batch = batch, group = pygsty.graphics.background_group)

    def __repr__(self):
        return "Tile( {} {} )".format(self._position, self.terrain.name)

    def change_terrain(self, terrain):
        self._terrain = terrain

class Terrain():
    def __init__(self, name="UNKNOWN", passable=True, image=None ):
        self.name = name
        self.passable = passable
        self.image = image

terrains = {
    "unknown" : Terrain(),
    "grass" : Terrain(name="GRASS", image=data.get_floor_image(31,8)),
    "water" : Terrain(name="WATER",  passable=False, image=data.get_floor_image(16, 15)),
}

class OutOfBoundsError(Exception):
    pass
