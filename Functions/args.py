def sum_all_values(*args):
	total = 0
	for val in args:
		total += val

	return total

print(sum_all_values(1, 2, 3)) # 6

print(sum_all_values(1, 2, 3, 4, 5)) # 15

def fav_color(**kwargs):
	print(kwargs)

fav_color(colt="purple", rudy="red", ted="blue")

