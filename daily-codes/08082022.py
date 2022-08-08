
one= """
 ________
/_______/|
|       ||
|   o   ||
|_______|/
"""
two= """
 ________
/_______/|
|   o   ||
|   o   ||
|_______|/
"""
three= """
 ________
/_______/|
|       ||
| o o o ||
|_______|/
"""
four= """
 ________
/_______/|
|  o o  ||
|  o o  ||
|_______|/
"""
five= """
 ________
/_______/|
| o o o ||
|  o o  ||
|_______|/
"""
six= """
 ________
/_______/|
| o o o ||
| o o o ||
|_______|/
"""

import numpy as np

random_n = np.random.randint(0,7)

def die_roll():
    roll = np.random.randint(0,7)
    if roll == 1:
        print(one)
    elif roll == 2:
        print(two)
    elif roll == 3:
        print(three)
    elif roll == 4:
        print(four)
    elif roll == 5:
        print(five)
    elif roll == 6:
        print(six)
    else:
        print("Error. Please roll again.")

die_roll()