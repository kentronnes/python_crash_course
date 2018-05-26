guest_list = ['John F Kennedy', 'Jimi Hendrix', 'Martin Luther King']
invitation = ", would you like to come for dinner?"

guest_list.insert(0, 'James Hetfield')
guest_list.insert(3, 'Bruce Campbell')
guest_list.insert(5, 'Marylin Monroe')

print(guest_list)

no_of_guests = len(guest_list)
print(no_of_guests)

message = "There are " + str(no_of_guests) + " people coming to dinner."
print(message)