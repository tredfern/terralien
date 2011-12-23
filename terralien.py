#!/usr/bin/python

import pyglet
import random
from math import pi
from pyglet.gl import *
from pyglet.window import key
import controllers
import models
from models.habitat import *
from models.critter import *
import views

import pork
from pork.camera import Camera
from pork.drawing import *
from pork.scene import *

### OK Code
map_width = 50000
map_height = 50000
habitats = 10


map_info = Map(10, map_width, map_height)
critters = []

def create_critter():
  critter = Critter()
  critter.speed = 5 + random.randrange(10)
  critter.set_rotation(random.randrange(360))
  h = random.randrange(len(map_info.habitats))
  critter.occupy(map_info.habitats[h])
  critters.append(critter)
  
for r in range(100):
  create_critter()

pork.start()
pork.engine().push_controller(pork.controllers.PerformanceController())
#--

#@window.event
#def on_draw():
#    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#    
#    # Handle the camera
#    camera.focus(window.width, window.height)
#
    #Update the game
#    map_info.draw()
   
    # Draw top of the screen
#    camera.hud_mode(window.width, window.height)
#    fps_display.draw()

#@window.event
#def on_key_press(symbol, modifiers):
#  if symbol == key.LEFT:
#    camera.pan(camera.scale, -pi/2)
#  elif symbol == key.RIGHT:
#    camera.pan(camera.scale, pi/2)
#  elif symbol == key.DOWN:
#    camera.pan(camera.scale, pi)
#  elif symbol == key.UP:
#    camera.pan(camera.scale, 0)
#  elif symbol == key.PAGEUP:
#    camera.zoom(2)
#  elif symbol == key.PAGEDOWN:
#    camera.zoom(0.5)
#  return

#def update(dt):
#  for c in critters:
#    c.update()
#  camera.update()
#  return

#pyglet.clock.schedule_interval(update, 1/60.)
pork.run()
