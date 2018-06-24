from collections import OrderedDict

glossary = OrderedDict()

glossary['conditional test'] = 'an expression that can be evaluated as true or false.'
glossary['immutable'] = 'a value that cannot change.'
glossary['tuples'] = 'allows you to create a list of items that cannot change.'
glossary['slice'] = 'allows you to work with a specific group of items in a list'
glossary['list comprehension'] = "combines the for loop and creation of the new " \
                                 "elements into one line, and automaticaally appends "\
                                 "each new element."


for word, definition in glossary.items():
	print("\n" + word.title() + ": " + definition)