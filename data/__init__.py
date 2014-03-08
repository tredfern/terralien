import pyglet
import pygsty

#
# Load Humanoid images
#

pygsty.logger.info("Loading Images")
_humanoid = pyglet.image.load("data/images/Characters/Humanoid0.png")
_humanoid2 = pyglet.image.load("data/images/Characters/Humanoid1.png")
_h_rows = int(_humanoid.height / 16)
_h_cols = int(_humanoid.width / 16)

pygsty.logger.info("Processing Images")
#Chop up into image grid
_humanoid_grid_1 = pyglet.image.ImageGrid(_humanoid, _h_rows, _h_cols)
_humanoid_grid_2 = pyglet.image.ImageGrid(_humanoid2, _h_rows, _h_cols)
