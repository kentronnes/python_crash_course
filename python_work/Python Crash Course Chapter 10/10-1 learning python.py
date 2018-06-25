file_name = 'learning_python.txt'
file_path = '/Users/kentronnes/Documents/python_crash_course/python_work/Python Crash Course Chapter 10/'
file = file_path + file_name

print("--- Reading in the entire file:")
with open(file) as f:
	contents = f.read()
print(contents)	

print("\n--- Looping over the lines:")
with open(file) as f:
	for line in f:
		print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(file) as f:
	lines = f.readlines()

for line in lines:
	print(line.rstrip())	