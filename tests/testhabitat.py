import unittest
from pyglet import *
from habitat import *

class TestHabitat(unittest.TestCase):
  def setUp(self):
    self.habitat = Habitat(10, 20, 1000)

  def test_stores_coordinates_and_size(self):
    self.assertEqual(self.habitat.x, 10)
    self.assertEqual(self.habitat.y, 20)
    self.assertEqual(self.habitat.size, 1000)
  


class TestMap(unittest.TestCase):
  def setUp(self):
    self.map = Map(10, 10000, 12000)

  def test_creating_a_map_generates_the_right_number_of_habitats(self):
    self.assertEqual(len(self.map.habitats), 10)

  def test_keeps_track_of_map_width_and_height(self):
    self.assertEqual(self.map.map_width, 10000)
    self.assertEqual(self.map.map_height, 12000)


