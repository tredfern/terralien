#!/usr/bin/python

import pyglet
import random
from primitives import *
from math import pi
from camera import Camera
from geometry import * 
from scene import * 
from pyglet.gl import *
from pyglet.window import key
from euclid import *

team_colors= {
      1: (0, 128, 0, 255),
      2: (128, 0, 0, 255)
      }

def angle_length_to_vector2(angle, length):
  return Vector2(math.cos(math.radians(angle)) * length, math.sin(math.radians(angle)) * length)

class UnitRenderGroup(pyglet.graphics.Group):
  def set_unit(self, unit):
    self.unit = unit
  def set_state(self):
    glPushMatrix()
    glTranslatef(self.unit.location.x, self.unit.location.y, 0)
    glRotatef(self.unit.rotation, 0, 0, 1)

  def unset_state(self):
    glPopMatrix()


class Unit:
  def __init__(self, x, y, team):
    self.location = Point2(x,y)
    self.team = team
    self.width = 16
    self.height = 16
    self.color = team_colors.get(team)
    self.attack_range = 128
    self.rotation = random.randrange(360)
    self.create_arrow_overlay()
    self.group = UnitRenderGroup()
    self.group.set_unit(self) 
    self.velocity = 300
    self.move_vector = angle_length_to_vector2(self.rotation, self.velocity)
    self.batch = pyglet.graphics.Batch()
    self.add_to_batch(self.batch)

  @property
  def bounding_rect(self):
    return Rect(self.location.x, self.location.y, self.width, self.height)

  def create_arrow_overlay(self):
    half_width = self.width /2
    half_height = self.height /2
    self.arrow_verts = (0, 0,
                 -half_width,+half_height, 
                 self.width, 0, 
                 -half_width, -half_height)
    self.arrow_indices = [0, 1, 2, 0, 2, 3]

  def add_to_batch(self, batch):
    batch.add_indexed(4, GL_TRIANGLES, self.group,
        self.arrow_indices,
        ('v2i', self.arrow_verts),
        ('c4B', self.color * 4))
    #add_circle(batch, self.location.x, self.location.y, self.attack_range, (255, 0, 255, 255))
  def update(self, dt, battle):
    #self.think(dt, battle)
    self.move(dt, battle)
    return

  def move(self, dt, battle):
    #update movement based on vector
    self.location += self.move_vector * dt
    self.rotation += random.randrange(-3, 3)
    self.move_vector = angle_length_to_vector2(self.rotation, self.velocity)


  def think(self, dt, battle):
    #look for an enemy
    enemies = battle.locate_enemies_in_range(self, self.attack_range)

  def draw(self):
    self.batch.draw()

class Battle:
  def __init__(self):
    self.batch = pyglet.graphics.Batch()
    self.units = []
    self._tree = QuadTree(Rect(-10000, -10000, 20000, 20000))

  def add_unit(self, new_unit):
    new_unit.add_to_batch(self.batch)
    self.units.append(new_unit)

  def draw(self, ):
    for unit in self._tree.get_things(camera.bounding_rect):
      unit.draw()

  def update(self, dt):
    self._tree = QuadTree(Rect(-10000, -10000, 20000, 20000))
    for unit in self.units:
      unit.update(dt, self)
      self._tree.add_thing(unit, unit.bounding_rect)

  def locate_enemies_in_range(self, source_unit, radius):
    e = []
    for target_unit in self.units:
      if target_unit.team != source_unit.team:
        if source_unit.location.distance(target_unit.location) < radius:
          e.append(target_unit)
    return e

FONT_NAME = ('Verdana', 'Helvetica', 'Arial')
window = pyglet.window.Window(800, 600)
camera = Camera((100,100), 2)
fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(FONT_NAME, 24))
battle = Battle()
for n in range(200):
  battle.add_unit(Unit(random.randrange(1000), random.randrange(1000), 1))

for n in range(200):
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
