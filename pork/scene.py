from pork.geometry import * 

quad_tree_consts = {
    "max_level" : 10,
    "max_objects" : 10
}

class QuadTree():
  def __init__(self, bounding_rect, level=0):
    self.bounding_rect = bounding_rect
    self.level = 0
    self.things = []
    self.children = []


  def add_thing(self, thing, bounding_rect):
    if len(self.things) > quad_tree_consts["max_objects"] and self.level < quad_tree_consts["max_level"]:
        self.divide_node()

    if self.has_children:
      self.add_to_children(thing, bounding_rect)
    else:
      self.things.append((thing, bounding_rect))

  def add_to_children(self, thing, bounding_rect):
    c = self.children_in_rect(bounding_rect)
    if len(c):
      c[0].add_thing(thing, bounding_rect)

  def get_things(self, bounding_rect):
    if self.has_children:
      return [t for c in self.children if c.bounding_rect.intersects(bounding_rect) for t in c.get_things(bounding_rect)]
    else:
      return [t[0] for t in self.things]

  def children_in_rect(self, bounding_rect):
    return [c for c in self.children if c.bounding_rect.intersects(bounding_rect)]

  @property
  def has_children(self):
    return len(self.children) > 0

  def divide_node(self):
    if self.has_children:
      return

    middle_point = self.bounding_rect.center
    next_level = self.level + 1
    #TOP LEFT
    self.children.append(QuadTree(
        rect_from_coordinates(
          self.bounding_rect.left, 
          middle_point.x,
          middle_point.y, 
          self.bounding_rect.top), 
        next_level))
    #TOP RIGHT
    self.children.append(QuadTree(
        rect_from_coordinates(
          middle_point.x,
          self.bounding_rect.right,
          middle_point.y, 
          self.bounding_rect.top), 
        next_level))
    #BOTTOM LEFT
    self.children.append(QuadTree(
        rect_from_coordinates(
          self.bounding_rect.left, 
          middle_point.x,
          self.bounding_rect.bottom,
          middle_point.y), 
        next_level))
    #BOTTOM RIGHT
    self.children.append(QuadTree(
        rect_from_coordinates(
          middle_point.x,
          self.bounding_rect.right,
          self.bounding_rect.bottom,
          middle_point.y), 
        next_level))

    for t in self.things:
      self.add_to_children(t[0], t[1])
