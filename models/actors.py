import random

import pygsty.models
import pygsty.graphics
import pygsty.geometry
import pygsty.euclid
import pyglet

import models.map
from models.map import TILE_SIZE
import ai
import event_log
import data


class Actor(pygsty.models.VisibleModel):
    def __init__(self, position=(0, 0)):
        super().__init__(position=position)
        self._goal = None
        self.path = []
        self._setupGraphics()

    @property
    def screen_x(self):
        return self.x * TILE_SIZE

    @property
    def screen_y(self):
        return self.y * TILE_SIZE

    @property
    def goal(self):
        return self._goal

    def update(self, map):
        while not self.goal:
            self._goal = pygsty.euclid.Point2(random.randint(0, map.array_width), random.randint(0, map.array_height) )
            if not map.getTile(self.goal.x, self.goal.y).terrain.passable:
                self._goal = None

        if not len(self.path):
            self.path = ai.pathing.find_path(self.position, self.goal, map)

        if len(self.path):
            n = self.path.pop(0)
            self.moveTo(n.point.x, n.point.y)
            if self.position == self._goal:
                self._goal = None

        self._sprite.x = self.screen_x
        self._sprite.y = self.screen_y

    def _setupGraphics(self):
        self._sprite = pyglet.sprite.Sprite(data._humanoid_grid_1[0], batch = self.batch)
