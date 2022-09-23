import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import scipy.stats as stats
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels as sm

data = pd.read_excel("铅钡聚类情况.xlsx")
data = data.values

predata = np.zeros([data.shape[0], 15])

for i in range(14):
    predata[:, i] = data[:, i + 1]

predata[:,14]=data[:,16]

predata = pd.DataFrame(predata, columns=[
    '二氧化硅', '氧化钠', '氧化钾', '氧化钙', '氧化镁', '氧化铝', '氧化铁', '氧化铜', '氧化铅',
    '氧化钡', '五氧化二磷', '氧化锶', '氧化锡', '二氧化硫','种类'])

model = ols("二氧化硅 ~种类", data=predata)
mydata = model.fit()
print("二氧化硅")
print(anova_lm(mydata))

model = ols("氧化钠 ~种类", data=predata)
mydata = model.fit()
print("氧化钠")
print(anova_lm(mydata))

model = ols("氧化钾 ~种类", data=predata)
mydata = model.fit()
print("氧化钾")
print(anova_lm(mydata))

model = ols("氧化钙 ~种类", data=predata)
mydata = model.fit()
print("氧化钙")
print(anova_lm(mydata))

model = ols("氧化镁 ~种类", data=predata)
mydata = model.fit()
print("氧化镁")
print(anova_lm(mydata))

model = ols("氧化铝 ~种类", data=predata)
mydata = model.fit()
print("氧化铝")
print(anova_lm(mydata))

model = ols("氧化铁 ~种类", data=predata)
mydata = model.fit()
print("氧化铁")
print(anova_lm(mydata))

model = ols("氧化铜 ~种类", data=predata)
mydata = model.fit()
print("氧化铜")
print(anova_lm(mydata))

model = ols("氧化铅 ~种类", data=predata)
mydata = model.fit()
print("氧化铅")
print(anova_lm(mydata))

model = ols("氧化钡 ~种类", data=predata)
mydata = model.fit()
print("氧化钡")
print(anova_lm(mydata))

model = ols("五氧化二磷 ~种类", data=predata)
mydata = model.fit()
print("五氧化二磷")
print(anova_lm(mydata))

model = ols("氧化锶 ~种类", data=predata)
mydata = model.fit()
print("氧化锶")
print(anova_lm(mydata))

model = ols("氧化锡 ~种类", data=predata)
mydata = model.fit()
print("氧化锡")
print(anova_lm(mydata))

model = ols("二氧化硫 ~种类", data=predata)
mydata = model.fit()
print("二氧化硫")
print(anova_lm(mydata))
