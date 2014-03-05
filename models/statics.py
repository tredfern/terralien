import pygsty.models
import pygsty.graphics
import random
import pyglet

static_batch = pygsty.graphics.batches.create_batch()

class Tree(pygsty.models.BaseModel):
    def __init__(self, location=None):
        self.location = location
        if location:
            super().__init__(position=location._worldPosition)
            self.add_to_batch()

        self.wood = random.randint(1, 50)


    def add_to_batch(self):
        v = (self.position[0] + 2, self.position[1] +2), \
            (self.position[0], self.position[1] +4), \
            (self.position[0] +4 , self.position[1] +4)
        i = [0,1,2]
        color = (100, 20, 30, 255)
        print("adding to batch {}".format(v))
        p = pygsty.graphics.IndexedPrimitive(v, i, color, pyglet.gl.GL_TRIANGLES)
        p.add_to_batch(static_batch)
