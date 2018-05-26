#usernames = ['kentron83', 'snu2006', 'jimtron', 'normajean', 'fn-2187', 'admin']
usernames = []

for user in usernames:
	if user == 'admin':
		print("\nHello " + user + ", would you like to see a status report?")
	elif user != 'admin':	
		print("\nHello " + user +", welcome!")
else:
	print("\nWe need to find some users!")	



