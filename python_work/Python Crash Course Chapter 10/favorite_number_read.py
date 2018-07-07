import json


with open('favorite_number.json') as f:
	number = json.load(f)

print("I know what your favorite number is!  It's " + str(number) + ".")
