import unittest
from mock import *
import actions

from pygsty.euclid import Point2

class TestWalk(unittest.TestCase):
    def test_given_an_actor_and_a_path_it_moves_across_terrain(self):
        actor = Mock()
        actor.moveTo = MagicMock()
        o = actions.moving.walk(actor, Point2(21, 20))
        actor.moveTo.assert_called_with(21, 20)
