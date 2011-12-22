import pork 
import unittest
from mock import * 

@patch("pork.window.Window")
class TestRack(unittest.TestCase):
  def test_it_creates_a_window(self, mock_window):
    r = pork.rack.Rack() 
    r.start()
    self.assertEqual(r.window, mock_window.return_value)
    mock_window.assert_called_with(r, 800, 600)

class TestRackControllerManagement(unittest.TestCase):
  def setUp(self):
    self.patcher = patch("pork.window.Window")
    self.mock_pyg_window = self.patcher.start()
    self.rack = pork.rack.Rack()
    self.rack.start()

  def test_you_can_push_controllers_onto_the_stack(self):
    c1 = pork.controllers.BaseController()
    c2 = pork.controllers.BaseController()
    self.rack.push_controller(c1)
    self.rack.push_controller(c2)
    self.assertEqual(len(self.rack._controllers), 2)
    self.assertEqual(self.rack._controllers[0], c1)
    self.assertEqual(self.rack._controllers[1], c2)

  def test_you_can_pop_a_controller_off_the_stack(self):
    c1 = pork.controllers.BaseController()
    c2 = pork.controllers.BaseController()
    self.rack.push_controller(c1)
    self.rack.push_controller(c2)
    popped = self.rack.pop_controller()
    self.assertEqual(popped, c2)
    self.assertEqual(len(self.rack._controllers), 1)

  def test_it_draws_all_controllers_in_stack(self):
    c1 = pork.controllers.BaseController()
    c2 = pork.controllers.BaseController()
    self.rack.push_controller(c1)
    self.rack.push_controller(c2)
    c1.draw = Mock()
    c2.draw = Mock()
    self.rack.draw()
    c1.draw.assert_called_with()
    c2.draw.assert_called_with()

  def tearDown(self):
    self.patcher.stop()

