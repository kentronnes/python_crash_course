def make_shirt(size='large', text='I love Python'):
	"""Displays information about a shirt order."""
	print("\nYou have ordered a " + size + ' t-shirt with the message "'  + text.title() + '" to be printed on the front.')

make_shirt('medium')
make_shirt('large')
make_shirt('small', 'baby on board')