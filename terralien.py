#!/usr/bin/python

import pyglet
import random
from math import pi
from camera import Camera
from pyglet.gl import *
from pyglet.window import key
from primitives import *
from scene import *


FONT_NAME = ('Tahoma')
window = pyglet.window.Window(800, 600)
camera = Camera((100,100), 100)
fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(FONT_NAME, 24))
map_width = 10000
map_height = 10000

class Habitat:
  def __init__(self, x, y, size):
    self.x = x
    self.y = y
    self.size = size
    self.batch = pyglet.graphics.Batch()
    add_circle(self.batch, self.x, self.y, size, (255,0,0, 255))

  def draw(self):
    self.batch.draw()
    

class Map:
  def __init__(self, habitats):
    self.habitats = []

    for x in range(habitats):
      self.generate_habitats()

  def generate_habitats(self):
    x = random.randrange(map_width)
    y = random.randrange(map_height)
    radius = 250 + random.randrange(250)
    habitat = Habitat(x, y, radius)
    self.habitats.append(habitat)
    
  def draw(self):
    for h in self.habitats:
      h.draw()
  
map_info = Map(50)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Handle the camera
    camera.focus(window.width, window.height)

    #Update the game
    map_info.draw()
   
    # Draw top of the screen
    camera.hud_mode(window.width, window.height)
    fps_display.draw()

@window.event
def on_key_press(symbol, modifiers):
  if symbol == key.LEFT:
    camera.pan(camera.scale, -pi/2)
  elif symbol == key.RIGHT:
    camera.pan(camera.scale, pi/2)
  elif symbol == key.DOWN:
    camera.pan(camera.scale, pi)
  elif symbol == key.UP:
    camera.pan(camera.scale, 0)
  elif symbol == key.PAGEUP:
    camera.zoom(2)
  elif symbol == key.PAGEDOWN:
    camera.zoom(0.5)
  return

def update(dt):
  camera.update()
  return

pyglet.clock.schedule_interval(update, 1/60.)
pyglet.app.run()
