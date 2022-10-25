import numpy as np, pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt 
from scipy.stats import norm

ticker = 'PG'
data = pd.DataFrame()
data[ticker] = wb.DataReader(ticker, data_source='yahoo', start='2007-1-1')['Adj Close']
print(data)

log_returns = np.log(1 + data.pct_change())

data.plot()
plt.show()

log_returns.plot()
plt.show()