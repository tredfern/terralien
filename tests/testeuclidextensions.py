import unittest
from euclid import *
from euclidextensions import * 


class TestCircleExtensions(unittest.TestCase):
  def test_circles_can_detect_overlapping(self):
    circle1 = Circle(Point2(0,0), 2.5)
    circle2 = Circle(Point2(2,2), 1.0)
    circle3 = Circle(Point2(10, 10), 5.0)
    circle4 = Circle(Point2(1000, 1000), 10000.0)

    self.assertTrue(circle1.overlap(circle2))
    self.assertFalse(circle1.overlap(circle3))
    self.assertTrue(circle1.overlap(circle4))

  def test_circles_can_detect_points_within_it(self):
    circle = Circle(Point2(0, 0), 1.)
    self.assertTrue(circle.contains_point(Point2(0.2,0.2)))
    self.assertTrue(circle.contains_point(Point2(-0.2,-0.2)))
    self.assertFalse(circle.contains_point(Point2(2.,-2.)))
