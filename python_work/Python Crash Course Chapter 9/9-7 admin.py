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

class Admin(User):
	"""Creating a class for users with admin privileges."""
	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the admin."""
		super().__init__(first_name, last_name, username, email, location)
		self.privileges = []

	def show_privileges(self):
		"""Display the privileges this admin has."""
		print("\nPrivileges:")
		for privilege in self.privileges:
			print("-" + privilege)

eric = Admin('eric', 'metthes', 'e_matthes', 'e_matthews@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
	'can reset passwords',
	'can moderate discussions',
	'can suspend accounts',
	]

eric.show_privileges()							