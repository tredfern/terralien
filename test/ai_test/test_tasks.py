import unittest
import models
import ai

class TestChopTrees(unittest.TestCase):
    def setUp(self):
        self.actor = models.actors.Actor(position=(10, 10))
        self.subject = ai.tasks.ChopTrees(self.actor)


    def test_it_has_an_actor_for_the_task(self):
        self.assertEqual(self.actor, self.subject.actor, 'Chopping trees should know who is doing the work')

    def test_actor_knows_its_task(self):
        self.assertEqual(self.subject, self.actor.current_task)

    def test_it_finds_a_tree_to_chop_down_near_the_actor(self):
        target_tree = models.statics.Tree(position=(12, 12))
        t = self.subject.find_target()
        self.assertEqual([target_tree], t)

class TestMoveTo(unittest.TestCase):
    def setUp(self):
        self.actor = models.actors.Actor(position=(10, 10))
        self.subject = ai.tasks.MoveTo(self.actor, target=models.map.MapPoint(20, 20))

    def test_it_assigns_the_task_to_the_actor(self):
        self.assertEqual(self.subject, self.actor.current_task)

    def test_it_generates_a_path_to_the_target(self):
        self.assertTrue(len(self.subject.path))
