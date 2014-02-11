import pyglet
from math import pi
from pyglet.gl import *
from pyglet.window import key
import pork
import pork.rack
import pork.controllers
import pork.camera

pork_globals = { 
    'rack' : None,
    'default_font' : 'Tahoma'
    } 

def start():
  pork_globals['rack'] = pork.rack.Rack()

def engine():
  return pork_globals['rack'];
  
def run():
  pyglet.clock.schedule_interval(pork_globals['rack'].update, 1/60.)
  pyglet.app.run()
