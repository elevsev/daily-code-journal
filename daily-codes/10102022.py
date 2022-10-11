# reduce - applied to an iterable for the purposes of reducing it to a single cumulative value

from functools import reduce

def addition(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

numbers = [0, 1, 2, 3, 4]

print(reduce(addition, numbers))
