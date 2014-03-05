import unittest
import models.statics

class TestTree(unittest.TestCase):
    def test_it_can_be_plopped_on_the_map_somewhere(self):
        tile = models.map.Tile(position=(3,3), terrain=models.map.grass())
        tree = models.statics.Tree(location=tile)
        self.assertEqual(tree.location, tile)
        self.assertEqual(tree.position, tile._worldPosition)

    def test_it_has_a_wood_value(self):
        t = models.statics.Tree()
        self.assertTrue(t.wood > 0)
