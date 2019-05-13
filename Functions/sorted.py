nums = [1,3,4,5,2,11,9]
tuple_num = (4,5,7,1,3,9,88,23,31)

print(sorted(nums))
print(sorted(tuple_num))

users = [
	{"name": "b", "tweets": ["hi","Adsfsadf","asdfasdfasf","Asdfsadf","asdfsdaf"]},
	{"name": "c", "tweets": ["hi","hello"]},
	{"name": "a", "tweets": ["hi","adf","asdfasdfas"]},
	{"name": "d", "tweets": ["hi",]},
]

print(sorted(users, key = lambda user: user["name"]))
print(sorted(users, key = lambda user: len(user["tweets"])))
