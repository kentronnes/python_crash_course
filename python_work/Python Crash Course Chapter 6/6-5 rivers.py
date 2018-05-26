rivers = {'nile': 'egypt', 'mississippi': 'united states', 'amazon': 'brazil'}

for name, country in rivers.items():
	if country == 'united states':
		print("\nThe " + name.title() + " River is located in the " + country.title() + ".")	

	else:	
		print("\nThe " + name.title() + " River is located in " + country.title() + ".")

print("Rivers:")
for name in rivers.keys():
	print("\t" + name.title() + " River")		

print("\nCountries:")
for country in rivers.values():
	print("\t" + country.title())	