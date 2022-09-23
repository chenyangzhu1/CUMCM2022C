# Create SVM classification object
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn import svm, linear_model

x = pd.read_excel("分类表格整理.xlsx")
x = x.values

y = pd.read_excel("分类表格结果.xlsx")
y = y.values
y = y.flatten()

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.7)

model = linear_model.LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

# y_test_predict=model.predict(x_test)

# p_test=precision_score(y_test,y_test_predict)
# r_test=recall_score(y_test,y_test_predict)
# f1_test=f1_score(y_test,y_test_predict)
# print(p_test,r_test,f1_test)

# print(model.coef_)
# print(model.intercept_)

# rocy=model.predict_proba(x_test)
# print(rocy)


x3 = pd.read_excel("问题3数据.xlsx")
x3 = x3.values
# pro3pre = model.predict(x3)
# print(pro3pre)
#
# print(metrics.log_loss(y_test,y_test_predict))


truelabel = [0, 1, 1, 1, 1, 0, 0, 1]

"""
二氧化硅 12
氧化钠 0.24
氧化钾 0.168
氧化钙 0.702
氧化镁
氧化铝(Al2O3)	
氧化铁(Fe2O3)	
氧化铜(CuO)	
氧化铅(PbO)	
氧化钡(BaO)	
五氧化二磷(P2O5)	
氧化锶(SrO)	
氧化锡(SnO2)	
二氧化硫(SO2)

"""

idx = 2
zengliang = 12

deltalist = np.linspace(0, 100, 100)

losslist = []

for delta in deltalist:
    x3 = pd.read_excel("问题3数据.xlsx")
    x3 = x3.values
    myx = x3
    myx[:, idx] = myx[:, idx] + delta
    deltapre = model.predict(myx)
    deltapre_proba=model.predict_proba(myx)

    probabi=np.zeros([8])
    for i in range(8):
        probabi[i]=deltapre_proba[i,truelabel[i]]

    losslist.append(metrics.log_loss(truelabel, probabi))

plt.plot(deltalist,losslist)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('氧化钠增量值', fontsize=13)
plt.ylabel('logloss',fontsize=13)

plt.show()