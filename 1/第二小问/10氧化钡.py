import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import scipy.stats as stats
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels as sm

data = pd.read_excel("表1表2整合.xlsx")

data = data.values

a = 12  # 无风化 高钾
b = 23  # 无风化 铅钡
c = 6  # 风化 高钾
d = 26  # 风化 铅钡

alist = [0, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 21]
blist = [20, 23, 24, 25, 29, 30, 31, 32, 33, 34, 35, 37, 39, 44, 45, 48, 49, 50, 51, 54, 56, 60, 63]
clist = [8, 11, 12, 14, 22, 28]
dlist = [1, 9, 10, 13, 19, 26, 27, 36, 38, 40, 41, 42, 43, 46, 47, 52, 53, 55, 57, 58, 59, 61, 62, 64, 65, 66]
#
# for i in range(data.shape[0]):
#     if(data[i,16]=="无风化" and data[i,18]=="高钾"):
#         a+=1
#         alist.append(i)
#     elif(data[i,16]=="无风化" and data[i,18]=="铅钡"):
#         b+=1
#         blist.append(i)
#     elif(data[i,16]=="风化" and data[i,18]=="高钾"):
#         c+=1
#         clist.append(i)
#     else:
#         d+=1
#         dlist.append(i)

ya = np.zeros(a)
yb = np.zeros(b)
yc = np.zeros(c)
yd = np.zeros(d)

idx = 10

for i in range(a):
    ya[i] = data[alist[i], idx]

for i in range(b):
    yb[i] = data[blist[i], idx]

for i in range(c):
    yc[i] = data[clist[i], idx]

for i in range(d):
    yd[i] = data[dlist[i], idx]

ya = np.sort(ya)
yb = np.sort(yb)
yc = np.sort(yc)
yd = np.sort(yd)


def self_JBtest(y):
    # 样本规模n
    n = y.size
    # for i in range(data.shape[0]):
    #     if(data[i,16]=="无风化"):
    #         n+=1
    y_ = y - y.mean()
    M2 = np.mean(y_ ** 2)

    skew = np.mean(y_ ** 3) / M2 ** 1.5
    krut = np.mean(y_ ** 4) / M2 ** 2

    #         wufenglist.append(i)
    #     else:
    #         m+=1
    #         fenglist.append(i)
    JB = n * (skew ** 2 / 6 + (krut - 3) ** 2 / 24)
    pvalue = 1 - stats.chi2.cdf(JB, df=2)
    print("JB检验：", stats.jarque_bera(y))
    return np.array([JB, pvalue])


self_JBtest(ya)
self_JBtest(yb)
self_JBtest(yc)
self_JBtest(yd)

print('基于中位数的levene test P值：', stats.levene(ya, yb, yc, yd, center='median').pvalue)

predata = np.zeros([67, 3])

predata[:, 0] = data[:, idx]

for i in range(67):
    if (data[i, 18] == "高钾"):
        predata[i, 2] = 0
    else:
        predata[i, 2] = 1
    if (data[i, 16] == "无风化"):
        predata[i, 1] = 0
    else:
        predata[i, 1] = 1

predata = pd.DataFrame(predata, columns=['氧化钡', '风化', '类型'])

model = ols("氧化钡 ~风化+类型+风化:类型", data=predata)
mydata = model.fit()
print(anova_lm(mydata))

gaojia=np.append(ya,yc)
self_JBtest(gaojia)

qianbei=np.append(yb,yd)
self_JBtest(qianbei)

gaojia=np.append(ya,yc)
qianbei=np.append(yb,yd)


fenghua=np.append(ya,yb)
wufenghua=np.append(yc,yd)

gaojianei1=ya
gaojianei2=yc

qianbeinei1=yb
qianbeinei2=yd

import scipy.stats as ss
from scipy.stats import ttest_ind
print(ss.ranksums(gaojia,qianbei))
print(ss.ranksums(qianbeinei1,qianbeinei2))

self_JBtest(gaojia)
self_JBtest(qianbei)

self_JBtest(qianbeinei1)
self_JBtest(qianbeinei2)