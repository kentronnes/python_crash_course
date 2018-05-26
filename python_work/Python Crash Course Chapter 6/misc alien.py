# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# print(alien_0['color'])
# print(alien_0['points'])

# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")

# print("\n")
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print("\n")
# print(alien_0)

# alien_1 = {}

# alien_1['color'] = 'green'
# alien_1['points'] = 5
# print(alien_1)
	
# alien_0 = {'color': 'green'}
# print("The alien is " + alien_0['color'] + ".")

# alien_0['color'] = 'yellow'
# print("The alien is now " + alien_0['color'] + ".")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
# alien_0['speed'] = 'fast'

# # Move alien to the right.
# # Determine how far to move the alien based on its current speed
# if alien_0['speed'] == 'slow':
# 	x_increment = 1

# elif alien_0['speed'] == 'medium':
# 	x_increment = 2

# else:
# 	# This must be a fast alien
# 	x_increment = 3

# # The new position is the old position plus the increment
# alien_0['x_position'] = alien_0['x_position'] + x_increment

# print("New x-position: " + str(alien_0['x_position']))		

# favorite_languages = {
# 	'jen' : 'python',
# 	'sarah' : 'c',
# 	'edward' : 'ruby',
# 	'phil' : 'python'
# 	}

# print(" Sarah's favorite language is " + 
# 	favorite_languages['sarah'].title() + 
# 	".")

# for name, language in favorite_languages.items():
# 	print(name.title() + "'s favorite language is " + language.title() + ".")

# print("\nNow just the names...")

# both of the beolw options will work to print out the keys of a list
# as looping through a set of keys is the default behavior when 
# looping through a dictionary

# for name in favorite_languages: 
# for name in favorite_languages.keys():
# 	print(name.title())	

# print("\nMessages to specific friends:")

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
# 	print("\n" + name.title())	

# 	if name in friends:
# 		print("\n Hi " + name.title() +
# 			", I see your favorite language is " +
# 			favorite_languages[name].title() + "!")
# 	if 'erin' not in favorite_languages.keys():
# 		print("\nErin, please take our poll!")	
# print(sorted(favorite_languages))

# for name in sorted(favorite_languages.keys()):
# 	print(name.title() + ", thank you for taking the poll.")

# print("The folowing languages have been mentiond:")
# for language in set(favorite_languages.values()):
# 	print("\t* " + language.title())

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
# 	print(alien)

# # Make an empty list for sorting aliens
# aliens = []

# # Make 30 aliens
# for alien_number in range(30):
# 	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# 	aliens.append(new_alien)

# for alien in aliens[0:3]:
# 	if alien['color'] == 'green':
# 		alien['color'] = 'yellow'
# 		alien['speed'] = 'medium'
# 		alien['points'] = 10	
# 	elif alien['color'] == 'yellow':
# 		alien['color'] = 'red'
# 		alien['speed'] = 'fast'
# 		alien['points'] = 15		

# # Show the first 5 aliens
# for alien in aliens[:5]:
# 	print(alien)
# print("...")	

# # Show how many aliens have been created
# print("Total number of aliens: " + str(len(aliens)))	


# # Store informatiom about a pizza being ordered
# pizza = {
# 	'crust': 'thick',
# 	'toppings': ['mushrooms', 'extra cheese'],
# 	}

# # Summarize the order
# print("You ordered a " + pizza['crust'] + "-crust pizza " + 
# 	"with the following toppings:")

# for topping in pizza['toppings']:
# 	print("\t" + topping)


# favorite_languages = {
# 	'jen' : ['python', 'ruby'],
# 	'sarah' : 'c',
# 	'edward' : ['ruby', 'go'],
# 	'phil' : ['python', 'haskell']
# 	}

# for name, languages in favorite_languages.items():
# 	if len(languages) > 1:
# 		print("\n" + name.title() + "'s favorite languages are:")
# 	else:
# 	   	print("\n" + name.title() + "'s favorite language is:")
# 	for language in languages:
# 		print("\t" + language.title())

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
	},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
	},
}


for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	# print(full_name.title())
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
