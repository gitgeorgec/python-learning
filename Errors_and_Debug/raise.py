def colorize(text, color):
	colors = ("cyan", "yellow", "blue", "green", "red")
	if type(text) is not str:
		raise TypeError("text must be instance or str")
	if type(color) is not str:
		raise TypeError("color must be instance or str")
	if color not in colors:
		raise ValueError("color is invalid color")
	print(f"Print {text} in {color}")

colorize("hello", "red")
# colorize(34, "blue")
colorize("hello", "mongo")
