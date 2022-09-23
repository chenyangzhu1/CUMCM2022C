import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler


data = pd.read_excel("高钾筛选后数据.xlsx")

data = data.values

data_array = data[:, 1:7]
model = AgglomerativeClustering(n_clusters=2, linkage='average')
mydata = data_array
y = data[:, 7]
print(model.fit_predict(data_array))
anchor1 = [2,5,7]
anchor2 = [16,13,12]


idxlist1 = [0,1,3,4,6,8]

idxlist2 = [9,10,11,14,15,17]

# idxlist3 = [38, 39, 41, 43, 44, 45, 48, 47]

# idx=1 #
# idx=2   #提高50%  无变化
# idx=4    #提高50%  无变化
# idx=5    #提高50%  无变化
# idx=21    #提高50% 变化了

# idxlist=np.arange(35)
#
# idxlist=np.delete(idxlist,anchor1)


# ylabel = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2,
#           2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

changesum = 0

# 可调参数
gaibianfudu = 1.2
zhelunzhibiaoxuhao = 3
# 0              1             2            3                 4          5
#二氧化硅(SiO2)	氧化钾(K2O)	氧化钙(CaO)	氧化铝(Al2O3)	氧化铜(CuO)	氧化锡(SnO2)

print("种类1")
for idx in idxlist1:
    anchor_of_idx = 0  # 种类
    data = pd.read_excel("高钾筛选后数据.xlsx")

    data = data.values

    data_array = data[:, 1:7]

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
        flag = 0
        if (latlabel[idx] == latlabel[anchor2[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor2[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor2[2]]):
            flag += 1
        if (flag >= 2):
            change = 0
    changesum += change
    if (change == 1):
        print(idx)

print("种类2")
for idx in idxlist2:
    anchor_of_idx = 1  # 种类
    data = pd.read_excel("高钾筛选后数据.xlsx")

    data = data.values

    data_array = data[:, 1:7]

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
        flag = 0
        if (latlabel[idx] == latlabel[anchor2[0]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor2[1]]):
            flag += 1
        if (latlabel[idx] == latlabel[anchor2[2]]):
            flag += 1
        if (flag >= 2):
            change = 0
    changesum += change
    if (change == 1):
        print(idx)

print("改变量总和", changesum)
print("指标",1-changesum/12)
