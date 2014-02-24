import pygsty.controllers
from models.habitat import *
from models.critter import *

class GameController(pygsty.controllers.BaseController):
  def __init__(self):
    self.map_info  = Map(10, 50000, 50000)
    self.critters = []

    for r in range(300):
      self.create_critter()

  def create_critter(self):
    critter = Critter()
    critter.speed = 5 + random.randrange(10)
    critter.set_rotation(random.randrange(360))
    h = random.randrange(len(self.map_info.habitats))
    critter.occupy(self.map_info.habitats[h])
    self.critters.append(critter)

  def draw(self):
    self.map_info.draw()
    pygsty.models.render_models()

  def update(self, dt):
    for c in self.critters:
      c.update()

  
