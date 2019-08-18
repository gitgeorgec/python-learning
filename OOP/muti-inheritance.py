class Aquatic:
    def __init__(self, name):
        print("Aquatic init")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming"

    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        print("Ambulatory init")
        self.name = name

    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land!"

class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("Penguin init")
        super().__init__(name = name)

# jaws = Aquatic("Jaws")
# lassie = Ambulatory("Lassie")
captain_cool = Penguin("Captain_cool")

print(captain_cool.swim())
print(captain_cool.walk())
print(captain_cool.greet())

print(f"captain_cool is instance of Penguin: {isinstance(captain_cool, Penguin)}")
print(f"captain_cool is instance of Aquatic: {isinstance(captain_cool, Aquatic)}")
print(f"captain_cool is instance of Ambulatory: {isinstance(captain_cool, Ambulatory)}")