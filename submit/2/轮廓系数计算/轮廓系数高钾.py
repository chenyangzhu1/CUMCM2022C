import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics

data = pd.read_excel("高钾筛选后数据.xlsx")

data = data.values

data_array = data[:, 1:7]
model = AgglomerativeClustering(n_clusters=2, linkage='average')
mydata = data_array
y = data[:, 7]
print(model.fit_predict(data_array))
print(y)

print("轮廓系数高钾：", metrics.silhouette_score(data_array,model.fit_predict(data_array), metric='euclidean'))
