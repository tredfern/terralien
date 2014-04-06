import models
import models.map
import random
import pygsty

LAKES = 3
LAKE_SIZE = 0.05
FORESTS = 15
FOREST_SIZE = 0.05

def make_map(width, height):
    map = models.map.TileMap(width, height)
    fill_map(map, models.map.terrains["grass"])
    create_lakes(map, LAKES, int(width * height * LAKE_SIZE))
    create_forest(map, FORESTS, int(width * height * FOREST_SIZE))
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

def create_forest(map, forest_count, size):
    for l in range(forest_count):
        forest_type = random.choice(models.statics.tree_types)
        current = map.randomTile()
        while not current.terrain.passable:
            current = map.randomTile()

        for i in range(size):
            if current.terrain.passable and pygsty.models.model_repository.is_vacant((current.x, current.y)):
                pygsty.logger.info("Adding tree to {}".format(current))
                models.statics.Tree((current.x, current.y), forest_type)
            neighbors = map.getNeighbors(current.point.x, current.point.y)
            current = random.choice(neighbors)

    def find_trees(test_obj):
        return type(test_obj) is models.statics.Tree

    trees = pygsty.models.model_repository.find_all(find_trees)
    for t in trees:
        t.update_sprite()
