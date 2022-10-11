# filter - extract items from iterable given a condition

from turtle import pos


numbers = [-2, -1, 0, 1, 2]

positives = filter(lambda n: n > 0, numbers)
print(positives)
print(list(positives))