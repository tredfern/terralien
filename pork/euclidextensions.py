from euclid import *

#Circle Extensions
def circle_overlap(self, circle):
  distance = self.c.distance(circle.c)
  return distance < self.r + circle.r

def __circle_contains_point(self, point):
  if point == self.c:
    return True

  distance = self.c.distance(point)
  return distance < self.r

Circle.overlap = circle_overlap
Circle.contains_point = __circle_contains_point

def angle_length_to_vector2(angle, length):
  return Vector2(math.cos(math.radians(angle)) * length, math.sin(math.radians(angle)) * length)
