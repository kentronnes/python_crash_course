guest_list = ['John F Kennedy', 'Jimi Hendrix', 'Martin Luther King']
invitation = ", would you like to come for dinner?"

cant_attend = guest_list.pop()
guest_list.append('Grandma Belle')

guest_list.insert(0, 'James Hetfield')
guest_list.insert(3, 'Bruce Campbell')
guest_list.insert(5, 'Marylin Monroe')

print(guest_list)


print(guest_list[0] + invitation)
print(guest_list[1] + invitation)
print(guest_list[2] + invitation)
print(guest_list[3] + invitation)
print(guest_list[-2] + invitation)
print(guest_list[-1] + invitation)


new_table = "Hello all, I just wanted to inform you that I was not \nable to get the larger table I had recently told you \nwe were to have and can now only invite 2 guests for dinner."

print(new_table)

print(guest_list)
update1 = "I'm sorry "
update2 = ", but I do not have room for you at our table for dinner."

guest1 = guest_list.pop()
print(update1 + guest1 + update2)

guest2 = guest_list.pop()
print(update1 + guest2 + update2)

guest3 = guest_list.pop()
print(update1 + guest3 + update2)

#print(guest_list)
	
guest4 = guest_list.pop()
print(update1 + guest4 + update2)

print(guest_list)

still_inv1 = "Hey "
still_inv2 = ", I wanted to let you know I still have room at my table for you at dinner."

print(still_inv1 + guest_list[0] + still_inv2)
print(still_inv1 + guest_list[1] + still_inv2)

