import math
# import numpy as np
# standardise: rescale such that mean = 0, and stdev = 1, assumes a normal distribution

dataset = [[50, 30], [20, 90], [30, 50]]
# x1 = [50, 20, 30]
# x2 = [30, 90, 50]

print(dataset)

# standardisation = (value_i - mean) / stdev
def mean(data):
    means = [0 for i in range(len(data[0]))] 
    # [0,0]
    for i in range(len(data[0])):
        col_vals = [row[i] for row in data]
        means[i] = sum(col_vals) / len(data)
    return means

def stdev(data, means):
    stdevs = [0 for i in range(len(data[0]))]
    for i in range(len(data[0])):
        var = [pow(row[i] - means[i], 2) for row in data]
        stdevs[i] = sum(var)
    stdevs = [math.sqrt(x/float(len(data) - 1)) for x in stdevs]
    return stdevs

mean_data = mean(data=dataset)
stdev_data = stdev(data=dataset, means=mean_data)

print(f'Mean: {mean_data}')
print(f'Std Dev: {stdev_data}')

def standardise(data, means, stdevs):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i] - means[i]) / stdevs[i]


standardise(data=dataset, means=mean_data, stdevs=stdev_data)
print(dataset)
