import pyglet
from pyglet.gl import *
from pyglet.window import key
import pork
import pork.rack
import pork.controllers
import pork.camera

_window = None
pork_globals = { 
    'rack' : None,
    'default_font' : 'Tahoma'
    } 

def start():
  pork_globals['rack'] = pork.rack.Rack()
  global _window
  _window = pork_globals['rack']

def engine():
  return pork_globals['rack'];


#start()
#_window = engine().window

#camera = pork.camera.Camera((100,100), 100)
#fps_display = pyglet.clock.ClockDisplay(font=pyglet.font.load(pork_globals['default_font'], 24))

#@_window.event
#def on_draw():
#  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

# pork_globals['rack'].draw()
    
  # Handle the camera
  #camera.focus(window.width, window.height)

  # Draw top of the screen
#  camera.hud_mode(_window.width, _window.height)
#  fps_display.draw()
  
def run():
  pyglet.app.run()
