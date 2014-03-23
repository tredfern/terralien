import unittest
import data.generators.map
import models.map

import pygsty.models
pygsty.models.set_repository_size(250, 250)

class TestMapGenerator(unittest.TestCase):
    def test_it_constructs_a_map_to_our_specified_size(self):
        map = data.generators.map.make_map(100, 150)
        self.assertEqual(100, map.width)
        self.assertEqual(150, map.height)


    def test_it_can_fill_the_map_with_specific_terrain(self):
        map = data.generators.map.make_map(10, 10)
        data.generators.map.fill_map(map, models.map.terrains["water"])
        self.assertEqual(models.map.terrains["water"], map.getTile(3, 4).terrain)
        self.assertEqual(models.map.terrains["water"], map.getTile( 8, 6).terrain)
        self.assertEqual(models.map.terrains["water"], map.getTile( 1, 1).terrain)
