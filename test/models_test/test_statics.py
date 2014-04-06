import unittest
import models.statics
import pygsty.models

class TestTree(unittest.TestCase):
    def setUp(self):
        pygsty.models.model_repository.clear()

    def test_it_can_be_plopped_on_the_map_somewhere(self):
        tree = models.statics.Tree(position=(3, 4))
        self.assertEqual(tree.x, 3)
        self.assertEqual(tree.y, 4)
        self.assertEqual(tree.screen_x, 48)
        self.assertEqual(tree.screen_y, 64)

    def test_it_has_a_wood_value(self):
        t = models.statics.Tree()
        self.assertTrue(t.wood > 0)

    def test_it_can_figure_out_its_forest_sprite(self):
        t_nw_spoiler = models.statics.Tree(position=(2, 2), tree_type="leaf")
        t_nw = models.statics.Tree(position=(3, 3), tree_type="leaf")
        t_n = models.statics.Tree(position=(4, 3), tree_type="leaf")
        t_ne = models.statics.Tree(position=(5, 3), tree_type="leaf")
        t_w = models.statics.Tree(position=(3, 2), tree_type="leaf")
        t_center = models.statics.Tree(position=(4, 2), tree_type="leaf")
        t_e = models.statics.Tree(position=(5, 2), tree_type="leaf")
        t_sw = models.statics.Tree(position=(3, 1), tree_type="leaf")
        t_s = models.statics.Tree(position=(4, 1), tree_type="leaf")
        t_se = models.statics.Tree(position=(5, 1), tree_type="leaf")
        none = models.statics.Tree(position=(6, 1), tree_type="conifer")

        self.assertEqual(none.get_sprite_name(), "conifer")
        self.assertEqual(t_nw.get_sprite_name(), "leaf_forest_nw")
        self.assertEqual(t_n.get_sprite_name(), "leaf_forest_n")
        self.assertEqual(t_ne.get_sprite_name(), "leaf_forest_ne")
        self.assertEqual(t_w.get_sprite_name(), "leaf_forest_w")
        self.assertEqual(t_center.get_sprite_name(), "leaf_forest")
        self.assertEqual(t_e.get_sprite_name(), "leaf_forest_e")
        self.assertEqual(t_sw.get_sprite_name(), "leaf_forest_sw")
        self.assertEqual(t_s.get_sprite_name(), "leaf_forest_s")
        self.assertEqual(t_se.get_sprite_name(), "leaf_forest_se")
