from cProfile import label
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

def log_vs_norm(size=1000):
    x = random.logistic(size=size)
    y = random.normal(size=size)
    s = str(size)

    # print(s)

    plt.title("Logistic vs Normal, size: {}".format(s))
    plt.hist(x, label = "Logistic")
    plt.hist(y, label = "Normal")
    plt.legend()
    plt.show()

sizes = [10, 100, 1000, 10000]
for s in sizes:
    log_vs_norm(size=s)

