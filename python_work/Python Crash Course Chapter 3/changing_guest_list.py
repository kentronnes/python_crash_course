guest_list = ['John F Kennedy', 'Jimi Hendrix', 'Martin Luther King']
invitation = ", would you like to come for dinner?"

cant_attend = guest_list.pop()
guest_list.append('Grandma Belle')

cant_attend_message = " regretfully declined your dinner invitation."


print(guest_list[0] + invitation)
print(guest_list[1] + invitation)
print(guest_list[2] + invitation)

print(cant_attend + cant_attend_message)