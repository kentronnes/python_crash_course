sandwich_orders = ['roast beef', 'turkey', 'pastrami', 'ham', 'pastrami', 'pastrami']

finished_sandwiches = []
print("\nThe deli has run out of pastrami.  Sorry for the inconvenience.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print(sandwich_orders)	

while sandwich_orders:
	current_order = sandwich_orders.pop()
	print("\nI'm making your " + current_order.title() + " Sandwich.")

	finished_sandwiches.append(current_order)

for order in finished_sandwiches:
	print("\nI'm done making your " + order.title() + " Sandwich.")	 