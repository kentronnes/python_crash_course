def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		# Simulate creating a 3D print from the design.
		print("Printing: " + current_design)
		completed_models.append(current_design)


def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_models)




def show_magicians(magicians):
	"""Pass a list of magician names through a function
	to print their names
	"""
	for magician in magicians:
		print(magician.title())


def make_car(manufacturer, model_name, **attributes):
	"""Build a dictionary that store information about a customized car."""
	car={}
	car['make'] = manufacturer.title()
	car['model'] = model_name.title()
	for key, value in attributes.items():
		car[key] = value
	return car 	