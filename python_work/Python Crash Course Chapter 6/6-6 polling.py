favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'python'
	}

names = ['sarah', 'ken', 'steve', 'jen', 'zach']

for name in names:
	print(name.title())

	if name in favorite_languages.keys():
		print("Hi " + name.title() + ", thank you for taking the poll!")
	else:
		print("Hi " + name.title() + ", we show that you have not taken our poll yet.  Would you like to take it now?")		