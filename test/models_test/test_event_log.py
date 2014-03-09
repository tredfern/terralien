import unittest
import models.event_log

class TestEntry(unittest.TestCase):
    def test_it_has_a_message_of_what_happened(self):
        e = models.event_log.Entry("Brutal fighting event happened!")
        self.assertEqual("Brutal fighting event happened!", e.message, 'Message does not match')

    def test_it_has_a_time_stamp_of_when_it_happened(self):
        e = models.event_log.Entry("Event")
        self.assertIsInstance(e.created_at, models.event_log.GameDate)
        self.assertTrue(e.created_at.turn > 0)

class TestGameDate(unittest.TestCase):
    def setUp(self):
        models.event_log.reset_turn_counter()

    def test_it_tracks_the_turn_number(self):
        self.assertEqual(1, models.event_log.GameDate().turn, 'Should start on turn one')

    def test_it_can_increment_the_turn(self):
        d = models.event_log.GameDate()
        self.assertEqual(1, d.turn, 'Should start on turn one')

        models.event_log.next_turn()
        d = models.event_log.GameDate()
        self.assertEqual(2, d.turn, 'Should be on turn two')

        models.event_log.next_turn()
        d = models.event_log.GameDate()
        self.assertEqual(3, d.turn, 'Should be on turn three')
