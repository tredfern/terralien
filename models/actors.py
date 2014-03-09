import random

import pygsty.models
import pygsty.graphics
import pygsty.geometry
import pygsty.euclid
import pyglet

import models.map
from models.map import TILE_SIZE
import ai
import data


class Actor(pygsty.models.VisibleModel):
    def __init__(self, position=(0, 0)):
        super().__init__(position=position)
        self._goal = None
        self.path = []
        self._setupGraphics()
        self.name = data.generators.names.create_name()

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
            if(random.randint(0, 10) > 7):
                n = self.path.pop(0)
                self.moveTo(n.point.x, n.point.y)
                if self.position == self._goal:
                    models.event_log.Entry("arrived at her destination", created_by = self)
                    self._goal = None

        self._sprite.x = self.screen_x
        self._sprite.y = self.screen_y

        if(random.randint(0, 10) > 7):
            if self._current == 1:
                self._sprite.image = self._image_two
                self._current = 2
            else:
                self._sprite.image = self._image_one
                self._current = 1

    def _setupGraphics(self):
        self._image_one = data._humanoid_grid1[0]
        self._image_two = data._humanoid_grid2[0]
        self._current = 1
        self._sprite = pyglet.sprite.Sprite(self._image_one, batch = self.batch, group = pygsty.graphics.foreground_group)
