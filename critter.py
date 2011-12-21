import pyglet
from pyglet.gl import *
from drawing import *

class CritterRenderGroup(pyglet.graphics.Group):
  def set_critter(self, critter):
    self.critter = critter
  def set_state(self):
    glPushMatrix()
    glTranslatef(self.critter.position.x, self.critter.position.y, 0)
    #glRotatef(self.critter.rotation, 0, 0, 1)

  def unset_state(self):
    glPopMatrix()

class Critter():
  def __init__(self):
    self.group = CritterRenderGroup()
    self.group.set_critter(self) 
    self.batch = pyglet.graphics.Batch()
    add_arrow(self.batch, 32, 32, (255, 255, 255, 255), self.group)

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

  def draw(self):
    self.batch.draw()

