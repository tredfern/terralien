import unittest
import models.event_log


class TestEventLog(unittest.TestCase):
    def test_it_returns_an_empty_entry_if_there_is_no_history(self):
        models.event_log.history = []
        e = models.event_log.last_event()
        self.assertTrue(e is None)

class TestEntry(unittest.TestCase):
    def test_it_has_a_message_of_what_happened(self):
        e = models.event_log.Entry("Brutal fighting event happened!")
        self.assertEqual("Brutal fighting event happened!", e.message, 'Message does not match')

    def test_it_has_a_time_stamp_of_when_it_happened(self):
        e = models.event_log.Entry("Event")
        self.assertIsInstance(e.created_at, models.event_log.GameDate)
        self.assertTrue(e.created_at.turn > 0)

    def test_it_adds_itself_to_the_event_log_history(self):
        e = models.event_log.Entry("Event 2")
        self.assertTrue(e in models.event_log.history, "Should be in the history")
        last_event = models.event_log.last_event()
        self.assertEqual(e, last_event)

    def test_it_can_be_associated_with_an_actor_and_makes_a_nice_message(self):
        a = models.actors.Actor()
        e = models.event_log.Entry("Event Foo", created_by = a)
        self.assertEqual(a, e.created_by, 'Should track who created this event')
        formatted_message = e.formatted_message()
        self.assertEqual("({}) {} : {}\n".format(e.created_at.turn, a.name, e.message),formatted_message )

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
