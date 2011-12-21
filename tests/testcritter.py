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
