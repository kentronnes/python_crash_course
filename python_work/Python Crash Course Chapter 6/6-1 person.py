person = {'first_name': 'sarah', 'last_name': 'tronnes', 'age': '30', 'city': 'san pablo'}

print("This person's first name is " + person['first_name'].title() + ".")
print("\n")

print(person['first_name'].title() + "'s last name is " + person['last_name'].title() + ".")
print("\n")

print(person['first_name'].title() + 
	" " +
	person['last_name'].title() + 
	" is " + str(person['age']) + 
	" years old.")
print("\n")

print(person['first_name'].title() +
	" " + 
	person['last_name'].title() + 
	", " + 
	"age " + 
	str(person['age']) +
	", lives in " + 
	person['city'].title() +
	".")