import unittest
import ai
from ai.pathing import *

class TestPathNodes(unittest.TestCase):
    def test_its_f_score_is_g_plus_h(self):
        n = PathNode(point=(4, 2), g=1, h=3)
        self.assertEqual(n.f, 4, 'F Score should match h + g')


class TestPathBuilding(unittest.TestCase):
    def test_heuristic_score_is_zero_for_the_same_points(self):
        h_score = heuristic_cost_estimate(Point2(0,0), Point2(0,0))
        self.assertEqual(0, h_score, 'H Score should be zero')

    def test_heuristic_score_is_the_distance_between_two_points(self):
        p1 = Point2(0, 0)
        p2 = Point2(10, 100)
        d = p1.distance(p2)

        h_score = heuristic_cost_estimate(p1, p2)
        self.assertEqual(d, h_score, 'H Score should match distance')
