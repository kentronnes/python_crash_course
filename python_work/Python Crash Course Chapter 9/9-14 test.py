from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
    	"""Initialize the die."""
    	self.sides = sides

    def roll_die(self):
    	"""Return a number between 1 and the number of sides."""
    	return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
	result = d6.roll_die()
	results.append(result)
print("10 rolls of a 6-sided die:")
print(results)
