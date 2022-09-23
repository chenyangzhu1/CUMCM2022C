import math

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr
from scipy.stats import norm

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
z = pd.read_excel("高钾总表.xlsx")
z = z.values

data = z[:, :]

res = pd.DataFrame(data, columns=[
    '二氧化硅', '氧化钠', '氧化钾', '氧化钙', '氧化镁', '氧化铝', '氧化铁', '氧化铜', '氧化铅',
    '氧化钡', '五氧化二磷', '氧化锶', '氧化锡', '二氧化硫'], dtype=np.float)

corrgaojia = res.corr(method='pearson')
corrgaojia = corrgaojia.values
z = pd.read_excel("铅钡总表.xlsx")
z = z.values

data = z[:, :]

res = pd.DataFrame(data, columns=[
    '二氧化硅', '氧化钠', '氧化钾', '氧化钙', '氧化镁', '氧化铝', '氧化铁', '氧化铜', '氧化铅',
    '氧化钡', '五氧化二磷', '氧化锶', '氧化锡', '二氧化硫'], dtype=np.float)

corrqianbei = res.corr(method='pearson')

corrqianbei = corrqianbei.values
zpvalue = np.zeros([14, 14])

for i in range(14):
    for j in range(14):
        if (i != j):
            gaojia = corrgaojia[i, j]
            qianbei = corrqianbei[i, j]

            r1 = gaojia
            n1 = 18
            r2 = qianbei
            n2 = 49

            z1 = 0.5 * math.log((1 + r1) / (1 - r1))
            z2 = 0.5 * math.log((1 + r2) / (1 - r2))

            ddiff = z1 - z2
            SEddiff = math.sqrt(1 / (n1 - 3) + 1 / (n2 - 3))

            zvalue = ddiff / SEddiff
            pvalue = 2 * (1 - norm.cdf(abs(zvalue)))
            zpvalue[i, j] = pvalue
np.savetxt("z检验p值结果.csv",zpvalue,delimiter=',')
