number = input("Pick a number, any number: ")
number = int(number)

if number % 10 == 0:
	print("\nThe number " + str(number) + " is divisible by 10!")
else:
	print("\nThe number " + str(number) + " is not divisible by 10.")	