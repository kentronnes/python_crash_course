# when using a FileNotFoundException error in a function
# I found it necessary to include this at the top of my script
# under any import statement in order to run successfully 

try:
    FileNotFoundError
except NameError:
    #py2
    FileNotFoundError = IOError



# example
def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try: 
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None 
	else: 
		return username	