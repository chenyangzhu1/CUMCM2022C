import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['FangSong']

data = pd.read_excel("铅钡五氧化二磷.xlsx")

data = data.values

y = data[:, 0]

y = y.flatten()

x = np.zeros([5, y.shape[0]])
for i in range(5):
    x[i] = data[:, i + 1]


def fun(x, px11, px22, px33, pt1, pt2, px1, px2, px3, px12, px13, px23, px00):
    x1 = x[0, :]
    x2 = x[1, :]
    x3 = x[2, :]
    t1 = x[3, :]
    t2 = x[4, :]

    return px11 * x1 ** 2 + px22 * x2 ** 2 \
           + px33 * x3 ** 2 + pt1 * t1 + pt2 * t2 \
           + px1 * x1 + px2 * x2 + px3 * x3 + px12 * x1 * x2 \
           + px13 * x1 * x3 + px23 * x2 * x3 + px00


def funlin(x, pt1, pt2, px1, px2, px3, px00):
    x1 = x[0, :]
    x2 = x[1, :]
    x3 = x[2, :]
    t1 = x[3, :]
    t2 = x[4, :]
    return px1 * x1 + px2 * x2 + px3 * x3 + px00 + pt1 * t1 + pt2 * t2


popt, pcov = curve_fit(fun, x, y,method='trf')

px11, px22, px33, pt1, pt2, px1, px2, px3, px12, px13, px23, px00 = popt

y2 = np.zeros(y.shape[0])

former=[]
latter=[]


for i in range(y2.shape[0]):
    x1 = x[0, i]
    x2 = x[1, i]
    x3 = x[2, i]
    t1 = x[3, i]
    t2 = x[4, i]
    y2[i] = px11 * x1 ** 2 + px22 * x2 ** 2 + px33 * x3 ** 2 + pt1 * t1 + pt2 * t2 + px1 * x1 + px2 * x2 + px3 * x3 + px12 * x1 * x2 + px13 * x1 * x3 + px23 * x2 * x3 + px00
    if(t1==1 or t2==1):
        t1=0
        t2=0
        former.append(y[i])
        latter.append(px11 * x1 ** 2 + px22 * x2 ** 2 + px33 * x3 ** 2 + pt1 * t1 + pt2 * t2 + px1 * x1 + px2 * x2 + px3 * x3 + px12 * x1 * x2 + px13 * x1 * x3 + px23 * x2 * x3 + px00)


def __sst(y_no_fitting):
    """
    计算SST(total sum of squares) 总平方和
    :param y_no_predicted: List[int] or array[int] 待拟合的y
    :return: 总平方和SST
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list = [(y - y_mean) ** 2 for y in y_no_fitting]
    sst = sum(s_list)
    return sst


def __ssr(y_fitting, y_no_fitting):
    """
    计算SSR(regression sum of squares) 回归平方和
    :param y_fitting: List[int] or array[int]  拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 回归平方和SSR
    """
    y_mean = sum(y_no_fitting) / len(y_no_fitting)
    s_list = [(y - y_mean) ** 2 for y in y_fitting]
    ssr = sum(s_list)
    return ssr


def __sse(y_fitting, y_no_fitting):
    """
    计算SSE(error sum of squares) 残差平方和
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 残差平方和SSE
    """
    s_list = [(y_fitting[i] - y_no_fitting[i]) ** 2 for i in range(len(y_fitting))]
    sse = sum(s_list)
    return sse


def goodness_of_fit(y_fitting, y_no_fitting):
    """
    计算拟合优度R^2
    :param y_fitting: List[int] or array[int] 拟合好的y值
    :param y_no_fitting: List[int] or array[int] 待拟合y值
    :return: 拟合优度R^2
    """
    SSR = __ssr(y_fitting, y_no_fitting)
    SST = __sst(y_no_fitting)
    rr = SSR / SST
    return rr


print(goodness_of_fit(y2, y))


print(former)
print(latter)

ans=np.zeros([len(former),2])

ans[:,0]=np.array(former)
ans[:,1]=np.array(latter)
np.savetxt("铅钡五氧化二磷预测.csv",ans,delimiter=',')
print(popt)