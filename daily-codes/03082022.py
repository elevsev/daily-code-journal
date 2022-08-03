import numpy as np
import matplotlib.pyplot as plt


class RandomNumbers:
    def __init__(self, l, h, n):
        self.l = l
        self.h = h
        self.n = n

    def create_random_sample_x(self):
        self.x = np.random.randint(low=self.l, high=self.h, size=self.n)
        return self.x

    def create_random_sample_y(self):
        self.y = np.random.randint(low=self.l, high=self.h, size=self.n)
        return self.y

    def plot_random_numbers(self):
        plt.scatter(self.x, self.y)
        plt.gca().legend(('x','y'))
        plt.show()
        
rndm = RandomNumbers(l=0, h=10, n=20)
print(rndm.create_random_sample_x())
print(rndm.create_random_sample_y())


xy_plot = rndm.plot_random_numbers()