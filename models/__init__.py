import models.map
import models.actors
import models.statics
import models.event_log
import models.stockpiles
import models.cursor
import data
import ai.tasks

from pygsty.models import model_repository

characters = []
buildings = []
main_guy = None
_world_map = None

def add_character(actor):
    global characters
    characters.append(actor)

def get_map():
    global _world_map
    if not _world_map:
        _world_map = map.TileMap(100, 100)
    return _world_map

def build_world():
    global _world_map
    _world_map = data.generators.map.make_map(200, 200)
    _world_map.build_batch()

    start = models.get_map().randomTile()
    while start.terrain == models.map.terrains["water"]:
        start = models.get_map().randomTile()
    global main_guy
    main_guy = models.actors.Actor(start._position)
    add_character(main_guy)


def move_main_guy_to(x, y):
    global main_guy
    order = ai.tasks.MoveTo(main_guy, map.MapPoint(x, y))
