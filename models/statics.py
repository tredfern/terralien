import pygsty.models
import pygsty.graphics
import random
import pyglet
import data
from models.map import TILE_SIZE


tree_types = ["leaf", "dark_leaf", "conifer", "dark_conifer"]
class Tree(pygsty.models.BaseModel):
    def __init__(self, position=(0,0), tree_type = None):
        super().__init__(position=position)
        self.screen_offset_x = TILE_SIZE
        self.screen_offset_y = TILE_SIZE
        if tree_type == None:
            tree_type = random.choice(tree_types)
        self.tree_type = tree_type

        self.initSprite(data.trees[self.tree_type], pygsty.graphics.middleground_group)
        self.wood = random.randint(1, 50)
