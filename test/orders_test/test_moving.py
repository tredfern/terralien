import unittest
from mock import *
import orders

from ai.pathing import PathNode
from pygsty.euclid import Point2

class TestWalk(unittest.TestCase):
    def test_given_an_actor_and_a_path_it_moves_across_terrain(self):
        actor = Mock()
        actor.moveTo = MagicMock()
        path = [PathNode(Point2(21, 20)), PathNode(Point2(22, 20))]
        o = orders.moving.Walk(actor, path)
        o.perform_action()
        actor.moveTo.assert_called_with(21, 20)
        self.assertFalse(o.completed())

    def test_order_is_completed_when_the_path_is_empty(self):
        actor = Mock()
        path = []
        o = orders.moving.Walk(actor, path)
        self.assertTrue(o.completed())
        #make sure this doesn't blow up
        o.perform_action()
