class Restaurant():
	"""A class representing a restaurant."""

	def __init__(self,name, cuisine_type):
		"""Initialize name and cuisine attributes."""
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Prints a statement describing the restaurant."""
		msg = self.name + " serves wonderful " + self.cuisine_type + "."
		print("\n" + msg)

	def open_restaurant(self):
		"""Prints the hours of operation for the restaurant."""
		msg = self.name + " is open. Come on in!"
		print("\n" + msg)

restaurant = Restaurant("bobbie g's", 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)		 

restaurant.describe_restaurant()
restaurant.open_restaurant()	

