import requests
from pyfiglet import figlet_format
from random import choice
from termcolor import colored

header = figlet_format("DAD JOKE 3000")
header = colored(header, color="yellow")
print(header)

term = input("what whould you like to search for?")
url = "https://icanhazdadjoke.com/search"
res = requests.get(url,
	headers={"Accept": "application/json"},
	params={"term": term}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
	print(f"I found {num_jokes} jokes about {term}. Here's one")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"I found one joke about {term}")
	print(res["results"][0]["joke"])
else:
	print(f"sorry, couldn't find a joke with your term: {term}")
