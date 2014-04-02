import pygsty

import os
dir = os.path.dirname(__file__)
ui_resource_path = os.path.join(dir, '../data/images/gui')


def get_ui_resource_path():
    return ui_resource_path

def log_configuration():
    pygsty.logger.info("-- Configuration --")
    pygsty.logger.info("UI Resource Path: {}".format(get_ui_resource_path()))



log_configuration()
