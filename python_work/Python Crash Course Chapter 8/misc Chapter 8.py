# def greet_user():
# 	"""Display a simple greeting."""
# 	print("Hello!")

# greet_user()	


# def greet_user(username):
# 	"""Display a simple greeting."""
# 	print("Hello! " + username.title() + "!")

# greet_user('jesse')	


# # positional arguments
# def describe_pet(animal_type, pet_name):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')	


# # keyword arguments
# def describe_pet(animal_type, pet_name):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(animal_type='dog', pet_name='willie')	

# #when using keyword arguments, be sure to use the exact names of the parameters in the function's definition.

# # default arguments
# def describe_pet(pet_name, animal_type='dog'):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('willie')	
# describe_pet(pet_name='harry', animal_type='hamster')

# def get_formatted_name(first_name, last_name):
# 	"""Return a full name, neatly formatted."""
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)	

# def get_formatted_name(first_name, middle_name, last_name):
# 	"""Return a full name, neatly formatted."""
# 	full_name = first_name + ' ' + middle_name + ' ' + last_name
# 	return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)	

# # making argument optional, we move the optional argument to the 
# # end of the function and set = ''
# def get_formatted_name(first_name, last_name, middle_name=''):
# 	"""Return a full name, neatly formatted."""
# 	if middle_name:
# 		full_name = first_name + ' ' + middle_name + ' ' + last_name
# 	else:
# 		full_name = first_name + ' ' + last_name	
# 	return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)	

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)	

# def build_person(first_name, last_name):
# 	"""Return a disctionary of information about a person."""
# 	person = {'first': first_name, 'last': last_name}
# 	return person

# musician = build_person('jimi', 'hendrix')
# print(musician)	

# def build_person(first_name, last_name, age=''):
# 	"""Return a disctionary of information about a person."""
# 	person = {'first': first_name, 'last': last_name}
# 	if age:
# 		person['age'] = age
# 	return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)	


# def get_formatted_name(first_name, last_name):
# 	"""Return a full name, neatly formatted."""
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()

# # This is an infinite loop!
# while True:
# 	print("\nPlease tell me your name:")
# 	print("\n(enter 'q' at any time to quit)")

# 	f_name = raw_input("First name: ")
# 	if f_name == 'q':
# 		break

# 	l_name = raw_input("Last name: ")
# 	if l_name == 'q':
# 		break

# 	formatted_name = get_formatted_name(f_name, l_name)
# 	print("\nHello, " + formatted_name + "!")	

# def greet_users(names):
# 	"""Print a simple greeting to each user in the list."""
# 	for name in names:
# 		msg = "Hello, " + name.title() + "!"
# 		print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)		

# # Start with some designs that need to be printed.
# unprinted_designs = ['iphone case','robot pendant', 'dodecahedron']
# completed_models = []


# # Simulate printing each design, until none are left.
# # Move each design to completed models after printing.
# while unprinted_designs:
# 	current_design = unprinted_designs.pop()

# 	# Simulate creating a 3D print from the design.
# 	print("Printing model: " + current_design)
# 	completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
# 	print(completed_model)	

# def print_models(unprinted_designs, completed_models):
# 	"""
# 	Simulate printing each design, until none are left.
#     Move each design to completed models after printing.
#     """
# 	while unprinted_designs:
#    		current_design = unprinted_designs.pop()

#     	# Simulate creating a 3D print from the design.
# 		print("Printing model: " + current_design)
# 		completed_models.append(current_design)

# def show_completed_models(completed_models):
# 	"""Show all the models that were printed."""
# 	print("\nThe following models have been printed:")
# 	for completed_model in completed_models:
# 		print(completed_model)	

# unprinted_designs = ['iphone case','robot pendant', 'dodecahedron']
# completed_models = []


# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def print_models(unprinted_designs, completed_models):
# 	"""
# 	Simulate printing each design, until none are left
# 	Move each design to completed_models after printing.
# 	"""
# 	while unprinted_designs:
# 		current_design = unprinted_designs.pop()

# 		# Simulate creating a 3D print from the design.
# 		print("Printing: " + current_design)
# 		completed_models.append(current_design)

# def show_completed_models(completed_models):
# 	"""Show all the models that were printed."""
# 	print("\nThe following models have been printed:")
# 	for completed_model in completed_models:
# 		print(completed_models)

# unprinted_designs = ['ipnone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)		

# def make_pizza(*toppings):
# 	"""Print the list of toppings that have been requested."""
# 	print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')	

# def make_pizza(*toppings):
# 	"""Summarize the pizza we are about to make."""
# 	print("\nMaking a pizza with the following toppings:")
# 	for topping in toppings:
# 		print("- " + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(size, *toppings):
# 	"""Summarize the pizza we are about to make."""
# 	print("\nMaking a " + str(size) + 
# 		"-inch pizza with the following toppings:")
# 	for topping in toppings:
# 		print("- " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
# 	"""Build a dictionary containing everyting we know about a user."""
# 	profile = {}
# 	profile['first_name'] = first 
# 	profile['last_name'] = last
# 	for key, value in user_info.items():
# 		profile[key] = value 
# 	return profile 
	
# user_profile = build_profile('albert', 'einstein',
# 							location='princeton',
# 							field='physics')

# print(user_profile)		

							
