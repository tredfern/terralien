class TileMap():
    def __init__(self):
        self.tiles = []

    def generate(self, w, h):
        self._width = w
        self._height = h
        for x in range(w * h):
            self.tiles.append(Tile())

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height


class Tile():
    pass
