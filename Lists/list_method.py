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



data.clear()
print(f"clear(): {data}")


