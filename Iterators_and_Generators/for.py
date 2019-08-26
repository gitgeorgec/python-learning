def my_for(iterable, func):
	iterator = iter(iterable)
	while(True):
		try:
			thing = next(iterator)
			func(thing)
		except StopIteration:
			break

my_for([1,2,3,4], print)

def square(x):
	print(x*x)

my_for([1,2,3,4], square)
