responses = {}

poll_active = True

while poll_active:
	name = input("\nWhat is your name? ")
	place = input("If you could visit one place in the world, where would you go? ")

	responses[name] = place 

	addtl_entry = input("\nWould you like to submit another entry? (yes/no)? ")
	if addtl_entry == 'no':
		poll_active = False

print("\n*** Dream Vacation Poll Results ***")
for name, place in responses.items():
	print("\n" + name + " would like to vacation in " + place + ".")    	
