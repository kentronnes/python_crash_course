""""A collection of functions for working with cities."""

def get_formatted_location(city, country, population=0):
	"""Generate a neatly formatted city and country."""
	location = city.title() + ', ' + country.title()
	if population:
		location += ' - population ' + str(population)
	return location

