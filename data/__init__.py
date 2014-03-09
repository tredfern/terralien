import pyglet
import pygsty

#
# Load Humanoid images
#

pygsty.logger.info("Loading Images")
_humanoid = pyglet.image.load("data/images/Characters/Humanoid0.png")
_humanoid2 = pyglet.image.load("data/images/Characters/Humanoid1.png")
_floor = pyglet.image.load("data/images/Map/Floor.png")
_trees = pyglet.image.load("data/images/Map/Tree0.png")
_h_rows = int(_humanoid.height / 16)
_h_cols = int(_humanoid.width / 16)
_f_rows = int(_floor.height / 16)
_f_cols = int(_floor.width / 16)
_t_cols = int(_trees.width / 16)
_t_rows = int(_trees.height / 16)

pygsty.logger.info("Processing Images")
#Chop up into image grid
_humanoid_grid1 = pyglet.image.ImageGrid(_humanoid, _h_rows, _h_cols)
_humanoid_grid2 = pyglet.image.ImageGrid(_humanoid2, _h_rows, _h_cols)
_floor_grid = pyglet.image.ImageGrid(_floor, _f_rows, _f_cols)
_tree_grid = pyglet.image.ImageGrid(_trees, _t_rows, _t_cols)

def get_floor_image(row, col):
    index = row * _f_cols + col
    return _floor_grid[index]

def get_tree_image(row, col):
    index = row * _t_cols + col
    return _tree_grid[index]
