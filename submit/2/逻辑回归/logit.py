# Create SVM classification object
import pandas as pd
from sklearn import metrics
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn import svm, linear_model

x=pd.read_excel("分类表格整理.xlsx")
x=x.values

y=pd.read_excel("分类表格结果.xlsx")
y=y.values
y=y.flatten()


x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1,train_size=0.7)


model=linear_model.LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

y_test_predict=model.predict(x_test)

p_test=precision_score(y_test,y_test_predict)
r_test=recall_score(y_test,y_test_predict)
f1_test=f1_score(y_test,y_test_predict)
print(p_test,r_test,f1_test)

# print(model.coef_)
# print(model.intercept_)

rocy=model.predict_proba(x_test)
# print(rocy)


x3=pd.read_excel("问题3数据.xlsx")
x3=x3.values
pro3pre=model.predict(x3)
print(pro3pre)

print(metrics.log_loss(y_test,y_test_predict))