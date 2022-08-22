# normalise: rescale data between [0,1] - assumes no distribution
# standardise: centre distribution of random variable such that mean = 0, and standard deviation = 1

# normalise

def min_max(data):
    min_max = list()
    for i in range(len(data[0])):
        col_vals = [row[i] for row in data]
        min_val = min(col_vals)
        max_val = max(col_vals)
        min_max.append([min_val, max_val])

    return min_max

def normalise(data, min_max):
    for row in data:
        for i in range(len(row)):
            # scaled_value = (value - min) / (max - min)
            row[i] = (row[i] - min_max[i][0]) / (min_max[i][1] - min_max[i][0])


dataset = [[50, 30], [20, 90]]

print("Raw data:\n",dataset)

min_and_max = min_max(data=dataset)
print("Min and max of columns:\n",min_and_max)

normalise(data=dataset, min_max=min_and_max)

print("Normalised data:\n", dataset)



