file_name = 'pi_million_digits.txt'
file_path = '/Users/kentronnes/Documents/python_crash_course/python_work/Python Crash Course Chapter 10/'
file = file_path + file_name

with open(file) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

birthday = raw_input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi.")
else:
	print("Your birthday does not appear in the first million digits of pi.")

