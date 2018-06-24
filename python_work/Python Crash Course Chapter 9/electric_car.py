"""A set of classes that can be used to represent electric cars."""

from car import Car

class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Print a ststement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately "	+ str(range) + " miles on a full charge."
	##	message += " miles on a full charge."
		print(message)

	def upgrade_battery(self):
		"""Updgrade the battery if possible."""
		if self.battery_size == 70:
			self.battery_size = 85
			print("Updgraded battery to 85 kWh.")
		else:
			print("Battery is already upgraded.")


class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electirc car.
		"""
		super().__init__(make, model, year)
		self.battery = Battery()		