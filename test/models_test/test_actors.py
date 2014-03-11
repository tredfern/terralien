import unittest
import models.actors

from models.actors import Actor

class TestActor(unittest.TestCase):
    def test_it_has_a_world_position(self):
        a = Actor(position=(20, 30))
        self.assertEqual(a.x, 20)
        self.assertEqual(a.y, 30)

    def test_it_picks_a_goal_if_it_does_not_have_one(self):
        a = Actor()
        self.assert_(a.goal == None, 'Should not start with a goal')

        map = models.map.TileMap(10, 10)
        
        a.update(map)
        self.assert_(a.goal is not None, 'Should have a goal')

    def test_it_has_a_name(self):
        a = Actor()
        self.assertTrue(len(a.name) > 0, "Should have a name")
