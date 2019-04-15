# some_list[start:ens:step]

first_list = [1, 2, 3, 4, 5]

print(first_list[1:]) #[2, 3, 4, 5]
print(first_list[3:]) #[4, 5]
print(first_list[-2:]) #[4, 5]

print(first_list[:2]) #[1, 2]
print(first_list[:4]) #[1, 2, 3, 4]
print(first_list[:-1]) #[1, 2, 3, 4]

print(first_list[2:4]) #[3, 4]

first_list2 = first_list[:]
print(first_list2 == first_list) #True
print(first_list2 is first_list ) #False

print(first_list[1::2]) #[2, 4]
print(first_list[2::-1]) #[3, 2, 1]

number = [1, 2, 3, 4, 5]
number[1::2] = ["a", "b"]
print(number)

geeting = ["good", "morning"]
#swap
geeting[0], geeting[1] = geeting[1], geeting[0]
print(geeting)
