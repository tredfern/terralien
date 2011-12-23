#!/usr/bin/python

import controllers

import pork
from pork.camera import Camera
from pork.drawing import *
from pork.scene import *

pork.start()
pork.engine().push_controller(pork.controllers.PerformanceController())
pork.engine().push_controller(controllers.GameController())
pork.run()
