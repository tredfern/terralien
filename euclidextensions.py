from euclid import *

def circle_overlap(self, circle):
  distance = self.c.distance(circle.c)
  return distance < self.r + circle.r

Circle.overlap = circle_overlap

