import unittest
import models.map
import pygsty.graphics

from models.map import *


class TestTileMap(unittest.TestCase):
    def test_it_generates_a_set_of_tiles_to_set_dimensions(self):
        map = TileMap(10, 40)
        self.assertEqual(len(map.tiles), 40) #40 rows
        self.assertIsInstance(map.tiles[0][0], models.map.Tile)
        self.assertEqual(map.width, 10)
        self.assertEqual(map.height, 40)
        self.assertEqual(map.array_width, 9)
        self.assertEqual(map.array_height, 39)

    def test_it_can_access_tiles_and_tiles_are_for_the_correct_position(self):
        map = TileMap(10, 5)
        t = map.getTile(9, 4)
        self.assertEqual(t, map.tiles[4][9])

    def test_it_returns_a_list_of_neighbors(self):
        map = TileMap(10, 10)
        expected = [
            map.getTile(2,3),
            map.getTile(3,3),
            map.getTile(4,3),
            map.getTile(2,4),
            map.getTile(4,4),
            map.getTile(2,5),
            map.getTile(3,5),
            map.getTile(4,5)
        ]
        neighbors = map.getNeighbors(3, 4)
        self.assertEqual(len(expected), len(neighbors), 'Lists should be the same size')
        for e in expected:
            self.assert_(e in neighbors, 'Expected item wasn\'t in neighbors list')

    def test_get_tile_returns_none_if_outside_range(self):
        map = TileMap(10, 10)
        t = map.getTile(11, 11)
        self.assert_(t == None, 'No tile to return')
        t = map.getTile(-1, -1)
        self.assert_(t == None, 'No tile to return')


    def test_it_does_not_return_tiles_that_go_off_the_edge(self):
        map = TileMap(1,1)
        expected = []
        neighbors = map.getNeighbors(0,0)
        self.assertEqual(expected, neighbors, "1x1 map has no neighbors to it's single tile")

    def test_you_get_an_empty_array(self):
        map = TileMap(1,1)
        self.assertRaises(OutOfBoundsError, map.getNeighbors,10,10)

class TestTile(unittest.TestCase):
    def test_it_has_terrain(self):
        t = Terrain()
        t.color = (1,1,1,1)
        tile = Tile((83, 42), t )
        self.assertEqual(tile.terrain, t)

    def test_it_is_represented_by_a_rectangle_for_its_world_coordinates(self):
        tile = Tile((2, 3), terrains["grass"])
        test_rect = pygsty.geometry.rect_from_coordinates(32 , 48, 48, 64)
        self.assertEqual(tile.rect, test_rect)

    def test_it_represents_itself_clearly(self):
        t = Tile((20, 30), terrains["grass"] )
        self.assertEqual("Tile( (20, 30) GRASS )", repr(t), 'Tiles should represent themselves clearly')

class TestTerrain(unittest.TestCase):
    def test_it_defaults_to_options_that_let_us_know_nothing_has_been_set(self):
        t = Terrain()
        self.assertEqual("UNKNOWN", t.name, 'Name should default to unknown')

    def test_terrains_have_good_names(self):
        self.assertEqual("GRASS", terrains["grass"].name, 'Grass should call itself grass')
        self.assertEqual("WATER", terrains["water"].name, "Water should be named water")
