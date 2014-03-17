import unittest
import models
import ai

class TestChopTrees(unittest.TestCase):
    def setUp(self):
        self.actor = models.actors.Actor()
        self.subject = ai.tasks.ChopTrees(self.actor)


    def test_it_has_an_actor_for_the_task(self):
        self.assertEqual(self.actor, self.subject.actor, 'Chopping trees should know who is doing the work')

    def test_it_finds_a_tree_to_chop_down(self):
        pass
        
