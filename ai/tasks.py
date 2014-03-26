import random
import ai
from pygsty.euclid import *
import models
import actions

class ChopTrees():
    def __init__(self, actor):
        self._actor = actor
        actor.current_task = self
        self.search_radius = 20

    @property
    def actor(self):
        return self._actor

    def find_target(self):
        def is_tree(mo):
            return isinstance(mo, models.statics.Tree)

        return models.model_repository.find_nearest(
            self._actor.position,
            self.search_radius,
            is_tree)


class MoveToRandomLocation():
    def __init__(self, actor, map):
        self._actor = actor
        actor.current_task = self
        self._goal = None
        while not self._goal:
            self._goal = Point2(random.randint(0, map.array_width), random.randint(0, map.array_height))
            if not map.getTile(self._goal[0], self._goal[1]).terrain.passable:
                self._goal = None
        self.path = ai.pathing.find_path(actor.position, self._goal, map)

    def next_step(self):
        if len(self.path):
            next = self.path.pop(0)
            actions.moving.walk(self._actor, next.point)

    def completed(self):
        return self._actor.position == self._goal

    def cannot_complete(self):
        return len(self.path) == 0
