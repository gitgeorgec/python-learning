d = dict(a=1, b=2)

c = d.copy()
print(c)
print(c == d)
print(c is d)

d.clear()
print(d)

new_user = {}.fromkeys(["name", "score", "email", "bio"], "init value")
print(new_user)

print(new_user.get("name"))
print(new_user.get("not exist key")) #None

new_user.pop("bio")
print(new_user)

# random remove item
new_user.popitem()
print(new_user)


# get dict items from other dict
student1 = {"number": 1, "age": 21}
person1 = {"name": "John"}

student1.update(person1)
print(student1)