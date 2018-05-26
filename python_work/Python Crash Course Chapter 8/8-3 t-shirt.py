def make_shirt(size, text):
	"""Displays information about a shirt order."""
	print("\nYou have ordered a " + size + ' t-shirt with the message "'  + text.title() + '" to be printed on the front.')

make_shirt('medium', 'baby on board')
make_shirt(size='large', text='life of the party!')