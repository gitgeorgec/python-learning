instructor = {
    "name": "John",
    "age": 40,
    "skill": ["python", "linux",  "js"],
    "email": "John@gmail.com"
}

# get values
for value in instructor.values():
    print(value)

# get keys
for key in instructor.keys():
    print(key)

# get keys and values
for item in instructor.items():
    print(item)

for k, v in instructor.items():
    print(f"key is {k}, value is {v}")

# test key in dictionary
print("name" in instructor)
print("has_dog" in instructor)

# test values in dictionary
print("John" in instructor.values())
print(41 in instructor.values())
