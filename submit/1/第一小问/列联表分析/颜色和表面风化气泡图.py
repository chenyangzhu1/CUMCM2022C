import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_excel("颜色排序.xlsx")
data = data.values

x = data[:, 4]
y = data[:, 3]

# print(stats.pointbiserialr(x, y))
# y是颜色
# x是二值


mydata = {'x': y, 'y': x}

df=pd.DataFrame(mydata)
my_mean=df.groupby('y')['x'].mean()

r_pb = 2*(my_mean[1]-my_mean[0])/(df.shape[0])

print(r_pb)

plotx = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
ploty = np.array([1, 2, 3, 4, 5, 6, 7, 1, 3, 4, 5, 7, 8])
z = np.zeros(13)

for i in range(54):
    if (x[i] == 0 and y[i] == 1):
        z[0] += 1
    elif (x[i] == 0 and y[i] == 2):
        z[1] += 1
    elif (x[i] == 0 and y[i] == 3):
        z[2] += 1
    elif (x[i] == 0 and y[i] == 4):
        z[3] += 1
    elif (x[i] == 0 and y[i] == 5):
        z[4] += 1
    elif (x[i] == 0 and y[i] == 6):
        z[5] += 1
    elif (x[i] == 0 and y[i] == 7):
        z[6] += 1
    elif (x[i] == 1 and y[i] == 1):
        z[7] += 1
    elif (x[i] == 1 and y[i] == 3):
        z[8] += 1
    elif (x[i] == 1 and y[i] == 4):
        z[9] += 1
    elif (x[i] == 1 and y[i] == 5):
        z[10] += 1
    elif (x[i] == 1 and y[i] == 7):
        z[11] += 1
    elif (x[i] == 1 and y[i] == 8):
        z[12] += 1
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('表面是否风化（0为无风化，1为风化）', fontsize=13)
plt.ylabel('颜色（从1至8依次加深）', fontsize=13)

plt.scatter(plotx, ploty, s=250 * z, alpha=0.5)
plt.xlim(-1, 2)
plt.ylim(0, 9)
plt.show()
