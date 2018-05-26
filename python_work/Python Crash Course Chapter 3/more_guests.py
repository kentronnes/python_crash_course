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


new_table = "Hello all, I just wanted to inform you that I was able to get a larger table and a 3 more people will be joining us for dinner."

print(new_table)
