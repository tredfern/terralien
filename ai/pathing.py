from euclid import *
import random

class PathNode():
  def __init__(self, point, g, h):
    self.point = point
    self.g = g
    self.h = h
    self.came_from = None

  @property
  def f(self):
    return self.g + self.h

def get_key(point):
  return (point.x, point.y)

def find_path(start_point, end_point):
  closedset = []
  openset = [start_point]
  came_from =  {}

  current_key = get_key(start_point)
  g_score = {current_key:0}
  h_score = {current_key:heuristic_cost_estimate(start_point, end_point)}
  f_score = {current_key:g_score[current_key] + h_score[current_key]}

  while len(openset) > 0:
    x = openset[0]
    f = f_score[get_key(x)]
    for t in openset:
      if f_score[get_key(t)] < f:
        x = t
        f = f_score[get_key(t)]

    if x == end_point:
      return construct_path(x, came_from)
    openset.remove(x)
    closedset.append(x)

    test_points = get_neighbor_nodes(x)
    for y in test_points:
      if y in closedset:
        continue

      tentative_g_score = g_score[get_key(x)] + x.distance(y)
      tentative_is_better = False
      if not y in openset:
        openset.append(y)
        tentative_is_better = True
      elif tentative_g_score < g_score[get_key(y)]:
        tentative_is_better = True

      if tentative_is_better:
        came_from[get_key(y)] = x
        g_score[get_key(y)] = tentative_is_better
        h_score[get_key(y)] = heuristic_cost_estimate(y, end_point)
        f_score[get_key(y)] = g_score[get_key(y)] + h_score[get_key(y)]


def heuristic_cost_estimate(a, b):
  if a == b:
    return 0
  else:
    return a.distance(b)

def construct_path(point, nodes):
  path = []
  if get_key(point) in nodes:
    path = construct_path(nodes[get_key(point)], nodes)
    path.append(point)
  return path

def shortest(a, b):
  return cmp(a.f, b.f)

def get_neighbor_nodes(point):
  neighbors = []
  for x in range(-1, 2):
    for y in range(-1, 2):
      pt = Point2(point.x + x, point.y + y)
      if pt.x >= 0 and pt.x < width and pt.y >= 0 and pt.y < height and not blocking_tile(pt):
        neighbors.append(pt)

  return neighbors

def point_in_path(point, path):
  for pt in path:
    if point == pt:
      return True
  return False

def blocking_tile(pt):
  return tile_map[pt.y][pt.x]  == 0
