import unittest
import data.generators.names

class TestSyllables(unittest.TestCase):
    def test_it_has_at_least_one_vowel(self):
        syl = data.generators.names.create_syllable()
        self.assertRegex(syl, "[aeiouy]")


class TestNames(unittest.TestCase):
    def test_it_does_not_blow_up(self):
        name = data.generators.names.create_name()
        self.assertTrue(len(name) > 0, 'Should have gotten something back')
