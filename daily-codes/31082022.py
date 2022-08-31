import matplotlib.pyplot as plt
import random

def roll_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)

    if die_1 == die_2:
        same_roll = True
    else:
        same_roll = False
    return same_roll

simulations = 10_000
max_rols = 1000
bet = 1

win_prob = []
end_balance = []

fig = plt.figure()
plt.title("Monte Carlo Dice Game [" + str(simulations) + " simulations]")
plt.xlabel("Roll Number")
plt.ylabel("Balance [$]")
plt.xlim([0, max_rols])

for i in range(simulations):
    balance = [1000]
    num_rolls = [0]
    num_wins = 0 

    while num_rolls[-1] < max_rols:
        same = roll_dice()

        if same:
            balance.append(balance[-1] + 4 * bet)
            num_wins += 1
        else:
            balance.append(balance[-1] - bet)
        num_rolls.append(num_rolls[-1] + 1)

    win_prob.append(num_wins / num_rolls[-1])
    end_balance.append(balance[-1])
    plt.plot(num_rolls, balance)



print(f"Average win after {simulations} simulations: {sum(win_prob) / len(win_prob)}")
print(f"Average balance: {sum(end_balance) / len(end_balance)}")

plt.show()
