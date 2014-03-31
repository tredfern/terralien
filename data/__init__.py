import pyglet
import pygsty
import random
import data.generators

#
# Load Humanoid images
#

pygsty.logger.info("Loading Images")
_humanoid = pyglet.image.load("data/images/Characters/Humanoid0.png")
_humanoid2 = pyglet.image.load("data/images/Characters/Humanoid1.png")
_floor = pyglet.image.load("data/images/Map/Floor.png")
_trees = pyglet.image.load("data/images/Map/Tree0.png")
_trees2 = pyglet.image.load("data/images/Map/Tree1.png")
_tiles = pyglet.image.load("data/images/Map/Tile.png")
_cursors = pyglet.image.load("data/images/gui/cursors.png")

_h_rows = int(_humanoid.height / 16)
_h_cols = int(_humanoid.width / 16)
_f_rows = int(_floor.height / 16)
_f_cols = int(_floor.width / 16)
_t_cols = int(_trees.width / 16)
_t_rows = int(_trees.height / 16)
_tile_cols = int(_tiles.width / 16)
_tile_rows = int(_tiles.height / 16)

pygsty.logger.info("Processing Images")
#Chop up into image grid
_humanoid_grid1 = pyglet.image.ImageGrid(_humanoid, _h_rows, _h_cols)
_humanoid_grid2 = pyglet.image.ImageGrid(_humanoid2, _h_rows, _h_cols)
_floor_grid = pyglet.image.ImageGrid(_floor, _f_rows, _f_cols)
_tree_grid = pyglet.image.ImageGrid(_trees, _t_rows, _t_cols)
_tree_grid2 = pyglet.image.ImageGrid(_trees2, _t_rows, _t_cols)
_tile_grid = pyglet.image.ImageGrid(_tiles, _tile_rows, _tile_cols)


def get_floor_image(row, col):
    index = row * _f_cols + col
    return _floor_grid[index]

def get_tree_image(row, col):
    index = row * _t_cols + col
    return _tree_grid[index]

def get_tiles_image(row, col):
    index = row * _tile_cols + col
    return _tile_grid[index]

cursors = {
    "default": _cursors
}

tiles = {
    "stockpile": get_tiles_image(3,0)
}

terrain = {
    "grass": get_floor_image(31, 8),
    "water": get_floor_image(15, 16),
    "dirt": get_floor_image(19, 1)
}

trees = {
    "leaf": get_tree_image(26, 3),
    "burnt_leaf": get_tree_image(26, 7),
    "dark_leaf": get_tree_image(23, 3),
    "burnt_dark": get_tree_image(23, 7),
    "snow_leaf": get_tree_image(20, 3),
    "burnt_snow": get_tree_image(20, 7),
    "blue_leaf": get_tree_image(17, 3),
    "blue_snow": get_tree_image(17, 7),
    "conifer": get_tree_image(14, 3),
    "conifer_burnt": get_tree_image(14, 7),
    "dark_conifer": get_tree_image(11, 3),
    "dark_conifer_burnt": get_tree_image(11, 7),
    "conifer_snow": get_tree_image(8, 3),
    "conifer_snow_burnt": get_tree_image(8,7),
    "conifer_blue": get_tree_image(5,3),
    "conifer_blue_burnt": get_tree_image(5, 7),
    "cactus": get_tree_image(2, 3),
    "palm": get_tree_image(5,3)
}
