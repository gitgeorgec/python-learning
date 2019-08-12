class User:
	active_users = 0

	@classmethod
	def display_active_user(cls):
		return f"There are currently {cls.active_users} active currently."

	@classmethod
	def form_string(cls, data_str):
		first, last, age = data_str.split(",")
		return cls(first, last, age)

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = int(age)
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}"

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_seniot(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

user1 = User("Joe", "Smith", 24)
user2 = User("Blance", "Lopez", 41)

print(User.display_active_user())


Tom = User.form_string("Tom, Jones, 12")
print(Tom.is_seniot())
