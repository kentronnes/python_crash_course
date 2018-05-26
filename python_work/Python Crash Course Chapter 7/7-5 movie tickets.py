prompt = input("Tell me your age and I can tell you how much your movie ticket will cost: ")
age = int(prompt)

if age < 3:
	print("\nYour ticket is free!")
elif age < 12:
	print("\nYour ticket will cost $10.")
else:
	print("\nYour tick will cost $15.")		