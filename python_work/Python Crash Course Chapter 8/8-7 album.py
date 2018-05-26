def make_album(artist_name, album_title, tracks=''):
	"""Returns a dictionary of information about an album."""
	describe_album = {'artist': artist_name.title(), 'album': album_title.title()}
	if tracks:
		describe_album['tracks'] = tracks
	return describe_album

album = make_album('foo fighters', 'the colour and the shape')
print(album)

album = make_album('pink floyd', 'dark side of the moon')
print(album)

album = make_album('light this city', 'terminal bloom', tracks=10)
print(album)	