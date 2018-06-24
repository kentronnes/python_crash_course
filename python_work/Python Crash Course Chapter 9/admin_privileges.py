from users import User 

class Admin(User):
	"""Creating a class for users with admin privileges."""

	def __init__(self, first_name, last_name, username, email, location):
		"""Initialize the admin."""
		super().__init__(first_name, last_name, username, email, location)

		# Initialize an empty set of privileges.
		self.privileges = Privileges()



class Privileges():
	"""A class to store an admin's privileges."""

	def __init__(self, privileges=[]):
		"""Initialize the privileges object."""
		self.privileges = privileges

	def show_privileges(self):
		"""Display the privileges this amdinistrator has."""
		for privilege in self.privileges:
			print("-" + privilege)	

		else:
			print("- This user has no privileges.")	