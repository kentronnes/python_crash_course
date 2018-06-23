class Car():
	"""A simple attempt to represent a car."""

	def __init__(self,make,model,year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model	
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing the car's mileage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_mileage(self,mileage):
		"""
		Set the odometer reading to a certain value.
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage	
		else:
			print("You can't roll back an odometer!")	

	def increment_odometer(self,miles):
		"""Add the given amount to the odometer reading."""
		self.odometer_reading += miles




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

print("Make and electirc car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()


