# class Animal:
	# def __init__(self, name, species):
	# 	self.name = name
	# 	self.species = species

# 	def __repr__(self):
# 		return f"{self.name} is a {self.species}"

# 	def make_sound(self, sound):
# 		print(f"this animal says {sound}")

from inheritrance import Animal

class Cat(Animal):
	def __init__(self, name, breed, toy):
		# self.name = name #1
		# self.species = species
		# Animal.__init__(self, name, species) #2
		super().__init__(name, species = "Cat")
		self.breed = breed
		self.toy = toy
	def play(self):
		print(f"{self.name} plays with {self.toy}")

blue = Cat("Blue", "Scottish", "String")
print(blue)
print(blue.name)
print(blue.species)
print(blue.breed)
print(blue.toy)

blue.play()

from user_class_method import User

class Moderator(User):
	total_mods = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_active_mods(cls):
		return f"There are currently {cls.total_mods} active mods."

	def remove_post(self):
		return f"{self.full_name()} remove a post from the {self.community} community"

print(User.display_active_user())
u1 = User("Tom", "Clon", 35)
u2 = User("Gin", "Clon", 35)
u3 = User("Hall", "Clon", 35)
print(User.display_active_user())
jasmine = Moderator("Jasmine", "Les", 34, "Piano")
jasmine2 = Moderator("Jasmine", "Les", 34, "Piano")
print(User.display_active_user())
print(Moderator.display_active_mods())


print(jasmine.full_name())
print(jasmine.community)
print(jasmine.remove_post())
