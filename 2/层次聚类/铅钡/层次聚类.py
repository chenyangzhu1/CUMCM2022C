import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import MinMaxScaler

data=pd.read_excel("铅钡聚类情况.xlsx")

data=data.values

data_array =data[0:18,1:15]
model = AgglomerativeClustering(n_clusters=3,linkage='average')


# min_max_scalar = MinMaxScaler()
# data_scalar = min_max_scalar.fit_transform(data_array)
print(model.fit_predict(data_array))
# from scipy.cluster.hierarchy import linkage, dendrogram
# plt.figure(figsize=(20, 6))
# Z = linkage(data_scalar, method='ward', metric='euclidean')
# p = dendrogram(Z, 0)
# plt.show()
