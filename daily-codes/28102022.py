from cgi import print_directory
import numpy as np
import statsmodels.api as sm

nobs = 100
X = np.random.random((nobs, 2))
print(X[:5])
X = sm.add_constant(X)
print(X[:5])

beta = [1, .1, .5]
e = np.random.random(nobs)
y = np.dot(X, beta) + e

results = sm.OLS(y, X).fit()
print(results.summary())