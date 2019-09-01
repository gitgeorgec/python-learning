from functools import wraps

def log_function_data(fn):
	@wraps(fn) #use this can save meta data to wrapper
	def wrapper(*args, **kwargs):
		"""I am wrapper function"""
		print(f"you are about to call {fn.__name__}")
		print(f"Here's the documentation: {fn.__doc__}")
		return fn(*args, *kwargs)
	return wrapper

@log_function_data
def add(x, y):
	"""Add two number together"""
	return x + y

add(10, 4)

print(add.__doc__)
print(add.__name__)
