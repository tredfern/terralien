#!/usr/bin/python

import pyglet
import random
from math import pi
from camera import Camera
from pyglet.gl import *
from pyglet.window import key

FONT_NAME = ('Verdana', 'Helvetica', 'Arial')
window = pyglet.window.Window()

class Tile:
  WATER=1
  GRASS=2
  FOREST=3
  HILL=4
  MOUNTAIN=5

  colors= {
      WATER: (0, 0, 128, 255),
      GRASS: (0, 200, 0, 255),
      FOREST: (0, 128, 0, 255),
      HILL: (120, 120, 0, 255),
      MOUNTAIN: (128, 128, 128, 255)
      }
  def __init__(self, x, y, width, height, terrain, batch):
    self.x = x * width
    self.y = y * height
    self.width = width
    self.height = height
    self.color = Tile.colors.get(terrain)
    self.add_to_batch(batch)

  def add_to_batch(self, batch):
    batch.add(4, GL_QUADS, None ,
        ('v2i', (self.x,self.y,self.x+self.width,self.y, self.x+self.width, self.y+self.width, self.x, self.y+self.width)),
        ('c4B', self.color * 4))


class WorldMap:
  def __init__(self):
    self.batch = pyglet.graphics.Batch()
    self.tiles = [[Tile(x, y, 6, 6, random.randrange(1, 6), self.batch) for x in range(100)] for y in range(100)]
    return

  def draw(self):
    self.batch.draw()

world = WorldMap()
camera = Camera((100,100), 100)

fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(FONT_NAME, 24))

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.focus(window.width, window.height)

    world.draw()
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
  return

def update(dt):
  camera.update()
  return

pyglet.clock.schedule_interval(update, 1/60.)
pyglet.app.run()
