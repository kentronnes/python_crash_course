prompt = "\nEnter a pizza topping you like on your pizzas:"
prompt += "\n(Enter 'quit' when you have entered all of your toppings.) "

while True:
	topping = input(prompt)

	if topping != 'quit':
		print("\nOk, we'll add " + topping + " to your pizza!")

	else:	
		break