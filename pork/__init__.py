import pyglet
from pyglet.gl import *
from pyglet.window import key
import pork
import pork.rack

pork_globals = { 
    'rack' : None 
    } 

def start():
  pork_globals[rack] = pork.rack.Rack()
  pork_globals[rack].start()

def engine():
  return pork_globals[rack];

