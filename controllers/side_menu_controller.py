import pygsty
import pyglet
import config

import pyglet_gui
from pyglet_gui.manager import Manager
from pyglet_gui.buttons import Button
from pyglet_gui.containers import VerticalContainer, HorizontalContainer, GridContainer
from pyglet_gui.gui import Frame
from pyglet_gui.constants import *

def build_stockpile(pressed):
    if pressed:
        pygsty.logger.info("Building Stockpiles")
    else:
        pygsty.logger.info("Doing Nothing")


class SideMenuController(pygsty.controllers.BaseController):
    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.setup_menu()

    def setup_menu(self):
        self._build_button = Button(label="Build Stockpile", on_press=build_stockpile)
        self._menu = VerticalContainer([self._build_button])
        self._manager = Manager(content=self._menu,
            window=pygsty.engine(),
            batch=self.batch,
            theme=config.ui_theme,
            anchor=ANCHOR_TOP_RIGHT)

    def draw_hud(self):
        self.batch.draw()
