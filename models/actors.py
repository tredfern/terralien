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


class Actor(pygsty.models.BaseModel):
    def __init__(self, position=(0, 0)):
        super().__init__(position=position)
        self.path = []
        self._setupGraphics()
        self.name = data.generators.names.create_name()
        self.screen_offset_x = TILE_SIZE
        self.screen_offset_y = TILE_SIZE
        self.current_task = None

    def update(self, map):
        if not self.current_task:
            self.current_task = ai.tasks.MoveToRandomLocation(self, map)

        self.current_task.next_step()
        if self.current_task.completed():
            models.event_log.Entry("arrived at her destination", created_by = self)
            self.current_task = None
        elif self.current_task.cannot_complete():
            models.event_log.Entry("canceled her task (unreachable)", created_by = self)
            self.current_task = None

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
