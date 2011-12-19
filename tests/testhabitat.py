import unittest
from pyglet import *
from habitat import *

class TestHabitat(unittest.TestCase):
  def setUp(self):
    self.habitat = Habitat(10, 20, 1000)

  def test_sets_up_a_circle_for_collision_and_space_tracking(self):
    self.assertEqual(self.habitat.boundary.c.x, 10)
    self.assertEqual(self.habitat.boundary.c.y, 20)
    self.assertEqual(self.habitat.boundary.r, 1000)

class TestMap(unittest.TestCase):
  def setUp(self):
    self.map = Map(10, 10000, 12000)

  def test_creating_a_map_generates_the_right_number_of_habitats(self):
    self.assertEqual(len(self.map.habitats), 10)

  def test_keeps_track_of_map_width_and_height(self):
    self.assertEqual(self.map.map_width, 10000)
    self.assertEqual(self.map.map_height, 12000)

  def test_habitats_are_valid_if_they_do_not_collide_with_another(self):
    a_map = Map(1, 10000, 10000)
    habitat = a_map.habitats[0]
    valid_habitat_x = habitat.boundary.c.x + habitat.boundary.r + 1000
    valid_habitat_y = habitat.boundary.c.y + habitat.boundary.r + 1000
    valid_habitat_size = 999
    self.assertTrue(a_map.is_habitat_valid(valid_habitat_x, valid_habitat_y, valid_habitat_size))

  def test_habitats_are_invalid_if_they_do_collide_with_another(self):
    habitat_five = self.map.habitats[5]
    collide_x = habitat_five.boundary.c.x + habitat_five.boundary.r / 2
    collide_y = habitat_five.boundary.c.y + habitat_five.boundary.r / 2
    radius = habitat_five.boundary.r / 2 -10
    self.assertFalse(self.map.is_habitat_valid(collide_x, collide_y, radius))
