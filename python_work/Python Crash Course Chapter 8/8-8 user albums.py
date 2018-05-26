def make_album(artist_name, album_title, tracks=''):
	"""Returns a dictionary of information about an album."""
	describe_album = {
		'artist': artist_name.title(), 
		'album': album_title.title(),
		}
	if tracks:
		describe_album['tracks'] = tracks
	return describe_album

# prepare the prompts
artist_prompt = "\nWhat artist are you thinking of? "
album_prompt = "Which album? "

# let the user know how to quit
print("Enter 'quit' at any time to stop.")

while True:
	artist_name = raw_input("Artist: ")
	if artist_name == 'quit':
		break

	album_title = raw_input("Album: ")
	if album_title == 'quit':
		break

	formatted_album = make_album(artist_name, album_title)
	print(formatted_album)
	#print("\n" + album_title.title() + " by " + artist_name.title() + " is a great choice!")		

