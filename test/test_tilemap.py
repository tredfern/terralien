import unittest
import models.map
import pygsty.graphics

class TestTileMap(unittest.TestCase):
    def test_it_generates_a_set_of_tiles_to_set_dimensions(self):
        map = models.map.TileMap()
        map.generate(10, 40)
        self.assertEqual(len(map.tiles), 40) #40 rows
        self.assertIsInstance(map.tiles[0][0], models.map.Tile)
        self.assertEqual(map.width, 10)
        self.assertEqual(map.height, 40)

    def test_it_can_access_tiles_and_tiles_are_for_the_correct_position(self):
        map = models.map.TileMap()
        map.generate(10, 5)
        t = map.getTile(9, 4)
        self.assertEqual(t, map.tiles[4][9])


class TestTile(unittest.TestCase):
    def test_it_has_terrain(self):
        t = models.map.Terrain()
        t.color = (1,1,1,1)
        tile = models.map.Tile((83, 42), t )
        self.assertEqual(tile.terrain, t)

    def test_it_is_represented_by_a_rectangle_for_its_world_coordinates(self):
        tile = models.map.Tile((83, 42), models.map.grass())
        test_rect = pygsty.geometry.rect_from_coordinates(83, 42, 88, 47)
        self.assertEqual(tile.rect, test_rect)
