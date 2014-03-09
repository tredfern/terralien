import pygsty.models
import pygsty.graphics
import random
import pyglet
import data

static_batch = pygsty.graphics.batches.create_batch()

class Tree(pygsty.models.VisibleModel):
    def __init__(self, location=None):
        self.location = location
        if location:
            super().__init__(position=location._worldPosition)
            self.add_to_batch()

        self.wood = random.randint(1, 50)


    def add_to_batch(self):
        self._sprite = pyglet.sprite.Sprite(data.get_tree_image(26, 3),
        x = self.x,
        y = self.y,
        batch=self.batch,
        group=pygsty.graphics.middleground_group)
