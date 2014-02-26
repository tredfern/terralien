
import pygsty
from pygsty.camera import Camera
from pygsty.drawing import *

import controllers

def main():
    pygsty.start()
    pygsty.engine().push_controller(pygsty.controllers.CameraController((100, 100), 100))
    pygsty.engine().push_controller(pygsty.controllers.PerformanceController())
    pygsty.engine().push_controller(controllers.GameController())
    pygsty.run()

if __name__ == '__main__':
    main()
