class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']
	def  __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"you can't have a {species} pet")
		self.name = name
		self.species = species

	def set_specices(self, species):
		if species not in Pet.allowed:
			raise ValueError(f"you can't have a {species} pet")
		self.species = species

cat = Pet("Blue", "cat")
dog = Pet("Futty", "dog")
# dog = Pet("Tony", "tiger")
