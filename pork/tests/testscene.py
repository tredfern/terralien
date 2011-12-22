import unittest
from scene import *

class TestQuadTree(unittest.TestCase):
  def setUp(self):
    self.qt = QuadTree(Rect(0, 0, 200, 200))

  def test_add_a_thing_stores_in_list(self):
    self.qt.add_thing("thing", Rect(1, 1, 2, 2))
    self.assertEqual(len(self.qt.things), 1)


  def test_add_a_thing_keeps_track_of_thing(self):
    self.qt.add_thing("thing", Rect(1, 1, 2, 2))
    self.assertEqual(self.qt.things[0][0], "thing")

  def test_add_a_thing_keeps_track_of_rect(self):
    r = Rect(1, 1, 2, 2)
    self.qt.add_thing("thing", r)
    self.assertEqual(self.qt.things[0][1], r)

  def test_divide_node_creates_four_children(self):
    self.qt.divide_node()
    self.assertEqual(len(self.qt.children),4)
