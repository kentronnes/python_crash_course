import admin_privileges
# Altername import below
# from admin_privileges import Admin

eric = admin_privileges.Admin('eric', 'metthes', 'e_matthes', 'e_matthews@example.com', 'alaska')
eric.describe_user()

eric_privileges = [
	'can reset passwords',
	'can moderate discussions',
	'can suspend accounts',
	]

eric.privileges.privileges = eric_privileges

print("\nThe admin " + eric.username + " has these privileges: ")
eric.privileges.show_privileges()						