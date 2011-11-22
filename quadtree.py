from geometry import * 

quad_tree_consts = {
    "max_level" : 7,
    "max_objects" : 10
}

class QuadTree():
  def __init__(self, bounding_rect, level=0):
    self.bounding_rect = bounding_rect
    self.level = 0
    self.things = []


  def add_thing(self, thing, bounding_rect):
    self.things.append((thing, bounding_rect))

  def get_things(self, bounding_rect):
    return [t[0] for t in self.things]



