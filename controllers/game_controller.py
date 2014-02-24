import pygsty

class GameController(pygsty.controllers.BaseController):
    def __init__(self):
        pass

    def draw(self):
        pygsty.models.render_models()

    def update(self, dt):
        pass
