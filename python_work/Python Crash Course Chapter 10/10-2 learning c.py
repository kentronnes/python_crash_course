file_name = 'learning_python.txt'
file_path = '/Users/kentronnes/Documents/python_crash_course/python_work/Python Crash Course Chapter 10/'
file = file_path + file_name


print("--- Version 1")
with open(file) as f:
	contents = f.read()
	contents = contents.replace('Python', 'C')
print(contents)	

print("\n--- Version 2")
with open(file) as f:
	lines = f.readlines()

for line in lines:
	#Get rid of newline, then replace Python with C.
	print(line.rstrip().replace('Python', 'C'))	


