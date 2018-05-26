cities = {
	'denver': {
		'population': 682545, 
		'country': 'united states', 
		'fact': 'known as the mile high city'
		}, 
	'boulder': 
		{'population': 108090, 
		'country': 'united states', 
		'fact': 'home of CU Boulder Campus'
		},
	'austin': 
		{'population': 947890, 
		'country': 'united states', 
		'fact': "the state capital of Texas"
		}
}

for city, city_info in cities.items():
	print("\nHere is some information about " + city.title() + ":")
	print("\tThe population of " + 
		city.title() +
		" is about " + 
		str(city_info['population']) 
		+ ".")
	print("\t" + city.title() + 
		" is in the " + 
		city_info['country'].title() + 
		".")
	print("\tA fun fact about " + 
		city.title() + 
		" is that is is " +
		city_info['fact'] + 
		".")	 
#	country = city_info['country'].title()
