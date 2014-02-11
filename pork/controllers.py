import pork
import pyglet

class BaseController():
  def draw(self):
    pass

  def draw_hud(self):
    pass

  def update(self, dt):
    pass

class PerformanceController(BaseController):
  def __init__(self):
    self.fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load("Arial", 24))

  def draw_hud(self):
    self.fps_display.draw()
    
