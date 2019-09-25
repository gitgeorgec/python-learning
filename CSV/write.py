from csv import writer, reader, DictWriter

with open("cat.csv", "w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["Name", "Age"])
	csv_writer.writerow(["Blue", 3])
	csv_writer.writerow(["Kitty", 1])

with open('fighters.csv') as file:
	csv_reader = reader(file)
	fighters = [[s.upper() for s in row] for row in csv_reader]
	for row in csv_reader:
		print(row)

with open('screaming_filters.csv', "w") as file:
	csv_writer = writer(file)
	for fighter in fighters:
		csv_writer.writerow(fighter)

with open("dog.csv", "w") as file:
	headers = ["Name", "Breed", "Age"]
	csv_writer = DictWriter(file, fieldnames=headers)
	csv_writer.writeheader()
	csv_writer.writerow({
		"Name": "hello",
		"Breed": "Bit",
		"Age": 10
	})
