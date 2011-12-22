import pyglet
import pork

class Rack():
  def __init__(self):
    self._controllers = []

  def start(self):
    self.window = pork.window.Window(self, 800, 600)

  def push_controller(self, c):
    self._controllers.append(c)

  def pop_controller(self):
    return self._controllers.pop()

  def draw(self):
    print 'draw'
    for c in self._controllers:
      c.draw()
