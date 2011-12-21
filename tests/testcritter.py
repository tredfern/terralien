from critter import *
from habitat import *
import unittest

class TestCritter(unittest.TestCase):
  def test_critters_occupy_a_habitat(self):
    critter = Critter()
    habitat = Habitat(0,0, 100)
    critter.occupy(habitat)
    self.assertTrue(habitat.contains_critter(critter))
    self.assertEqual(critter.habitat, habitat)
    #sets position to center of habitat
    self.assertEqual(critter.position, habitat.boundary.c)

  def test_critters_are_initialized_with_reasonable_defaults(self):
    critter = Critter()
    self.assertEqual(critter.rotation, 0)

  def test_critters_can_have_their_direction_set(self):
    critter = Critter()
    critter.set_rotation(250)
    self.assertEqual(critter.rotation, 250)
  
  def test_critters_set_with_rotation_greater_or_less_than_360_figure_it_out(self):
    critter = Critter()
    critter.set_rotation(370)
    self.assertEqual(critter.rotation, 10)
    critter.set_rotation(-50)
    self.assertEqual(critter.rotation, 310)
    critter.set_rotation(725)
    self.assertEqual(critter.rotation, 5)


  def test_critters_must_stay_in_boundary_of_habitat(self):
    critter = Critter()
    habitat = Habitat(0, 0, 100)
    critter.occupy(habitat)

    #make sure it can move
    critter.set_position(Point2(50, 50))
    self.assertEqual(critter.position, Point2(50, 50))

    #make sure it does not move
    critter.set_position(Point2(1000, 1000))
    self.assertNotEqual(critter.position.x, 1000)
    self.assertNotEqual(critter.position.y, 1000)
