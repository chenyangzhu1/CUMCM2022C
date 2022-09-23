import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel("表1表2整合.xlsx")

data = data.values

n = 32  # 风化对象个数
fenglist = [1, 8, 9, 10, 11, 12, 13, 14, 21, 24, 28, 29, 30, 38, 40, 42, 43, 44, 45, 48, 49, 54, 55, 57, 59, 60, 61, 63,
            64, 66, 67, 68]

m = 37  # 无风化对象个数
wufenglist = [0, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 31, 32, 33, 34, 35, 36, 37, 39, 41, 46,
              47, 50, 51, 52, 53, 56, 58, 62, 65]
# for i in range(data.shape[0]):
#     if(data[i,16]=="无风化"):
#         n+=1
#         wufenglist.append(i)
#     else:
#         m+=1
#         fenglist.append(i)


yfenghua = np.zeros(n)

ywufenghua = np.zeros(m)

idx = 1

for i in range(n):
    yfenghua[i] = data[fenglist[i], idx]

yfenghua = np.sort(yfenghua)

for i in range(m):
    ywufenghua[i] = data[wufenglist[i], idx]

ywufenghua = np.sort(ywufenghua)

plt.plot(np.arange(n), yfenghua)
plt.plot(np.arange(m), ywufenghua, color='red')

plt.show()
