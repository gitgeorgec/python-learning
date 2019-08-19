class Animal:
	cool = True
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")

class Cat(Animal):
	pass

if __name__ == "__main__":
	lulu = Cat("lulu", "Cat")
	lulu.make_sound("MEOW")
	print(lulu.cool)
	print(Cat.cool)


	print(isinstance(lulu, Cat))
	print(isinstance(lulu, Animal))
