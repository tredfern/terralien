import pygsty
import pyglet

from pyglet_gui.manager import Manager
from pyglet_gui.document import Document
import data

document = pyglet.text.decode_attributed('''
In {bold True}Pyglet-gui{bold False} you can use
{underline (255, 255, 255, 255)}pyglet{underline None}'s documents in a
scrollable window.

You can also {font_name "Courier New"}change fonts{font_name Lucia Grande},
{italic True}italicize your text{italic False} and use all features of Pyglet's document.
''')

class TestDocumentController(pygsty.controllers.BaseController):
    def __init__(self):
        self.hud_batch = pyglet.graphics.Batch()
        self.manager = Manager(Document(document, width=300, height=50),
        window=pygsty.engine(), batch=self.hud_batch,
        theme=data.ui_theme)

    def draw_hud(self):
        self.hud_batch.draw()
