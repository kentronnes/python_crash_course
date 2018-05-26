favorite_places = {
	'ken': ['stockholm', 'ft. lauderdale', 'cozumel'],
	'sarah': ['rome', 'paris', 'london'],
	'pete': ['monument', 'dublin', 'austin']
	}

for person, places in favorite_places.items():
	print("\n" + person.title() + "'s favorite places to visit are:")

	for place in places:
		print("\t* " + place.title())
