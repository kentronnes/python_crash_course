class User():
	"""Creating a class for user attributes."""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initiliaze the user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location
		self.login_atttempts = 0

	def describe_user(self):
		"""Display a summary of a user's information."""
		print("\n" + self.first_name + " " + self.last_name)
		print(" Username: " + self.username)
		print(" Email: " + self.email)
		print(" Location: " + self.location)

	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print("\nWelcome back, " + self.username + "!")

	def incremental_login_attempts(self):
		"""Track the number of subsequent login attempts by a user."""
		self.login_atttempts += 1

	def reset_login_attempts(self):
		"""Reset a user's login attempts to 0."""
		self.login_attempts = 0

ken = User('ken', 'tronnes', 'ktronnes', 'ktronnes@aol.com', 'fiji')
ken.describe_user()
ken.greet_user()

print("\nMaking 3 login attempts...")
ken.incremental_login_attempts()
ken.incremental_login_attempts()
ken.incremental_login_attempts()
print(" Login attempts: " + str(ken.login_atttempts))

print("\nResetting login attempts...")
ken.reset_login_attempts()
print(" Login attempts: " + str(ken.login_attempts))				