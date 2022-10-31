import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
from statsmodels.formula.api import logit

dta = sm.datasets.fair.load_pandas().data
dta["affair"] = (dta["affairs"] > 0).astype(float)
print(dta.head(10))
affair_mod = logit(
    "affair ~ occupation + educ + occupation_husb"
    "+ rate_marriage + age + yrs_married + children"
    " + religious",
    dta,
).fit()

print(affair_mod.summary())