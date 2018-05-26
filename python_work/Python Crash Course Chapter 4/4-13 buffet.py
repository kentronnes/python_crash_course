foods = (
	'mashed potatoes', 'fried chicken',
	'mac and cheese', 'prime rib', 
	'steamed vegetables')

for food in foods:
	print("\t" + food)

#causing an intentional error in trying to modify a tuple value
#foods[1] = 'fried rice'	

new_menu = foods + ('stir fry', 'tacos')
print("Our new menu:")
for food in new_menu:
	print("\t" + food)