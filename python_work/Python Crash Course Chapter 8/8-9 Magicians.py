# Pass a list of magician names through a function
# to print their names
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

magicians = ['houdini', 'david copperfield', 'david blaine']
show_magicians(magicians)