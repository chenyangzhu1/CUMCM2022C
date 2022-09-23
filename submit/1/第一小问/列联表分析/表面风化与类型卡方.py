import math

import numpy as np
import pandas as pd
import scipy.stats as stats

table=np.zeros([2,2])
table[0,0]=12
table[0,1]=6
table[1,0]=12
table[1,1]=28

kafang,p,ziyoudu,pingshubiao=stats.chi2_contingency(table)

xinagguanxishu=math.sqrt(kafang/(kafang+58))
print("卡方值",kafang)
print("p值",p)
print("自由度",ziyoudu)
print("频数表",pingshubiao)
print("相关系数",xinagguanxishu)