# Pass a list of magician names through a function
# to print their names
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	"""Add 'the Great' to each magician name."""
	# Build a new list to hold the great magicians
	great_magicians = []

	# Make each magician great, and add it to great_magicians list.
	while magicians:
		magician = magicians.pop()
		great_magician = magician + ' the Great'
		great_magicians.append(great_magician)		

	# Add the great magicians back into magicians.
	for great_magician in great_magicians:
		magicians.append(great_magician)	

	return magicians	

magicians = ['houdini', 'david copperfield', 'david blaine']
show_magicians(magicians)

print("\nGreat Magicians:")
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)

print("\nOriginal Magicians:")
show_magicians(magicians)