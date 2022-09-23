import pandas as pd

data = pd.read_excel("附件.xlsx", sheet_name="表单1")
data=data.values
a = 0  # 无风化 高钾
b = 0  # 无风化 铅钡
c = 0  # 风化 高钾
d = 0  # 风化 铅钡

alist = []
blist = []
clist = []
dlist = []

for i in range(data.shape[0]):
    if (data[i, 4] == "无风化" and data[i, 2] == "高钾"):
        a += 1
        alist.append(i)
    elif (data[i, 4] == "无风化" and data[i, 2] == "铅钡"):
        b += 1
        blist.append(i)
    elif (data[i, 4] == "风化" and data[i, 2] == "高钾"):
        c += 1
        clist.append(i)
    else:
        d += 1
        dlist.append(i)
