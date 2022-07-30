# creating a normal distribution
# N ~ (0,1)
# Z = (x - mu)/std_dev

import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

class NormalDistribution:
    '''Class: creates the mean, std, z-score, and probability density function for a list of values'''
    def __init__(self, x):
        self.x = x 
        self.mu = np.mean(self.x)
        self.std_dev = np.std(self.x)

    def z_score(self):
        self.z_score = (self.x - self.mu)/self.std_dev
        return self.z_score

    def normal_distribution(self):
        self.probability_density = (np.pi * self.std_dev) * np.exp(-0.5* ((self.x - self.mu) / self.std_dev) ** 2)
        return self.probability_density

z = NormalDistribution(x=x)
z_scores = z.z_score()
z_dist = z.normal_distribution()

print("Mean: ", z.mu)
print("Std: ",z.std_dev)
print("Z-scores: ", z_scores)


plt.plot(z_dist)
plt.show()