#!/usr/bin/python

import pyglet
import random
from math import pi
from camera import Camera
from pyglet.gl import *
from pyglet.window import key

FONT_NAME = ('Verdana', 'Helvetica', 'Arial')
window = pyglet.window.Window()

camera = Camera((100,100), 100)

fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(FONT_NAME, 24))

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    camera.focus(window.width, window.height)

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
