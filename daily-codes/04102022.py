from cProfile import label
import matplotlib.pyplot as plt
from typing import Callable

xs = range(-10, 11)

def square(x):
    return x ** 2

def derivative_sq(x):
    return 2 * x

def difference_quotient(f: Callable[[float], float], x, h):
    return (f(x + h) - f(x)) / h 

actuals = [derivative_sq(x=x) for x in xs]
estimates = [difference_quotient(f=square, x=x, h=0.001) for x in xs]

plt.title('Actual vs Estimate')
plt.plot(xs, actuals, 'rx', label='Actual')
plt.plot(xs, estimates, 'b+', label='Estimates')
plt.plot(xs, label='X')

plt.show()