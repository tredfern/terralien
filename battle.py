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
    self.attack_range = 128

  def add_to_batch(self, batch):
    half_width = self.width /2
    half_height = self.height /2
    batch.add_indexed(4, GL_TRIANGLES, None,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (self.location.x,self.location.y,
                 self.location.x-half_width,self.location.y-half_height, 
                 self.location.x, self.location.y+half_height, 
                 self.location.x+half_width, self.location.y-half_height)),
        ('c4B', self.color * 4))
    add_circle(batch, self.location.x, self.location.y, self.attack_range, (255, 0, 255, 255))
  def update(self, dt, battle):
    self.think(dt, battle)
    return

  def think(self, dt, battle):
    #look for an enemy
    enemies = battle.locate_enemies_in_range(self, self.attack_range)
    for e in enemies:
      add_line(battle.batch, self.location.x, self.location.y, e.location.x, e.location.y, (128, 128, 128, 255))

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

  def locate_enemies_in_range(self, source_unit, radius):
    e = []
    for target_unit in self.units:
      if target_unit.team != source_unit.team:
        if source_unit.location.distance(target_unit.location) < radius:
          e.append(target_unit)
    return e

FONT_NAME = ('Verdana', 'Helvetica', 'Arial')
window = pyglet.window.Window()
camera = Camera((100,100), 100)
fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(FONT_NAME, 24))
battle = Battle()
for n in range(20):
  battle.add_unit(Unit(random.randrange(1000), random.randrange(1000), 1))

for n in range(20):
  battle.add_unit(Unit(random.randrange(1000), random.randrange(1000), 2))

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
  battle.update(dt)
  return

pyglet.clock.schedule_interval(update, 1/60.)
pyglet.app.run()
