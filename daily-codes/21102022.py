import numpy as np
import matplotlib.pyplot as plt

mean_revenue = 170
stdev_revenue = 20
iterations = 1000

forecasted_revenue = np.random.normal(loc=mean_revenue, scale=stdev_revenue, size=iterations)

print(forecasted_revenue.mean())
# print(forecasted_revenue.std())

plt.figure(figsize=(15,6))
plt.plot(forecasted_revenue)
plt.show()