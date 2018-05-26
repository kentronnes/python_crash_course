favorite_numbers = {
	'Ken' : [21,31,13],
	'Sarah' : [22,23,10],
	'Jim' : [15,19,18],
	'Linda' : [9,3,12],
	'Buster' : [28,4,48]
}


for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + " likes the following numbers:")
	for number in numbers:
		print(" " + str(number))