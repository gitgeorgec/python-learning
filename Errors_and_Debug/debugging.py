import pdb

first = "FIRST"
second = "SECOND"
pdb.set_trace()

result = first + second
third = "THIRD"
result += third
print(result)

# common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue - finishes debugging)

def add_numbers(a,b,c,d):
	import pdb; pdb.set_trace()

	return a+b+c+d

add_numbers(1,2,3,4)
