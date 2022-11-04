from statsmodels.compat import lzip
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

prestige = sm.datasets.get_rdataset("Duncan", "carData", cache=True).data
prestige_model = ols("prestige ~ income + education", data=prestige).fit()
print(prestige_model.summary())
