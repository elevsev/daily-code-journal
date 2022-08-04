import math

class Poisson:
    def __init__(self, x):
        self.x = x[0]
        self.x_all = x
        self.m = sum(self.x_all) / len(self.x_all)

    def factorial(self):
        self.x_factorial = 1
        for i in self.x_all:
            self.x_factorial *= i
        return self.x_factorial

    def poisson(self):
        '''
        Creates the output of a poisson distribution
        P(x) = (e**-m * m**x) / (x!)
        '''
        self.p_x = (math.e ** (-self.m) * self.m ** (self.x)) / self.factorial()
        return self.p_x


# from math import factorial


x_values = [1, 2, 3]    

result = Poisson(x=x_values)
print("X: ",result.x)
print("E(X): ",result.m)
print("All x values: ", result.x_all)
print("X factorial: ",result.factorial())

print("P(X): ",result.poisson())