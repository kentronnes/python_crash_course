see city_functions.py and test_cities.py

# city_functions.py
""""A collection of functions for working with cities."""

def get_formatted_location(city, country):
	"""Generate a neatly formatted city and country."""
	location = city + ', ' + country

	return location.title()

# test_cities.py
import unittest
from city_functions import get_formatted_location

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Do locations like 'Santiago, Chile' work?"""
		formatted_location = get_formatted_location('santiago', 'chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

unittest.main()	