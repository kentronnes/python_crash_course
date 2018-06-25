
# file_path = '/Users/kentronnes/Documents/python_crash_course/python_work/Python Crash Course Chapter 10/pi_digits.txt'
# with open(file_path) as file_object:
# 	contents = file_object.read()
# 	print(contents)

file_name = 'pi_digits.txt'
file_path = '/Users/kentronnes/Documents/python_crash_course/python_work/Python Crash Course Chapter 10/'
file = file_path + file_name

with open(file) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line)