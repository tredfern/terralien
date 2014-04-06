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

class TestWall(unittest.TestCase):
    def test_it_can_figure_out_its_proper_sprite_by_neighbors(self):
        pygsty.models.model_repository.clear()
        pygsty.models.model_repository.set_position_set_size(100, 100)
        w_none = models.statics.Wall(position=(30, 30), wall_type="wood")

        w_nsew = models.statics.Wall(position=(10, 10), wall_type="wood")
        w_se2 = models.statics.Wall(position=(9, 11), wall_type="wood")
        w_sew = models.statics.Wall(position=(10, 11), wall_type="wood")
        w_sw2 = models.statics.Wall(position=(11, 11), wall_type="wood")
        w_nse = models.statics.Wall(position=(9, 10), wall_type="wood")
        w_nsw = models.statics.Wall(position=(11, 10), wall_type="wood")
        w_ne2 = models.statics.Wall(position=(9, 9), wall_type="wood")
        w_new = models.statics.Wall(position=(10, 9), wall_type="wood")
        w_nw2 = models.statics.Wall(position=(11, 9), wall_type="wood")

        w_se = models.statics.Wall(position=(20, 20), wall_type="wood")
        w_ns = models.statics.Wall(position=(20, 19), wall_type="wood")
        w_ns2 = models.statics.Wall(position=(22, 19), wall_type="wood")
        w_ne = models.statics.Wall(position=(20, 18), wall_type="wood")
        w_ew = models.statics.Wall(position=(21, 20), wall_type="wood")
        w_ew2 = models.statics.Wall(position=(21, 18), wall_type="wood")
        w_sw = models.statics.Wall(position=(22, 20), wall_type="wood")
        w_nw = models.statics.Wall(position=(22, 18), wall_type="wood")

        self.assertEqual(w_none.get_sprite_name(), "wood")

        self.assertEqual(w_nsew.get_sprite_name(), "wood_nsew")
        self.assertEqual(w_sew.get_sprite_name(), "wood_sew")
        self.assertEqual(w_nse.get_sprite_name(), "wood_nse")
        self.assertEqual(w_nsw.get_sprite_name(), "wood_nsw")
        self.assertEqual(w_new.get_sprite_name(), "wood_new")

        self.assertEqual(w_se.get_sprite_name(), "wood_se")
        self.assertEqual(w_ns.get_sprite_name(), "wood_ns")
        self.assertEqual(w_ne.get_sprite_name(), "wood_ne")
        self.assertEqual(w_ew.get_sprite_name(), "wood_ew")
        self.assertEqual(w_sw.get_sprite_name(), "wood_sw")
        self.assertEqual(w_nw.get_sprite_name(), "wood_nw")
