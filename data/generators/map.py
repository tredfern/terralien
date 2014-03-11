import models
import models.map
import random

LAKES = 3
LAKE_SIZE = 0.1

def make_map(width, height):
    map = models.map.TileMap(width, height)
    fill_map(map, models.map.terrains["grass"])
    create_lakes(map, LAKES, int(width * height * LAKE_SIZE))
    return map

def fill_map(map, terrain):
    for row in map.tiles:
        for col in row:
            col.change_terrain(terrain)

def create_lakes(map, lake_count, size):
    for l in range(lake_count):
        cx = random.randint(0, map.array_width)
        cy = random.randint(0, map.array_height)
        nt = map.getTile(cx, cy)
        nt._terrain = models.map.terrains["water"]
        size = 150
        for i in range(size):
            nt = None
            while not nt:
                nx = random.randint(-2, 2)
                ny = random.randint(-2, 2)
                nt = map.getTile(cx + nx, cy + ny)

            nt._terrain = models.map.terrains["water"]
            nb = map.getNeighbors(cx, cy)
            for ne in nb:
                ne._terrain = models.map.terrains["water"]
            cx = nt.point.x
            cy = nt.point.y
