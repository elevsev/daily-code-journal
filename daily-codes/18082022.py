import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets

iris = datasets.load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# print(df.head())


X = df.drop('target', axis=1)
y = df.target


def minkowski_distance(a, b, p=1):
    dimensions = len(a)
    distance = 0
    for dimension in range(dimensions):
        distance += abs(a[dimension] - b[dimension]) ** p

    distance = distance ** (1 / p)

    return distance

print(f"Minkowski distance between row 1 and 2: {minkowski_distance(a=X.iloc[0], b=X.iloc[1])}")
