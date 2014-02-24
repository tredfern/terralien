import unittest
import models.tilemap

class TestTileMap(unittest.TestCase):
    def test_it_generates_a_set_of_tiles_to_set_dimensions(self):
        map = models.TileMap()
        map.generate(10, 40)
        self.assertEqual(len(map.tiles), 400)
        self.assertIsInstance(map.tiles[0], models.Tile)
        self.assertEqual(map.width, 10)
        self.assertEqual(map.height, 40)

