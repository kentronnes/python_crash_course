dream_home = 'Lafayette'
print(dream_home == 'Lafayette')
print(dream_home != 'Lafayette')
print(dream_home == 'San Jose')
print(dream_home != 'San Jose')

locations = ['Austin', 'Denver', 'Boulder', 'San Francisco', 'San Diego']
city = 'san antonio'
if city.title() in locations:
	print("\nYes, " + city + " is in your list of locations.")
if city.title() not in locations:
	print("\nNo, " + city.title() + " is not in your list of locations.")	
	print("\nNo, " + city.title() + " is not in your list of locations.")	


print("\n")	

city = 'Denver'
if city.lower() == 'denver':
	print("That is correct.")