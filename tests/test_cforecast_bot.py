#!/usr/bin/python3
"""Test module for cforecast_bot.py """
import unittest

class TestNamedEntityFinder(unittest.TestCase):
    def test_named_entity_finder(self):
        """This test checks if the function correctly identifies the city and date in the given message."""
        message = "I will be traveling to London on 25th December 2011"
        result = named_enity_finder(message)
        self.assertEqual(result, {'city': ['London'], 'date': ['25th December 2011']})
    
    def test_named_entity_finder_multiple_cities(self):
        """This test checks if the function correctly identifies multiple cities in the given message."""
        message = "I will be traveling from New York to London on 25th December 2012"
        result = named_enity_finder(message)
        self.assertEqual(result, {'city': ['New York', 'London'], 'date': ['25th December 2012']})
    
    def test_named_entity_finder_no_city_or_date(self):
        """This test checks if the function correctly handles a message with no city or date."""
        message = "I will be traveling soon"
        result = named_enity_finder(message)
        self.assertEqual(result, {'city': [], 'date': []})
    
    def test_named_entity_finder_empty_message(self):
        """This test checks if the function correctly handles an empty message."""
        message = ""
        result = named_enity_finder(message)
        self.assertEqual(result, {'city': [], 'date': []})
    
    def test_named_entity_finder_non_string_message(self):
        """ This test checks if the function correctly handles a
        non-string message by raising a TypeError """
        message = 12345
        with self.assertRaises(TypeError):
            result = named_enity_finder(message)

if __name__ == '__main__':
    unittest.main()
