import unittest
import ai
from ai.pathing import *

class TestPathNodes(unittest.TestCase):
    def test_its_f_score_is_g_plus_h(self):
        n = PathNode(point=(4, 2), g=1, h=3)
        self.assertEqual(n.f, 4, 'F Score should match h + g')

    def test_it_represents_itself_in_a_clear_fashion(self):
        n = PathNode(point=(4,2), g=1, h=3)
        self.assertEqual("PathNode( (4, 2) g=1 h=3 f=4)", repr(n), \
            'PathNodes represent some understandable data')

    def test_its_hash_is_a_tuple_of_its_points(self):
        n = PathNode(point=(3, 3), g=1, h=1)
        self.assertEqual(hash((3, 3)), hash(n), 'Hash should be the points of the node')

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

    def test_it_selects_the_next_node_to_test_by_lowest_f_score(self):
        lowest = PathNode(point=(10, 10), g=1, h=1)
        nodes = [
            PathNode(point=(11, 11), g=2, h=2),
            PathNode(point=(12, 12), g=3, h=2),
            PathNode(point=(12, 13), g=4, h=2),
            lowest,
            PathNode(point=(13, 14), g=5, h=2),
            PathNode(point=(13, 15), g=6, h=2),
        ]

        next_node = find_next_node(nodes)
        self.assertEqual(lowest, next_node, 'Should use the lowest f score node next')
        self.assert_(lowest not in nodes, 'Lowest should be removed from node list')

    def test_it_returns_nothing_if_node_list_is_empty_for_the_next_node(self):
        n = find_next_node([])
        self.assert_(n == None, 'Should not return anything if list is empty')

    def test_it_can_construct_a_path_out_of_a_sequence_of_linked_nodes(self):
        n1 = PathNode(point=(1,1), g=0, h=3)
        n2 = PathNode(point=(1,2), g=1, h=2)
        n3 = PathNode(point=(1,3), g=2, h=1)
        n4 = PathNode(point=(1,4), g=3, h=0)

        n4.came_from = n3
        n3.came_from = n2
        n2.came_from = n1

        path = construct_path(n4)
        self.assertEqual([n1,n2,n3,n4], path, 'Path should be a list of nodes in sequence')
