my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for items in my_foods:
	print("\t" + items)

print("\nMy friend's favorite foods are:")
for items in friend_foods:
	print("\t" + items)