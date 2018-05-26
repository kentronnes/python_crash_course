current_users = ['kentron83', 'snu2006', 'jimtron', 'normajean', 'fn-2187', 'admin', 'John']

print(current_users)


current_users = [user.lower() for user in current_users]

print(current_users)

new_users = ['snt81', 'noah_18', 'linda55', 'fn-2187', 'snu2006', 'JOHN']

print(new_users)

new_users = [user.lower() for user in new_users]

print(new_users)


for user in new_users:
	if user.lower() in current_users:
		print("\n" + user + " is not an available username. Please select a different username.")
#	elif user.title() in current_users:
#		print("\n" + user + " is not an available username. Please select a different username.")
	elif user.lower() not in current_users:
		print("\n" + user + " is an available username!")	

