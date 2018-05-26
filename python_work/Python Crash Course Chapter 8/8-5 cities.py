def city(city_name, country='the united states'):
	"""Diplays a city and the country it is in."""
	print("\n" + city_name.title() + " is in " + country.title() + ".")

city('denver')
city(city_name='austin')
city('barcelona', 'spain')