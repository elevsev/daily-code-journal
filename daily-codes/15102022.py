import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.read_csv('https://raw.githubusercontent.com/susanli2016/Machine-Learning-with-Python/master/beef.csv', sep=',')
print(data.head())

ols_model = ols("Quantity ~ Price", data=data).fit()
print(ols_model.summary())