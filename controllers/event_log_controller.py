import pygsty.controllers
import logging
import models

import pyglet

class EventLogController(pygsty.controllers.BaseController):
    def __init__(self):
        super().__init__()

    @property
    def last_message(self):
        last_event = models.event_log.last_event()
        if last_event:
            return last_event.formatted_message()
        else:
            return "Nothing has happened."


    def draw_hud(self):
        label = pyglet.text.Label(self.last_message,
                          font_name='Arial',
                          font_size=18,
                          x=150, y= 45,
                          anchor_x='left', anchor_y='top')
        label.draw()
