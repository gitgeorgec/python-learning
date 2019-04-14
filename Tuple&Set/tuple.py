# tuple is commonly used for unchange data, tuple is Immutable
months = ("January", "February", "March" , "April", "May" , "June", "July" , "August" , "September", "October" , "November", "December")

print(months[0])

for month in months:
    print(month)

# tuple can be used as keys in dictionary
location = {
    (123.3413, 122,2322): "Tokoy Office",
    (10.3413, 216,2322): "London Office",
    (80.3413, 37,2322): "NewYork Office",
}

#some dictionary method like .items() return tuples
cat = {"name": "lulu", "age": 13}
print(cat.items())

x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

t = (1,2,3,3,3)
t.index(1) # 0
t.index(5) # ValueError: tuple.index(x): x not in tuple
t.index(3) # 2 - only the first matching index is returned