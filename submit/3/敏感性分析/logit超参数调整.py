# Create SVM classification object
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

cidx = np.linspace(0.000001, 100, 300)
res = []

for t in cidx:
    model = linear_model.LogisticRegression(C=t)
    model.fit(x_train, y_train)
    y_test_predict = model.predict(x_test)
    deltapre_proba=model.predict_proba(x_test)

    probabi=np.zeros([21])
    for i in range(21):
        probabi[i]=deltapre_proba[i,y_test[i]]

    res.append(metrics.log_loss(y_test, probabi))


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.xlabel('c值序号', fontsize=13)
plt.ylabel('logloss',fontsize=13)
plt.plot(np.arange(300),res)
plt.show()


tidx=np.linspace(0.000001, 100, 300)
rest=[]
for t in tidx:
    model = linear_model.LogisticRegression(tol=t)
    model.fit(x_train, y_train)
    y_test_predict = model.predict(x_test)
    deltapre_proba=model.predict_proba(x_test)

    probabi=np.zeros([21])
    for i in range(21):
        probabi[i]=deltapre_proba[i,y_test[i]]

    rest.append(metrics.log_loss(y_test, probabi))

plt.plot(np.arange(300),rest)
plt.xlabel('tol值序号', fontsize=13)
plt.ylabel('logloss',fontsize=13)
plt.show()


# model=linear_model.LogisticRegression(max_iter=1000)
# model.fit(x_train,y_train)

# y_test_predict = model.predict(x_test)
#
# print(metrics.log_loss(y_test, y_test_predict))

# p_test=precision_score(y_test,y_test_predict)
# r_test=recall_score(y_test,y_test_predict)
# f1_test=f1_score(y_test,y_test_predict)
# print(p_test,r_test,f1_test)

# print(model.coef_)
# print(model.intercept_)

# rocy=model.predict_proba(x_test)
# print(rocy)


# x3=pd.read_excel("问题3数据.xlsx")
# x3=x3.values
# pro3pre=model.predict(x3)
# print(pro3pre)
