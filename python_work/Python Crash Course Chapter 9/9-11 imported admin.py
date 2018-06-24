import users

eric = users.Admin('eric', 'metthes', 'e_matthes', 'e_matthews@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")

eric_privileges = [
	'can reset passwords',
	'can moderate discussions',
	'can suspend accounts',
	]

eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()