pizzas = ['salami and olive', 'peperoni', 'supreme', 'bbq chicken']
for pizza in pizzas:
	print(pizza.title())
	print("I like " + pizza.title() + " Pizza." + "\n")

friend_pizzas = pizzas[:]

pizzas.append('mushroom')
friend_pizzas.append('sausage')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print("\t" + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print("\t" + pizza)	 