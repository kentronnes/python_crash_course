import unittest
from city_functions import get_formatted_location

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Do locations like 'Santiago, Chile' work?"""
		formatted_location = get_formatted_location('santiago', 'chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

	def test_city_country_population(self):
		"""If a population is given, will the function still work?"""
		formatted_location = get_formatted_location('santiago', 'chile', population=5000000)
		self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000')

unittest.main()