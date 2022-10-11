# map - use same set of steps on each item while storing the result

def square(number):
    return number * number

numbers_to_square = [1, 2, 3, 4]
squared =  map(square, numbers_to_square)

print(squared)
print(list(squared))
