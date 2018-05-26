age = 3

if age < 2:
	print("\nBaby")

#variations of the same although I prefer being specifc
#with defining the range with "and" for the if statement
#elif age >= 2 and age < 4:
#	print("\nToddler")	
elif age < 4:
	print("\nToddler")


elif age >= 4 and age < 13:
	print("\nKid")

elif age >= 13 and age < 20:
	print("\nTeenager")

elif age >= 20 and age < 65:
	print("\nAdult")

else:
	print("\nElder")

