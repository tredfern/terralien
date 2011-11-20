import math

import pyglet
from pyglet.gl import *

class SmoothLineGroup(pyglet.graphics.Group):
    def set_state(self):
        glPushAttrib(GL_ENABLE_BIT)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable(GL_LINE_SMOOTH)
        glLineWidth(2)

    def unset_state(self):
        glPopAttrib()

    def __hash__(self):
        return hash(self.__class__.__name__)

    def __eq__(self, other):
        return self.__class__ is other.__class__

def add_circle(batch, x, y, radius, color, num_points=30, antialised=True):
    l = []
    angle1=0
    for n in range(num_points):
        angle2 = (math.pi * 2 * n+1) / num_points
        l.append(x + radius * math.cos(angle1))
        l.append(y + radius * math.sin(angle1))
        l.append(x + radius * math.cos(angle2))
        l.append(y + radius * math.sin(angle2))
        angle1 = angle2

    l.append(x + radius * math.cos(angle1))
    l.append(y + radius * math.sin(angle1))
    l.append(x + radius * math.cos(0))
    l.append(y + radius * math.sin(0))
    vertices_count = len(l)/2 
    if antialised:
        group = SmoothLineGroup()
    else:
        group = None
    return batch.add(vertices_count, GL_LINES, group, ('v2f', l),
        ('c4B', color*vertices_count))

def add_line(batch, x1, y1, x2, y2, color):
  l = (x1, y1, x2, y2)
  return batch.add(2, GL_LINES, None, ('v2f', l),
        ('c4B', color*2))
