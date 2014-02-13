#!/usr/bin/python

import pork
from pork.camera import Camera
from pork.drawing import *

import controllers

def main():
    pork.start()
    pork.engine().push_controller(pork.controllers.PerformanceController())
    pork.engine().push_controller(controllers.GameController())
    pork.run()

if __name__ == '__main__':
    main()
