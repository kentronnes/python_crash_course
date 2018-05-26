magicians = ['alice', 'david', 'carolina']

#for magician in magicians:
#	print(magician)

for magician in magicians:
	print(magician.title() + ", that was agreat trick!")
	##the \n will create a new line after each set of statements grouping each magicians' statement together
	print("I can't wait to see your next trick " + magician.title() + ".\n")

##since the below is not indented it will not be considered to be a part of the above for loop
##this is a good way/place to summarize the output of a for statement
print("Thank you, everyone.  That was a great magic show!")	