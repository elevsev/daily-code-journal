from random import randint


# numbers = randint(a=1, b=30)
number = int(randint(a=1, b=30))

# for number in numbers:
if (number % 3) == 0:
    print(number, "You're on holiday!")
else:
    print(number, "You should holiday!")