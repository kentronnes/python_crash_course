# line = "Row, row, row your boat"
# count = line.count('row')
# print(count)

# count = line.lower().count('row')
# print(count)

file_contents = open('alice.txt').read()

count = file_contents.lower().count('the')

print(count)
	