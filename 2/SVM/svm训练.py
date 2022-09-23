# Create SVM classification object
import pandas as pd
import sklearn
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn import svm

x=pd.read_excel("分类表格整理.xlsx")
x=x.values

y=pd.read_excel("分类表格结果.xlsx")
y=y.values
y=y.flatten()


x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1,train_size=0.7)


model=svm.SVC(kernel='linear',random_state=1)
model.fit(x_train,y_train)

y_test_predict=model.predict(x_test)

p_test=precision_score(y_test,y_test_predict)
r_test=recall_score(y_test,y_test_predict)
f1_test=f1_score(y_test,y_test_predict)
print(p_test,r_test,f1_test)

