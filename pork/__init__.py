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
  
def run():
  pyglet.app.run()
