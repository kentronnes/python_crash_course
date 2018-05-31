def make_sandwich(*toppings):
	"""Summarize a sandwich we are about to make."""
	print("\nI am about to make a sandwich with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_sandwich('turkey', 'pastrami', 'lettuce', 'tomato', 'red onion', 'pickles', 'mustard', 'mayo')
make_sandwich('ham', 'cheddar cheese')
make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'red onions', 'italian dressing')		