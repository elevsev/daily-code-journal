import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/susanli2016/Machine-Learning-with-Python/master/beef.csv', sep=',')
print(df.head())

print(df.groupby(['Year']).sum())
print(df.describe().T)
