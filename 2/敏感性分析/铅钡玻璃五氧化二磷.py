import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler


data = pd.read_excel("铅钡筛选后数据.xlsx")

data = data.values

data_array = data[:, 1:5]
model = AgglomerativeClustering(n_clusters=3, linkage='average')
mydata = data_array
y = data[:, 5]
print(model.fit_predict(data_array))
anchor1 = [1, 19, 32]
anchor2 = [35]
anchor3 = [46, 42, 40]


idxlist1 = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
            31, 33, 34]

idxlist2 = [36, 37]

idxlist3 = [38, 39, 41, 43, 44, 45, 48, 47]

# idx=1 #
# idx=2   #提高50%  无变化
# idx=4    #提高50%  无变化
# idx=5    #提高50%  无变化
# idx=21    #提高50% 变化了

# idxlist=np.arange(35)
#
# idxlist=np.delete(idxlist,anchor1)


ylabel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
          2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

changesum = 0

# 可调参数
gaibianfudu = 10
zhelunzhibiaoxuhao = 2  # 用于选二氧化硅等 0表示二氧化硅  1表示氧化铅 2是五氧化二磷 3是氧化锶

print("种类1")
for idx in idxlist1:
    anchor_of_idx = 0  # 种类
    data = pd.read_excel("铅钡筛选后数据.xlsx")

    data = data.values

    data_array = data[:, 1:5]
    data_array_lat = data_array
    data_array_lat[idx, zhelunzhibiaoxuhao] = data_array_lat[idx, zhelunzhibiaoxuhao] * gaibianfudu

    model = AgglomerativeClustering(n_clusters=3, linkage='average')
    latlabel = model.fit_predict(data_array_lat)
    # print(latlabel)

    change = 1

    if (anchor_of_idx == 0):
        flag = 0
        if (latlabel[idx] == latlabel[anchor1[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor1[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor1[2]]):
            flag += 1
        if (flag >= 2):
            change = 0

    if (anchor_of_idx == 1):
        if (latlabel[idx] == latlabel[anchor2[0]]):
            change = 0

    if (anchor_of_idx == 2):
        flag = 0
        if (latlabel[idx] == latlabel[anchor3[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor3[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor3[2]]):
            flag += 1
        if (flag >= 2):
            change = 0
    changesum += change
    if (change == 1):
        print(idx)

print("种类2")
for idx in idxlist2:
    anchor_of_idx = 1  # 种类
    data = pd.read_excel("铅钡筛选后数据.xlsx")

    data = data.values

    data_array = data[:, 1:5]

    data_array_lat = data_array
    data_array_lat[idx, zhelunzhibiaoxuhao] = data_array_lat[idx, zhelunzhibiaoxuhao] * gaibianfudu

    model = AgglomerativeClustering(n_clusters=3, linkage='average')
    latlabel = model.fit_predict(data_array_lat)
    # print(latlabel)

    change = 1

    if (anchor_of_idx == 0):
        flag = 0
        if (latlabel[idx] == latlabel[anchor1[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor1[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor1[2]]):
            flag += 1
        if (flag >= 2):
            change = 0

    if (anchor_of_idx == 1):
        if (latlabel[idx] == latlabel[anchor2[0]]):
            change = 0

    if (anchor_of_idx == 2):
        flag = 0
        if (latlabel[idx] == latlabel[anchor3[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor3[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor3[2]]):
            flag += 1
        if (flag >= 2):
            change = 0
    changesum += change
    if (change == 1):
        print(idx)

print("种类3")
for idx in idxlist3:
    anchor_of_idx = 2  # 种类
    data = pd.read_excel("铅钡筛选后数据.xlsx")

    data = data.values

    data_array = data[:, 1:5]
    data_array_lat = data_array
    # print(data_array_lat)
    data_array_lat[idx, zhelunzhibiaoxuhao] = data_array_lat[idx, zhelunzhibiaoxuhao] * gaibianfudu

    model = AgglomerativeClustering(n_clusters=3, linkage='average')
    latlabel = model.fit_predict(data_array_lat)

    change = 1

    if (anchor_of_idx == 0):
        flag = 0
        if (latlabel[idx] == latlabel[anchor1[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor1[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor1[2]]):
            flag += 1
        if (flag >= 2):
            change = 0

    if (anchor_of_idx == 1):
        if (latlabel[idx] == latlabel[anchor2[0]]):
            change = 0

    if (anchor_of_idx == 2):
        flag = 0
        if (latlabel[idx] == latlabel[anchor3[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor3[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor3[2]]):
            flag += 1
        if (flag >= 2):
            change = 0
    changesum += change
    if (change == 1):
        print(idx)
print("改变量总和", changesum)
