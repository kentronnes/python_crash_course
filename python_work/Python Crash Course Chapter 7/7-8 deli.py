sandwich_orders = ['roast beef', 'turkey', 'pastrami', 'ham']
finished_sandwiches = []

while sandwich_orders:
	current_order = sandwich_orders.pop()

	print("\nI made your " + current_order.title() + " Sandwich.")
	finished_sandwiches.append(current_order)

print("\nThe following sandwiches are ready:")
print("\n")
for sandwich in finished_sandwiches:
	print("\t" + sandwich.title())	
print("\n")	