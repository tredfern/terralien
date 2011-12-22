import pork 
import unittest
from mock import * 

class TestRack(unittest.TestCase):
  def test_it_creates_a_window(self):
    with patch("pyglet.window.Window") as mock:
      r = pork.rack.Rack() 
      r.start()
      self.assertEqual(r.window, mock.return_value)
      mock.assert_called_with(800, 600)
