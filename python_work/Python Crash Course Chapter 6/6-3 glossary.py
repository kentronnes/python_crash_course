glossary = {
	'conditional test' : 'an expression that can be evaluated as true or false.',
	'immutable' : 'a value that cannot change.',
	'tuples' : 'allows you to create a list of items that cannot change.',
	'slice' : 'allows you to work with a specific group of items in a list.',
	'list comprehension' : 'combines the for loop and creation of new elements into one line, and automatically appends each new element.'
	}

glossary['set()'] = 'pulls a unique set of values from a dictionary.'

glossary['values()'] = 'returns a list of values without any keys from a dictionary.'

glossary['"backslash n'] = 'adds a line break in your code.'

glossary['backslash t'] = 'adds a tab, or spacing of 4, to your code.'

glossary['float'] = 'any number with a decimal point.'

for key, value in glossary.items():
	print("\n" + 
		key + 
		": " + 
		"\n\t" + 
		value)	