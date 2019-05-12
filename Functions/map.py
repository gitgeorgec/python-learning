l = [1,2,3,4]

mapped_data = map(lambda x: x*2, l) # return map object, which can be convert into another data structure

doubles = list(mapped_data)

print(doubles) # [2,4,6,8]


names = [
	{'first':'Rusty', 'last': 'Steele'},
	{'first':'Colt', 'last': 'Steele', },
	{'first':'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))

print(first_names) # ['Rusty', 'Colt', 'Blue']
