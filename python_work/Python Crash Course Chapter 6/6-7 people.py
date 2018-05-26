people = []

sarah = {
	'first_name': 'sarah', 
	'last_name': 'tronnes', 
	'age': '30', 'city': 'san pablo'
	}
people.append(sarah)

ken = {
	'first_name': 'ken', 
	'last_name': 'tronnes', 
	'age': '34', 
	'city': 'san pablo'
	}
people.append(ken)	

noah = {
	'first_name': 'noah', 
	'last_name': 'tronnes', 
	'age': '0', 
	'city': "sarah's belly"
	}
people.append(noah)

for person in people:
	print("\n" + person['first_name'].title() + 
		" " + person['last_name'].title() + 
		" is " + str(person['age']) +
		" and lives in " + person['city'].title())

