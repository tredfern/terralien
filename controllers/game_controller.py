import pygsty
import models.map

class GameController(pygsty.controllers.BaseController):
    def __init__(self):
        self.map = models.map.TileMap()
        self.map.generate(200, 200)

    def draw(self):
        pygsty.models.render_models()

    def update(self, dt):
        pass
