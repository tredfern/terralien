import pyglet
from pyglet.gl import *
from pygsty.drawing import *
from pygsty.euclidextensions import *
import random 

class CritterRenderGroup(pyglet.graphics.Group):
  def set_critter(self, critter):
    self.critter = critter
  def set_state(self):
    glPushMatrix()
    glTranslatef(self.critter.position.x, self.critter.position.y, 0)
    glRotatef(self.critter.rotation, 0, 0, 1)

  def unset_state(self):
    glPopMatrix()

class Critter():
  def __init__(self):
    self.group = CritterRenderGroup()
    self.group.set_critter(self) 
    self.batch = pyglet.graphics.Batch()
    add_arrow(self.batch, 32, 32, (255, 255, 255, 255), self.group)
    self._rotation = 0
    self.speed = 0

  @property
  def rotation(self):
    return self._rotation

  @property
  def habitat(self):
    return self.h

  @property
  def position(self):
    return self.p

  def occupy(self, h):
    self.h = h
    h.add_critter(self)
    self.set_position(h.boundary.c)

  def set_position(self, pt):
    if self.h.can_move_to(pt):
      self.p = pt
      return True
    
    return False
  
  def set_rotation(self, rot):
    while rot > 360:
      rot -= 360
    while rot < 0:
      rot += 360
    self._rotation = rot

  def draw(self):
    self.batch.draw()

  def move(self):
    mv = angle_length_to_vector2(self.rotation, self.speed)

    if not self.set_position(self.position + mv):
      self.set_rotation(self._rotation - 180)

    self.set_rotation(self._rotation + random.randrange(-3, 4))

  def update(self):
    self.move()

