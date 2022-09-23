import pandas as pd

data = pd.read_excel("附件.xlsx", sheet_name="表单1")
data = data.values
a = 0  # 无风化 a
b = 0  # 无风化 b
c = 0  # 无风化 c
d = 0  # 风化 a
e = 0  # 风化 b
f = 0  # 风化 c

for i in range(data.shape[0]):
    if (data[i, 4] == "无风化" and data[i, 1] == "A"):
        a += 1
    elif (data[i, 4] == "无风化" and data[i, 1] == "B"):
        b += 1
    elif (data[i, 4] == "无风化" and data[i, 1] == "C"):
        c += 1
    elif(data[i, 4] == "风化" and data[i, 1] == "A"):
        d += 1
    elif(data[i, 4] == "风化" and data[i, 1] == "B"):
        e+=1
    else:
        f+=1
