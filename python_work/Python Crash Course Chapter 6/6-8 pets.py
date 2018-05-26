norma = {
	'name': 'norma jean',
	'type': 'dog',
	'owner': 'ken',
}

ruby = {
	'name': 'ruby',
	'type': 'dog',
	'owner': 'pete',
}

watson = {
	'name': 'watson',
	'type': 'cat',
	'owner': 'sarah',
}

tau = {
	'name': 'tau',
	'type': 'dog',
	'owner': 'lee',
}

pets = []
pets.append(norma)
pets.append(ruby)
pets.append(watson)
pets.append(tau)

for pet in pets:
	print("\n" + 
		pet['owner'].title() +
		" owns a " + 
		pet['type'] + 
		" named " + 
		pet['name'].title() + 
		".")

for pet in pets:
	print("\nHere's what I know about " + pet['name'].title() + ":")
	for key, value in pet.items():
		print("\t" + key + ": " + str(value))	