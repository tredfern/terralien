import unittest
import models.map

class TestTileMap(unittest.TestCase):
    def test_it_generates_a_set_of_tiles_to_set_dimensions(self):
        map = models.map.TileMap()
        map.generate(10, 40)
        self.assertEqual(len(map.tiles), 400)
        self.assertIsInstance(map.tiles[0], models.map.Tile)
        self.assertEqual(map.width, 10)
        self.assertEqual(map.height, 40)


class TestTile(unittest.TestCase):
    def test_it_has_terrain(self):
        tile = models.map.Tile(models.map.GRASS)
        self.assertEqual(tile.terrain, models.map.GRASS)
