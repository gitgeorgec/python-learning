from time import time

def speed_test(fn):
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"executing {fn.__name__}")
		print(f"Time Elspsed: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_num_gen():
	return sum(x for x in range(1000000))

@speed_test
def sum_num_list():
	return sum([x for x in range(1000000)])


sum_num_gen()
sum_num_list()
