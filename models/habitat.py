import pyglet
import random
import pygsty
from pygsty.euclid import *
from pygsty.drawing import *

class Habitat:
  def __init__(self, x, y, size):
    self.boundary = Circle(Point2(x,y) ,float(size))
    self.batch = pyglet.graphics.Batch()
    add_circle(self.batch, self.boundary.c.x, self.boundary.c.y, size, (255,0,0, 255))
    self.habitat_links = []
    self.critters = []

  def draw(self):
    self.batch.draw()
    for c in self.critters:
      c.draw()

  def link_to(self, h):
    if self.is_linked_to(h) or h == self:
      return

    self.habitat_links.append(h)
    h.link_to(self)
    c = self.boundary.connect(h.boundary)
    add_line(self.batch, c.p1.x, c.p1.y, c.p2.x, c.p2.y, (0,255,0,255))

  def is_linked_to(self, h):
    return self.habitat_links.count(h) > 0

  def add_critter(self, c):
    self.critters.append(c)

  def contains_critter(self, c):
    return self.critters.count(c) > 0

  def can_move_to(self, pt):
    return self.boundary.contains_point(pt)
  

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
    if self.is_habitat_valid(x, y, radius):
      habitat = Habitat(x, y, radius)
      self.habitats.append(habitat)

    #link some habitats
    for h in self.habitats:
      for i in range(2):
        r = random.randrange(len(self.habitats))
        h.link_to(self.habitats[r])
    
  def draw(self):
    for h in self.habitats:
      h.draw()

  def is_habitat_valid(self, x, y, size):
    c = Circle(Point2(x, y), float(size))
    for h in self.habitats:
      if h.boundary.overlap(c):
        return False
      
    return True
    
