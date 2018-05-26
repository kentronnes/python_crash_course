car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

sarah_bday = '12-22-1987'
print("\nIs Sarah's Birthday on '12-23-1987'? I predict False")
print(sarah_bday == '12-23-1987')

print("\nIs Sarah's on '12-22-1987'? I predict True")
print(sarah_bday == '12-22-1987')

locations = ['Austin', 'Denver', 'Boulder', 'San Francisco', 'San Diego']
new_location = 'Tacoma'
if new_location in locations:
	print("\nYes, I would be willing to " + new_location +  "!")
else:
	print("\nNo thanks. I would not be willing to " + new_location + ".")	

locations = ['Austin', 'Denver', 'Boulder', 'San Francisco', 'San Diego']
new_locations = 'Denver'
if new_locations not in locations:
	print("\nIs " + new_locations + " a place you would consider moving?")
else:
	print("\n" + new_locations + " is already a place you have considered moving to!")


age_0 = 55
age_1 = 65
age_2 = 75
#print("\nI think this test will result in 'True.'")
(age_0 >= 50) and (age_1 <= 67) and (age_2 == 75)

