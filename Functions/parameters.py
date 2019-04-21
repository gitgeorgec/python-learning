def square(num):
	return num * num

print(square(4))
print(square(8))

def divid(num1, num2):
	return num1/num2

print(divid(2, 5))

# default parameter

def exponent(num, power=1):
	return num ** power

print(exponent(2,3))
print(exponent(4))

# Keyword Arguments
print(exponent(power=4, num=3))
