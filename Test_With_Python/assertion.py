# def add_positive_numbers(x, y):
# 	assert x > 0 and y > 0, "Both number must be positive"
# 	return x + y

# add_positive_numbers(1,1) # 2
# add_positive_numbers(1,-3) # AssertionError: Both number must be positive

def eat_junk(food):
	assert food in [
		"pizza",
		"ice",
		"candy",
		"fried butter",
	], "food must be a junk food"
	return f"I am eating {food}"


food = input("Enter a Food")
print(eat_junk(food))
