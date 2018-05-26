def city_county(city, country):
	"""Returns a cleanly formatted city, country value"""
	return(city.title() + ', ' + country.title())

city = city_county('santiago', 'chile')	
print(city)

city = city_county('ushuaia', 'argentina')
print(city)

city = city_county('longyearbyen', 'svalbard')
print(city)


	