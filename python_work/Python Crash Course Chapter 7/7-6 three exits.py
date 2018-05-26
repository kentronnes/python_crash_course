prompt = "\nEnter a pizza topping you like on your pizzas:"
prompt += "\n(Enter 'quit' when you have entered all of your toppings.) "

active = True
while active:
	topping = input(prompt)

	if topping == 'quit':
		active = False
		
	else:	
		print("\nOk, we'll add " + topping + " to your pizza!")