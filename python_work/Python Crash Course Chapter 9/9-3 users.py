class User():
	"""Creating a class for user attributes."""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initiliaze the user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location

	def describe_user(self):
		"""Display a summary of a user's information."""
		print("\n" + self.first_name + " " + self.last_name)
		print(" Username: " + self.username)
		print(" Email: " + self.email)
		print(" Location: " + self.location)

	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print("\nWelcome back, " + self.username + "!")


ken = User('ken', 'tronnes', 'ktronnes', 'ktronnes@aol.com', 'fiji')
ken.describe_user()
ken.greet_user()

sarah = User('sarah', 'tronnes', 'snu06', 'sutron@msn.com', 'juneau')
sarah.describe_user()
sarah.greet_user()			

