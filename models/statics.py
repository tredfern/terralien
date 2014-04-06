import pygsty.models
import pygsty.graphics
import random
import pyglet
import data
from models.map import TILE_SIZE


tree_types = ["leaf", "dark_leaf", "conifer", "dark_conifer"]
_match_map = {
    11: "_se",
    22: "_sw",
    31: "_s",
    104: "_ne",
    107: "_e",
    208: "_nw",
    214: "_w",
    248: "_n",
    255: ""
}
_test_scores = [255, 248, 214, 208, 107, 104, 31, 22, 11]

#1, 2, 4
#8, 0, 16
#32, 64, 128

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

    def update_sprite(self):
        self._sprite.image = data.trees[self.get_sprite_name()]

    def get_sprite_name(self):
        neighbors = pygsty.models.model_repository.get_neighbors(self.x, self.y)
        match_score = 0

        for n in neighbors:
            if type(n) is Tree:
                if n.tree_type == self.tree_type:
                    #top left
                    if n.x == self.x - 1:
                        if n.y == self.y + 1:
                            match_score += 1
                        elif n.y == self.y:
                            match_score += 8
                        elif n.y == self.y - 1:
                            match_score += 32
                    elif n.x == self.x:
                        if n.y == self.y + 1:
                            match_score += 2
                        elif n.y == self.y:
                            match_score += 0
                        elif n.y == self.y - 1:
                            match_score += 64
                    elif n.x == self.x + 1:
                        if n.y == self.y + 1:
                            match_score += 4
                        elif n.y == self.y:
                            match_score += 16
                        elif n.y == self.y - 1:
                            match_score += 128
        pygsty.logger.debug("Match Score: {}".format(match_score))
        for t in _test_scores:
            if t & match_score == t:
                match_score = t
                break

        if match_score in _match_map:
            return self.tree_type + "_forest" + _match_map[match_score]
        else:
            return self.tree_type
