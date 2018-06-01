def make_sandwich(*toppings):
	"""Summarize a sandwich we are about to make."""
	print("\nI am about to make a sandwich with the following toppings:")
	for topping in toppings:
		print("- " + topping)