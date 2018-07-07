try:
	x = raw_input("Give me a number: ")
	x = int(x)

	y = raw_input("Give me another number: ")
	y = int(y)

except ValueError:
	print("Sorry, I really needed a number.")

else:
	sum = x + y
	print("The sum of " + str(x) + " and " + str(y) + " is " + str(sum) + ".")
