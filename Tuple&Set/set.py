# Sets cannot have duplictes
s = set({1, 2, 3, 4, 5, 5, 5}) # {1, 2, 3, 4, 5}

# Creating a new set
s = set({1, 4, 5})

# Creates a set with the same values as above
s = {1, 4, 5}

4 in s # True
8 in s # False

# METHOD
# add
s = set([1, 2, 3])
s.add(4) # {1, 2, 3, 4}
s.add(4) # {1, 2, 3, 4}

# remove removes a value from the set - returns a KeyError if the value is not found
set1 = {1,2,3,4,5,6}
set1.remove(3)
print(set1) # {1, 2, 4, 5, 6}

# if you need to avoid KeyErrors use .discard()
set1.discard(1)
print(set1)

# copy
s = set([1,2,3])
another_s = s.copy()
another_s # {1, 2, 3}
another_s is s # False

# clear
s = set([1, 2, 3])
s.clear() # set()

# Math
# intersection
# symmetric_difference
# union
math_students = {"Matt", "Kitty", "John", "Oeei", "Jane", "Colt"}
biology_students = {"Oliver", "James", "John", "Matt", "Jane", "Helen"}

union = math_students | biology_students
intersection = math_students & biology_students

print(union)
print(intersection)

# Set Comprehension
print({x**2 for x in range(10)})
