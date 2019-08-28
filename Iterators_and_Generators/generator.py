def yes_or_no():
	i = 0
	while True:
		i = i + 1
		if i % 2 == 0:
			yield "no"
		else:
			yield "yes"

gen = yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
