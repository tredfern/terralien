from mock import *
import unittest
import pork

@patch("pork.rack.Rack")
class TestPork(unittest.TestCase):
  def test_start_creates_and_starts_the_rack(self, mock_rack):
    r = mock_rack.return_value
    pork.start()
    self.assertEqual(pork.engine(), r)
    r.start.assert_called_with()
    mock_rack.assert_called_with()

