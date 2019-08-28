import time
gen_start_time = time.time()
print(sum(n for n in range(1000000))) # generator expression

gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(1000000)])) #list comprehension

list_time = time.time() - list_start_time

print(f"generator expression took: {gen_time}")
print(f"list comprehension took: {list_time}")
