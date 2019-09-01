def be_polite(fn):
	def wrapper():
		print("what a pleasure to meet you")
		fn()
		print("have a nice day")

	return wrapper

# greet = be_polite(greet)

@be_polite
def greet():
	print("My name is Tom")



greet()
