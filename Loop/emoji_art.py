for i in range(10):
	print("\U0001f600" * (i+1))

i = 0
while i < 10:
	print("\U0001f600" * (i+1))
	i+=1

for i in range(0,20, 2):
	space = int(20-i/2) - 10
	print(" " * space + "\U0001f600" * (i+1))
