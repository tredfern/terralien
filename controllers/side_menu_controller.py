import pygsty
import pyglet
import config

import pyglet_gui
from pyglet_gui.manager import Manager
from pyglet_gui.buttons import Button
from pyglet_gui.containers import VerticalContainer, HorizontalContainer, GridContainer
from pyglet_gui.gui import Frame

def build_button_press():
    pygsty.logger.info("Build button pressed")


class SideMenuController(pygsty.controllers.BaseController):
    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.setup_menu()

    def setup_menu(self):
        self._build_button = Button(label="Build")
        self._menu = VerticalContainer([self._build_button])
        self._manager = Manager(content=self._menu,
            batch=self.batch,
            theme=config.ui_theme)
        self._manager.set_position(config.side_menu_ui["x"],config.side_menu_ui["y"])

    def draw_hud(self):
        self.batch.draw()
