def build_profile(first, last, **user_info):
	"""Build a dictionary containing everyting we know about a user."""
	profile = {}
	profile['first_name'] = first 
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value 
	return profile 
	
user_profile = build_profile('ken', 'tronnes',
							place_of_birth='vallejo, ca',
							favorite_music='metal',
							spouse='sarah',
							dream_home='colorado')

print(user_profile)									
