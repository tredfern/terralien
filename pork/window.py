import pyglet

class Window(pyglet.window.Window):
  def __init__(self, rack, width, height):
    super(Window, self).__init__(width, height)
    self.rack = rack
