import random

numbers = []
for n in range(0,10):
    i = random.randint(1,30)
    numbers.append(i)

for number in numbers:
    if (number % 3) == 0:
        print(number, "Win!")
    elif (number % 5) == 0:
        print(number, "Win!")
    else:
        print( number, "Lose!")