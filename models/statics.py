import pygsty.models
import pygsty.graphics
import random
import pyglet
import data


tree_types = ["leaf", "dark_leaf", "conifer", "dark_conifer"]
class Tree(pygsty.models.BaseModel):
    def __init__(self, location=None, tree_type = None):
        self.location = location
        if tree_type == None:
            tree_type = random.choice(tree_types)
        self.tree_type = tree_type

        if location:
            super().__init__(position=location._worldPosition)
            self.add_to_batch()
        self.wood = random.randint(1, 50)


    def add_to_batch(self):
        self._sprite = pyglet.sprite.Sprite(data.trees[self.tree_type],
        x = self.x,
        y = self.y,
        batch=self.batch,
        group=pygsty.graphics.middleground_group)
