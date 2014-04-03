import pygsty.controllers
import logging
import models

import pyglet
import config

from pyglet_gui.manager import Manager
from pyglet_gui.document import Document
from pyglet_gui.gui import Frame
from pyglet_gui.containers import VerticalContainer

class EventLogController(pygsty.controllers.BaseController):
    def __init__(self):
        super().__init__()
        self.hud_batch = pyglet.graphics.Batch()
        self.doc = Document(self.last_message, width=800, height=100, is_fixed_size=True)
        self.frame = Frame(self.doc)
        self.manager = Manager(self.frame,
            window=pygsty.engine(), batch=self.hud_batch,
            theme=config.ui_theme)
        self.manager.set_position(0, 0)
        self._latest_event = None
        self._log = self.last_message

    def draw_hud(self):
        self.hud_batch.draw()


    @property
    def last_message(self):
        last_event = models.event_log.last_event()
        if last_event:
            return last_event.formatted_message()
        else:
            return ""

    def update(self, dt):
        if not models.event_log.last_event() is self._latest_event:
            self._log = self.last_message + self._log
            self.doc.set_text(self._log)
            self._latest_event = models.event_log.last_event()
