import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics


data = pd.read_excel("铅钡筛选后数据.xlsx")

data = data.values

data_array = data[:, 1:5]
model = AgglomerativeClustering(n_clusters=3, linkage='average')
mydata = data_array
y = data[:, 5]
print(model.fit_predict(data_array))

print("轮廓系数铅钡：", metrics.silhouette_score(data_array,model.fit_predict(data_array), metric='euclidean'))
