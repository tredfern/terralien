from pygsty.euclid import *
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

    def __repr__(self):
        return "PathNode( {} g={} h={} f={})".format(self.point, self.g, self.h, self.f)

def construct_path(node):
    if node.came_from == None:
        return [node]

    return construct_path(node.came_from) + [node]

def find_next_node(node_list):
    if len(node_list) == 0:
        return None

    n = node_list[0]
    for t in node_list:
        if t.f < n.f:
            n = t

    #remove from list so we don't keep testing it
    node_list.remove(n)
    return n

def heuristic_cost_estimate(a, b):
  if a == b:
    return 0
  else:
    return a.distance(b)
