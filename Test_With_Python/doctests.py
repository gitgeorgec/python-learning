# run =>  python3 -m doctest -v Test_With_Python/doctests.py
def add(x, y):
	""" add together x and y
	>>> add(2,3)
	5
	>>> add(100, 200)
	300
	"""
	return x + y

def double(values):
	""" double the values in a list

	>>> double([1,2,3,4])
	[2, 4, 6, 8]

	>>> double([])
	[]

	>>> double(['a', 'b', 'c'])
	['aa', 'bb', 'cc']

	>>> double([True, None])
	Traceback (most recent call last):
		...
	TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
	"""
	return [2 * element for element in values]

double([True, None])
