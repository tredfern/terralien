import pyglet
import pork

class Rack(pyglet.window.Window):
  def __init__(self):
    super(Rack, self).__init__(800, 600)
    self._controllers = []

  def push_controller(self, c):
    self._controllers.append(c)

  def pop_controller(self):
    return self._controllers.pop()

  def on_draw(self):
    print 'draw'
    for c in self._controllers:
      c.draw()
