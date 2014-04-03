import pygsty
import pyglet_gui.theme

import os
dir = os.path.dirname(__file__)
ui_resource_path = os.path.join(dir, '../data/images/gui')


ui_theme = pyglet_gui.theme.ThemeFromPath(resources_path=ui_resource_path)


def log_configuration():
    pygsty.logger.info("-- Configuration --")
    pygsty.logger.info("UI Resource Path: {}".format(ui_resource_path))

event_log_ui = {
    "x": 0,
    "y": 0,
    "width":800,
    "height":100
}

side_menu_ui = {
    "x": 850,
    "y": 0,
    "width":210,
    "height": 750
}

log_configuration()
