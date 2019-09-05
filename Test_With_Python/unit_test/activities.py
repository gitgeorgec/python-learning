from random import choice

def eat(food, is_healthy):
	if not isinstance(is_healthy, bool):
		raise ValueError("is_heathy must be boolean")
	ending = "because YOLO!"
	if is_healthy:
		ending = "because my body is a temple"

	return f"I'm eating {food}, {ending}"

def nap(num_hours):
	if num_hours > 2:
		return "Ugh I overslept. I didn't mean to nap"
	return f"I'm feeling refreshed after my {num_hours} hour nap"

def is_funny(name):
	if name == "tim":
		return "tim should not be funnny."
	else:
		return f"{name} should be funny"

def laugh():
	return choice(('lol', 'haha', 'tehteh'))
