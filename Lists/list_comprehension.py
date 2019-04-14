num = [1,2,3]

ten_times_num = [ x* 10 for x in num]

print(num)
print(ten_times_num)

name = "hello"

print([char.upper() for char in name])

firends = ["alex", "jason", "peter"]

print([name[0].upper() + name[1:] for name in firends])

numbers = [1,2,3,4,5,6]

even = [num for num in numbers if num%2 == 0]
odd = [num for num in numbers if num%2 == 1]
print(even, odd)

print([num*2 if num%2 == 0 else num/2 for num in numbers])

with_vowels = "this is fun hahaha"

remove_vowels = "".join(char for char in with_vowels if char not in "aeiou")
print(with_vowels, remove_vowels)

print([[i for i in range(0,10)] for num in range(0,10)] )