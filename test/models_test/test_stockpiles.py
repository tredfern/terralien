import unittest
from mock import Mock
from models.stockpiles import Stockpile

class TestStockpile(unittest.TestCase):
    def test_it_tracks_resources_stored_in_it(self):
        resource = Mock()
        stockpile = Stockpile(0, 0, 10, 10)
        stockpile.add(resource)
        self.assertTrue(resource in stockpile)
