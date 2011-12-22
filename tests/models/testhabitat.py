import unittest
from pyglet import *
from habitat import *

class TestHabitat(unittest.TestCase):
  def test_sets_up_a_circle_for_collision_and_space_tracking(self):
    habitat = Habitat(10, 20, 1000)
    self.assertEqual(habitat.boundary.c.x, 10)
    self.assertEqual(habitat.boundary.c.y, 20)
    self.assertEqual(habitat.boundary.r, 1000)

  def test_habitats_can_link_to_other_habitats(self):
    habitat_1 = Habitat(10, 20, 1000)
    habitat_2 = Habitat(1210, 3200, 400)
    habitat_1.link_to(habitat_2)
    self.assertTrue(habitat_1.is_linked_to(habitat_2))
    self.assertTrue(habitat_2.is_linked_to(habitat_1))
    self.assertEqual(len(habitat_1.habitat_links), 1)
    self.assertEqual(len(habitat_2.habitat_links), 1)

  def test_habitats_dont_add_multiple_links(self):
    habitat_1 = Habitat(10, 20, 1000)
    habitat_2 = Habitat(1210, 3200, 400)
    habitat_1.link_to(habitat_2)
    habitat_1.link_to(habitat_2)
    habitat_2.link_to(habitat_1)
    self.assertEqual(len(habitat_1.habitat_links), 1)
    self.assertEqual(len(habitat_2.habitat_links), 1)
  
  def test_habitats_dont_link_to_themselves(self):
    habitat = Habitat(10, 20, 1000)
    habitat.link_to(habitat)
    self.assertFalse(habitat.is_linked_to(habitat))
    self.assertEqual(len(habitat.habitat_links), 0)

  def test_checking_boundary_for_valid_locations(self):
    habitat = Habitat(0, 0, 1)
    self.assertTrue(habitat.can_move_to(Point2(0.2, 0.2)))
    self.assertTrue(habitat.can_move_to(Point2(-0.2, -0.2)))
    self.assertFalse(habitat.can_move_to(Point2(1, 1)))

class TestMap(unittest.TestCase):
  def setUp(self):
    self.map = Map(10, 10000, 12000)

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
    a_map = Map(1, 10000, 10000)
    habitat = a_map.habitats[0]
    collide_x = habitat.boundary.c.x + habitat.boundary.r / 2
    collide_y = habitat.boundary.c.y + habitat.boundary.r / 2
    radius = habitat.boundary.r
    self.assertFalse(self.map.is_habitat_valid(collide_x, collide_y, radius))

class TestMapGeneration(unittest.TestCase):
  pass
