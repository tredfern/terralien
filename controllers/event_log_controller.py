import pygsty.controllers
import logging
import models

import pyglet
import config

from pyglet_gui.manager import Manager
from pyglet_gui.document import Document
from pyglet_gui.gui import Frame

class EventLogController(pygsty.controllers.BaseController):
    def __init__(self):
        super().__init__()
        self.hud_batch = pyglet.graphics.Batch()
        self.doc = Document(self.last_message, width=600, height=50)
        self.frame = Frame(self.doc)
        self.manager = Manager(self.frame,
        window=pygsty.engine(), batch=self.hud_batch,
        theme=config.ui_theme)
        self.manager.set_position(10, 50)
        self._latest_event = None

    def draw_hud(self):
        self.hud_batch.draw()


    @property
    def last_message(self):
        last_event = models.event_log.last_event()
        if last_event:
            return last_event.formatted_message()
        else:
            return "Nothing has happened."

    def update(self, dt):
        if not models.event_log.last_event() is self._latest_event:
            self.doc.set_text(self.last_message)
