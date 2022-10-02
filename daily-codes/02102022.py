import matplotlib.pyplot as plt 
import random


def random_plot(start=0, end=100, number=10_000):
    to_plot_i = []    
    to_plot_j = []

    for n in range(0,number):
        i = random.randint(start, end) ** random.randint(0, 100)
        j = random.randint(start, end) ** random.randint(0, 100)
        to_plot_i.append(i) 
        to_plot_j.append(j)

    plt.plot(to_plot_i, to_plot_j)
    plt.show()

random_plot()