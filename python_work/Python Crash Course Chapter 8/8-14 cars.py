def make_car(manufacturer, model_name, **attributes):
	"""Build a dictionary that store information about a customized car."""
	car={}
	car['make'] = manufacturer.title()
	car['model'] = model_name.title()
	for key, value in attributes.items():
		car[key] = value
	return car 

car = make_car('ford', 'mustang', color='red', year='1966')		

print(car)
