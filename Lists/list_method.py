data = [1,2,3,4]
print(data)

data.append(5)
print(f"append(): {data}")

data.extend([1,2,3,4])
print(f"extend(): {data}")

data.insert(2, "hi")
print(f"insert(): {data}")

data.pop()
print(f"pop(): {data}")

data.pop(0)
print(f"pop(0): {data}")

data.remove("hi")
print(f"remove(hi): {data}")

# swap
names = ["Alex", "Bill"]

names[0], names[1] = names[1], names[0]
print(names)

data.clear()
print(f"clear(): {data}")

first_list = [1, 2, 3, 4, 2, 3, 4, 1, 32, 32, 11, 113]
print(first_list.index(2))
print(first_list.count(32))

name= ["a", "b", "c"]
name.reverse()
print(name)

first_list.sort()
print(first_list)

word = ["hello", "world", "good", "morning"]
print(" ".join(word))
