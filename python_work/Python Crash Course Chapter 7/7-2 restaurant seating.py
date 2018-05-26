guests = input("How many will be in your dinner party? ")
guests = int(guests)

if guests > 8:
	print("\nYou will have to wait about 20 minutes for a table for " + str(guests) + ".")
else:
	print("\nWe can seat you right away!")	