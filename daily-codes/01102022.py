import matplotlib.pyplot as plt 
import random


def random_plot(start=0, end=100, number=10_000):
    to_plot = []    

    for n in range(0,number):
        i = random.randint(start, end) ** random.randint(0, 100)
        to_plot.append(i)

    plt.plot(to_plot)
    plt.show()

random_plot()