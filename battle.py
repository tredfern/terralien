#!/usr/bin/python

import pyglet
import random
from math import pi
from camera import Camera
from pyglet.gl import *
from pyglet.window import key

team_colors= {
      1: (0, 128, 0, 255),
      2: (128, 0, 0, 255)
      }

class Unit:
  def __init__(self, x, y, team):
    self.x = x
    self.y = y
    self.team = team
    self.width = 16
    self.height = 16
    self.color = team_colors.get(team)

  def add_to_batch(self, batch):
    batch.add(4, GL_QUADS, None ,
        ('v2i', (self.x,self.y,self.x+self.width,self.y, self.x+self.width, self.y+self.width, self.x, self.y+self.width)),
        ('c4B', self.color * 4))


FONT_NAME = ('Verdana', 'Helvetica', 'Arial')
window = pyglet.window.Window()
camera = Camera((100,100), 100)
fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(FONT_NAME, 24))
a_batch = pyglet.graphics.Batch()
a_unit = Unit(100, 100, 1)
a_unit.add_to_batch(a_batch)
other_team = Unit(50, 50, 2)
other_team.add_to_batch(a_batch)

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.focus(window.width, window.height)

    a_batch.draw()
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
