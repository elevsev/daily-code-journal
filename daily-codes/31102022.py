from statsmodels.compat import lzip
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

prestige = sm.datasets.get_rdataset("Duncan", "carData", cache=True).data
print(prestige.head())

prestige_model = ols("prestige ~ income + education", data=prestige).fit()
print(prestige_model.summary())

fig = sm.graphics.influence_plot(prestige_model, criterion="cooks")
fig.tight_layout(pad=1.0)
fig