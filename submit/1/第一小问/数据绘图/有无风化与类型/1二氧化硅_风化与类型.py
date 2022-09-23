import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

idx = 1

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
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(np.arange(a), ya, color="blue", label="无风化 高钾")
# 无风化 高钾
plt.plot(np.arange(b), yb, color="green", label="无风化 铅钡")
# 无风化 铅钡
plt.plot(np.arange(c), yc, color="red", label="风化 高钾")
# 风化 高钾
plt.plot(np.arange(d), yd, color="black", label="风化 铅钡")
# 风化 铅钡


plt.legend()
plt.xlabel('排序号', fontsize=13)
plt.ylabel('二氧化硅(SiO2)',fontsize=13)
plt.show()
