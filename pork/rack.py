import pyglet
from pyglet.window import key

class Rack():
  def __init__(self):
    self._controllers = []

  def start(self):
    self.window = pyglet.window.Window(800, 600)

  def push_controller(self, c):
    self._controllers.append(c)

  def pop_controller(self):
    return self._controllers.pop()
