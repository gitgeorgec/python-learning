# def shout(fn):
# 	def wrapper(name):
# 		return fn(name).upper()
# 	return wrapper

def shout(fn):
	def wrapper(*args, **kwargs):
		return fn(*args, **kwargs).upper()
	return wrapper

@shout
def greet(name):
	return f"hi, i am {name}"

@shout
def order(main, side):
	return f"HI, I'd like the {main}, with a side of {side}, please."

print(greet("teddy"))
print(order("burger", "fries"))
