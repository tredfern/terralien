import pygsty
import pyglet_gui.theme

import os
dir = os.path.dirname(__file__)
ui_resource_path = os.path.join(dir, '../data/images/gui')


ui_theme = pyglet_gui.theme.ThemeFromPath(resources_path=ui_resource_path)


def log_configuration():
    pygsty.logger.info("-- Configuration --")
    pygsty.logger.info("UI Resource Path: {}".format(ui_resource_path))



log_configuration()
