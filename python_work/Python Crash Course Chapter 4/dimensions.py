dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#the below statement would fail becuase items in the above tuple are immutable and cannot be chaged
#dimensions[0] = 250

for dimension in dimensions:
	print(dimension)

print("\n")

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
	print(dimension)		