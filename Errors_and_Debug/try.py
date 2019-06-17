# try:
# 	foobar
# except:
# 	print("PROBLEM")
# print("after the try")

d = {"name": "Ricky"}

def get(d, key):
	try:
		return d[key]
	except KeyError:
		return None
print(get(d, "name"))
print(get(d, "city"))


while True:
	try:
		num = int(input("please enter a number: "))
	except ValueError:
		print("That's not a number!")
	else:
		print("GOOD JOB, you enter a number")
		break
	finally:
		print("RUN no MATTER what")
print("rest of game logic runs")

# def divide(a,b):
# 	try:
# 		result = a/b
# 	except ZeroDivisionError as err:
# 		print("don't divide by zero!")
# 		print(err)
# 	except TypeError as err:
# 		print("a and b must be ints or float!")
# 		print(err)
# 	else:
# 		print(f"{a} divided by {b} is {result}")

def divide(a,b):
	try:
		result = a/b
	except (ZeroDivisionError, TypeError)as err:
		print("something went wrong!")
		print(err)
	else:
		print(f"{a} divided by {b} is {result}")

divide(1, 2)
divide(1, "a")
divide(1, 0)
