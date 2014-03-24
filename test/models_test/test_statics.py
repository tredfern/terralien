import unittest
import models.statics

class TestTree(unittest.TestCase):
    def test_it_can_be_plopped_on_the_map_somewhere(self):
        tree = models.statics.Tree(position=(3, 4))
        self.assertEqual(tree.x, 3)
        self.assertEqual(tree.y, 4)
        self.assertEqual(tree.screen_x, 48)
        self.assertEqual(tree.screen_y, 64)

    def test_it_has_a_wood_value(self):
        t = models.statics.Tree()
        self.assertTrue(t.wood > 0)
