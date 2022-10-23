import numpy as np
import matplotlib.pyplot as plt

mean_revenue = 170
stdev_revenue = 20
iterations = 1000

forecasted_revenue = np.random.normal(loc=mean_revenue, scale=stdev_revenue, size=iterations)

# plt.figure(figsize=(15,6))
# plt.plot(forecasted_revenue)
# plt.show()

prop_of_rev_from_cogs = 0.6
cog_std = 0.1
# assume that the proportion of revenue that comes from cost of goods sold (COGS) is 60%
cost_of_goods_sold = -1 * forecasted_revenue * np.random.normal(loc=prop_of_rev_from_cogs, scale=cog_std)

print(cost_of_goods_sold.mean())
print(cost_of_goods_sold.std())

plt.figure(figsize=(15,6))
plt.plot(cost_of_goods_sold)
plt.show()