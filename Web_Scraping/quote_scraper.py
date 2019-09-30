import requests
from bs4 import BeautifulSoup
from csv import writer, reader
from time import sleep
import os
from random import choice

BASE_URL = "http://quotes.toscrape.com"

def getQuotes(url):
	next_url = ""
	has_next = True
	quotes = []

	while has_next:
		next_page_url = url + next_url
		response = requests.get(next_page_url)
		soup = BeautifulSoup(response.text, "html.parser")
		new_quotes = soup.select(".quote")
		quotes.extend(new_quotes)

		next_tag = soup.select_one(".next")

		if next_tag == None:
			has_next = False
		else:
			next_url = next_tag.find("a")["href"]
		# slow down request
		sleep(2)

	return quotes

def write_quotes_to_csv(quotes, csv_file_name):
	with open(csv_file_name, "w") as csv_file:
		csv_writer = writer(csv_file)
		csv_writer.writerow(["text", "author", "about_author_url"])

		for quote in quotes:
			text = quote.select_one(".text").get_text()
			author = quote.select_one(".author").get_text()
			about_author_url = BASE_URL + quote.find("a")["href"]
			csv_writer.writerow([text, author, about_author_url])

def init_data(csv_file_name):
	is_file_exist = os.path.isfile('./{}'.format(csv_file_name))

	if not is_file_exist:
		quotes = getQuotes(BASE_URL)
		write_quotes_to_csv(quotes, csv_file_name)

def play(csv_file_name):
	init_data(csv_file_name)
	with open(csv_file_name) as csv_file:
		csv_reader = reader(csv_file)
		data = list(csv_reader)

		print("start guess author of quote")
		guess_time = 0
		quote = choice(data)
		while True:
			guess_time += 1
			if guess_time == 1:
				about_req = requests.get(quote[2])
				about_soup = BeautifulSoup(about_req.text, "html.parser")
				author_born_data = about_soup.select_one(".author-born-date").get_text()
				author_born_location = about_soup.select_one(".author-born-location").get_text()
				print(quote[0])

			guess = str(input("Guess author: "))

			if guess != quote[1] and guess_time == 1:
				print("Author's first name is start with {}".format(quote[1][0]))
				print("Author's last name is start with {}".format(quote[1].split(" ")[1][0]))
			elif guess != quote[1] and guess_time == 2:
				print("Author is born in {}".format(author_born_data))
			elif guess != quote[1] and guess_time == 3:
				print("Author is born at {}".format(author_born_location))
			else:
				if guess == quote[1]:
					print("You guessed it! You won")
				else:
					print("wrong, answer is {}".format(quote[1]))
				state = input("Do you want to keep playing? (y/n)")
				guess_time = 0

				if(state == "y"):
					quote = choice(data)
				elif(state == "n"):
					print("Thank you for playing!")
					break

play("quotes.csv")
