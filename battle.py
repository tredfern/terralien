#!/usr/bin/python

import pyglet
import random
from primitives import *
from math import pi
from camera import Camera
from pyglet.gl import *
from pyglet.window import key
from euclid import *

team_colors= {
      1: (0, 128, 0, 255),
      2: (128, 0, 0, 255)
      }

class Unit:
  def __init__(self, x, y, team):
    self.location = Point2(x,y)
    self.team = team
    self.width = 16
    self.height = 16
    self.color = team_colors.get(team)
    self.attack_range = 32

  def add_to_batch(self, batch):
    batch.add(4, GL_QUADS, None ,
        ('v2i', (self.location.x,self.location.y,self.location.x+self.width,self.location.y, self.location.x+self.width, self.location.y+self.width, self.location.x, self.location.y+self.width)),
        ('c4B', self.color * 4))
    add_circle(batch, self.location.x, self.location.y, self.attack_range, (0, 0, 255, 255))
  def update(self, dt, battle):
    think(dt, battle)
    return

  def think(dt, battle):
    #look for an enemy
    enemies = battle.locate_enemies_in_range(self.location, self.attack_range)


class Battle:
  def __init__(self):
    self.batch = pyglet.graphics.Batch()
    self.units = []

  def add_unit(self, new_unit):
    new_unit.add_to_batch(self.batch)
    self.units.append(new_unit)

  def draw(self):
    self.batch.draw()

  def update(self, dt):
    for unit in self.units:
      unit.update(dt, self)

  def locate_enemies_in_range(self, location, radius):
    for target_unit in self.units:
      if target_unit.team != source_unit.team:
        if location.distance(target_unit) < radius:
          label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=10, y=10)
          label.draw()


FONT_NAME = ('Verdana', 'Helvetica', 'Arial')
window = pyglet.window.Window()
camera = Camera((100,100), 100)
fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(FONT_NAME, 24))
battle = Battle()
battle.add_unit(Unit(100, 100, 1))
battle.add_unit(Unit(150, 150, 2))

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.focus(window.width, window.height)

    battle.draw()
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
