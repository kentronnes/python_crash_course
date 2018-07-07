filenames = ['cats.txt', 'dogs.txt', 'mice.txt']

for filename in filenames:
	
	try:
		with open(filename) as f:
			contents = f.read()

	except FileNotFoundError:
		pass
	
	else:			
		print("\nReading file: " + filename)
		print(contents)
		