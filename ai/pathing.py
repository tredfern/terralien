from pygsty.euclid import *
import random

class PathNode():
    def __init__(self, point, g=-1, h=-1):
        self.point = point
        self.g = g
        self.h = h
        self.f = g + h
        self.came_from = None
        self.open = True

    @property
    def not_tested(self):
        return self.g == -1 or self.h == -1

    def __repr__(self):
        return "PathNode( {} g={} h={} f={})".format(self.point, self.g, self.h, self.f)

    def __hash__(self):
        return hash(self.point)

def construct_path(node):
    if node.came_from == None:
        return [node]

    return construct_path(node.came_from) + [node]

def find_next_node(node_list, candidate = None):
    if len(node_list) == 0:
        return None

    if candidate:
        n = candidate
    else:
        n = min(node_list, key=lambda inst:inst.f)

    #remove from list so we don't keep testing it
    node_list.remove(n)
    return n

def find_path(start, end, map, max_length = 10):
    if not map:
        return []

    current_node = PathNode(point=start, g=0, h=heuristic_cost_estimate(start, end))
    nodes = {start : current_node}
    openset = set([current_node])
    candidate = None

    while openset:
        best_node = find_next_node(openset, candidate)
        best_node.open = False

        #At the end
        if best_node.point == end or best_node.g > max_length:
            return construct_path(best_node)

        test_tiles = map.getNeighbors(best_node.point.x, best_node.point.y)

        for tile in test_tiles:
            test_node = None
            if tile.point in nodes.keys():
                test_node = nodes[tile.point]
            if not test_node:
                test_node = PathNode(point=tile.point)
                nodes.update({test_node.point : test_node})
                openset.add(test_node)

            if not test_node.open:
                continue

            calc_g_score = best_node.g + heuristic_cost_estimate(best_node.point, tile.point)
            tentative_is_better = False

            if calc_g_score < test_node.g or test_node.not_tested:
                test_node.came_from = best_node
                test_node.g = calc_g_score
                test_node.h = heuristic_cost_estimate(tile.point, end)
                test_node.f = test_node.g + test_node.h

                if test_node.h == 0:
                    return construct_path(test_node)

                if test_node.f < best_node.f:
                    if candidate:
                        if test_node.f < candidate.f:
                            candidate = test_node
                    else:
                        candidate = test_node
    return []


def heuristic_cost_estimate(a, b):
    if a == b:
        return 0
    else:
        return (abs(a.x - b.x) + abs(a.y - b.y))
