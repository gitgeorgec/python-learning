# return all

collections=[1,2,3,4,"a","b","c"]

is_collections_string = [type(s) == str for s in collections] # [false, false, false, true, true, true]

print(all(is_collections_string)) #false

print(any(is_collections_string)) #true
