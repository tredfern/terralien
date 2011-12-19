import pyglet
import random
from drawing import *

class Habitat:
  def __init__(self, x, y, size):
    self.x = x
    self.y = y
    self.size = size
    self.batch = pyglet.graphics.Batch()
    add_circle(self.batch, self.x, self.y, size, (255,0,0, 255))

  def draw(self):
    self.batch.draw()
    

class Map:
  def __init__(self, habitats, map_width, map_height):
    self.habitats = []
    self.map_width = map_width
    self.map_height = map_height

    for x in range(habitats):
      self.generate_habitats()

  def generate_habitats(self):
    x = random.randrange(self.map_width)
    y = random.randrange(self.map_height)
    radius = 2500 + random.randrange(2500)
    habitat = Habitat(x, y, radius)
    self.habitats.append(habitat)
    
  def draw(self):
    for h in self.habitats:
      h.draw()
