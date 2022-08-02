import numpy as np
import scipy.stats
from scipy.stats import pearsonr
import matplotlib.pyplot as plt


class PearsonCorrelation:
    '''Calculates the pearson correlation from scratch'''
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        self.n = len(self.x)
        self.xm = sum(self.x) / self.n
        self.ym = sum(self.y) / self.n
        self.std_x = np.std(x)
        self.std_y = np.std(y)
        self.cov = sum((a - self.xm) * (b - self.ym) for (a,b) in zip(self.x, self.y)) / self.n

    def pearsons_correlation(self):
        numerator = self.cov
        denomenator = (self.std_x * self.std_y)
        self.r = numerator / denomenator
        return self.r

x_values = [2, 4, 6, 8, 10]
y_values = [0.2, 0.22, 0.9, 1.1, 1.15]


result = PearsonCorrelation(x=x_values, y=y_values)
print("X_mean:", result.xm, "Y_mean:",result.ym, "X_std:",result.std_x, "Y_std:",result.std_y, "Covariance: ", result.cov)
print("Calc Pearson: ", result.pearsons_correlation())
print("Scipy Pearson: ", pearsonr(x=x_values, y=y_values))
print("Np Pearson: ", np.corrcoef(x=x_values, y=y_values))

plt.scatter(x_values,y_values)
plt.show()