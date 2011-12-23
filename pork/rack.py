import pyglet
from pyglet.gl import *
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

  def on_draw(self):
    self.clear()

    self.camera.focus(self.width, self.height)
    for c in self._controllers:
      c.draw()

    self.camera.hud_mode(self.width, self.height)
    for c in self._controllers:
      c.draw_hud()
