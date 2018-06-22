class Restaurant():
	"""A class representing a restaurant."""

	def __init__(self,name, cuisine_type):
		"""Initialize name and cuisine attributes."""
		self.name = name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Prints a statement describing the restaurant."""
		msg = self.name + " serves wonderful " + self.cuisine_type + "."
		print("\n" + msg)

	def open_restaurant(self):
		"""Prints the hours of operation for the restaurant."""
		msg = self.name + " is open. Come on in!"
		print("\n" + msg)

	def set_number_served(self, number_served):
		"""Allow user to set the number of customers that have been served."""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""Allow user to increment the number of customers served."""
		self.number_served += additional_served	

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))	
restaurant.number_served = 430
print("Number served: " + str(restaurant.number_served))	

restaurant.set_number_served(1257)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(239)
print("Number served: " + str(restaurant.number_served))