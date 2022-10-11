# for loop
from random import randint

result = []
items = range(0,5)
for item in items:
    new_item = randint(0,10)
    result.append(new_item)

print(result)

# list comprehension
list_comp_result = [randint(0,10) for i in range(0,5)]
print(list_comp_result)
