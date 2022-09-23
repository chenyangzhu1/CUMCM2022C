import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr

plt.rcParams['font.sans-serif'] = ['FangSong']
plt.rcParams['axes.unicode_minus'] = False
z = pd.read_excel("铅钡总表.xlsx")
z = z.values

data = z[:, :]

res = pd.DataFrame(data, columns=[
    '二氧化硅', '氧化钠', '氧化钾', '氧化钙', '氧化镁', '氧化铝', '氧化铁', '氧化铜', '氧化铅',
    '氧化钡', '五氧化二磷', '氧化锶', '氧化锡', '二氧化硫'], dtype=np.float)

corr = res.corr(method='pearson')

sns.heatmap(corr, annot=True, vmax=1, vmin=-1, xticklabels=True, yticklabels=True,
            square=True, cmap="RdYlGn",annot_kws={"fontsize":7}).get_figure().savefig("temp.png",dpi=500,bbox_inches = 'tight')

# plt.show()


name = ['二氧化硅', '氧化钠', '氧化钾', '氧化钙', '氧化镁', '氧化铝', '氧化铁', '氧化铜', '氧化铅',
        '氧化钡', '五氧化二磷', '氧化锶', '氧化锡', '二氧化硫']

# print(pearsonr(res['过滤阻力'], res['透气性']))

matriccor=np.zeros([14,14])
for n in range(14):
    for m in range(n + 1, 14):
        # print(name[n],name[m])
        # print(pearsonr(res[name[n]], res[name[m]]))
        _,pvalue=pearsonr(res[name[n]], res[name[m]])
        matriccor[n,m]=pvalue

np.savetxt("铅钡热图p值.csv",matriccor,delimiter=',')