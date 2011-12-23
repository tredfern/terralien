import pyglet
from math import pi
from pyglet.gl import *
from pyglet.window import key
import pork

class Rack(pyglet.window.Window):
  def __init__(self):
    super(Rack, self).__init__(800, 600)
    self._controllers = []
    self.camera = pork.camera.Camera((100, 100), 100)

  def push_controller(self, c):
    self._controllers.append(c)

  def pop_controller(self):
    return self._controllers.pop()

  def update(self, dt):
    self.camera.update()
    for c in self._controllers:
      c.update(dt)
    

  def on_draw(self):
    self.clear()

    self.camera.focus(self.width, self.height)
    for c in self._controllers:
      c.draw()

    self.camera.hud_mode(self.width, self.height)
    for c in self._controllers:
      c.draw_hud()

  def on_key_press(self, symbol, modifiers):
    if symbol == key.LEFT:
      self.camera.pan(self.camera.scale, -pi/2)
    elif symbol == key.RIGHT:
      self.camera.pan(self.camera.scale, pi/2)
    elif symbol == key.DOWN:
      self.camera.pan(self.camera.scale, pi)
    elif symbol == key.UP:
      self.camera.pan(self.camera.scale, 0)
    elif symbol == key.PAGEUP:
      self.camera.zoom(2)
    elif symbol == key.PAGEDOWN:
      self.camera.zoom(0.5)
    return
