from euclid import *

def rect_from_coordinates(left, right, bottom, top):
  return Rect(left, bottom, right-left, top-bottom)

class Rect():
  def __init__(self, x, y, width, height):
    self.x = x
    self.y = y
    self.width = width
    self.height = height

  @property
  def left(self):
    return self.x

  @property
  def bottom(self):
    return self.y
  
  @property
  def right(self):
    return self.x + self.width

  @property
  def top(self):
    return self.y + self.height

  def intersects(self, other):
    return not (self.x > other.right or
      self.right < other.left or
      self.y > other.top or
      self.top < other.y)

  def inspect(self):
    return "Rect({}, {}, {}, {})".format(self.x, self.y, self.width, self.height)
