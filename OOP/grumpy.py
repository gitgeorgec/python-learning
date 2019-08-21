class GrumpDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()

	def __missing__(self, key):
		print(f"You want {key}? well it is not here.")

	def __setitem__(self, key, value):
		print("You want to change the dictionary?")
		print("ok fine...")
		super().__setitem__(key, value)

data = GrumpDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)
