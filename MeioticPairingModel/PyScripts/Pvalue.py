import numpy as np
from statsmodels.stats.proportion import proportions_ztest
stat, pval = proportions_ztest(count=np.array([133,154]),
                               nobs=np.array([200, 200]),
                               alternative='two-sided',
                               prop_var=False
                              )
print (stat, pval)
