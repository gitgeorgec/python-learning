import sqlite3
connect = sqlite3.connect("dog_db.db")
# create cursor object
cursor = connect.cursor()
# excute some sql
# cursor.execute("CREATE TABLE dogs (name TEXT, breed TEXT, age INTERGER);")
# insert_query  = '''INSERT INTO dogs
# 					VALUES ('Happy', 'Lab', 9);'''

# data = ('Lulu', 'Husky', 8)
# insert_query = "INSERT INTO dogs VALUES (?,?,?)"
# cursor.execute(insert_query, data)

####INESRT MANY
# dogs_data = [
# 	("Ramb", "Husky", 4 ),
# 	("Koka", "Chihuahua", 5),
# 	("Bibi", "Lab", 8),
# 	("Cony", "Corgi", 2)
# ]
# cursor.executemany("INERST INTO dogs VALUES (?,?,?)", dogs_data)
# for dog in dogs_data:
# 	cursor.execute("INSERT INTO dogs VALUES (?,?,?)", dog)
# 	# do something with data
# 	print("inserting now", dog[0])

cursor.execute("SELECT * FROM dogs WHERE name is 'Lulu'")
# for result in cursor:
# 	print(result)

# print(cursor.fetchone())
print(cursor.fetchall())

# commit changes
connect.commit()
connect.close()

