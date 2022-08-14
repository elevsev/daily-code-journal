win = '''

█▄█ █▀█ █░█   █░█░█ █ █▄░█ █
░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█ ▄
'''

lose = '''

█▄█ █▀█ █░█   █░░ █▀█ █▀ █▀▀ █
░█░ █▄█ █▄█   █▄▄ █▄█ ▄█ ██▄ ▄
'''

loading1 = '''
Loading results…
█▒▒▒▒▒▒▒▒▒
'''
loading2 = '''
Loading results…
█████▒▒▒▒▒
'''
loading3 = '''
Loading results…
██████████
'''

loads = [loading1, loading2, loading3]

import numpy as np
import time

# inputs: range and guess

input_start = int(input("Choose a starting range: "))
input_end = int(input("Choose an ending range: "))
input_guess = int(input("Now, make your guess: "))
win_probability = round((1 / (input_end - input_start + 1)) * 100, 2)


def computer(start=input_start, end=input_end):
    random_guess = np.random.randint(low=start, high=end)
    return random_guess

computer_guess = computer()

print(f"Start: {input_start}, End: {input_end}\n\nYour probability of winning is {win_probability}%")

for load in loads:
    print(load)
    time.sleep(1)

print("-----------------------------------------------------------------")
print(f"Your guess: {input_guess} vs Computer's guess: {computer_guess}")
print("-----------------------------------------------------------------")

if input_guess == computer_guess:
    print(win)
else:
    print(lose)
