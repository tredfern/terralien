import unittest
import models.actors

from models.actors import Actor

class TestActor(unittest.TestCase):
    def test_it_has_a_world_position(self):
        a = Actor(position=(20, 30))
        self.assertEqual(a.x, 20)
        self.assertEqual(a.y, 30)
