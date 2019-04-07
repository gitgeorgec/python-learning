colors = ["red", "blue", "teal", "yellow"]

for color in colors:
	print(color)

numbers = [1,2,3,4,5,6,7]

for number in numbers:
	print(number * 2)

index = 0
while index < len(colors):
	print(f"{index+1}: {colors[index]}")
	index += 1

