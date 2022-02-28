# 20220211 已在vsc中跑通
# 邓老师提供的基建因子分析案例

import os
os.getcwd() #获得当前路径：'C:\\Users\\Thinkapd'
os.chdir('D:\\My docsify\\docs\\my_projects\\machine_learning\\factor_analysis\\sample') #修改为项目文件夹

import pandas as pd
import matplotlib.pyplot as plt
import warnings
from factor_analyzer import FactorAnalyzer
from sklearn.preprocessing import StandardScaler
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
import seaborn as sns
import numpy as np

warnings.filterwarnings("ignore")
scaler = StandardScaler()
plt.rcParams['font.family'] = 'Microsoft Yahei'

def init_color():
    from matplotlib.colors import LinearSegmentedColormap
    blue_red = ['#5A8AC6', '#82A6D4', '#ABC3E2', '#D3DFF0', # 蓝色 渐变
                '#FFFFFF', # 白色
                '#FBD8DA', '#FAB3B5', '#F98E90', '#F8696B'] # 红色 渐变
    cmap_blue_red = LinearSegmentedColormap.from_list('blue_red', blue_red)
    return cmap_blue_red


cmap_blue_red = init_color()

data = pd.read_excel('基建.xlsx', index_col=0, skiprows=9, header=None)
data.index = pd.to_datetime(data.index)
data.index.name='date'
data.columns = ['PPP项目数:总入库:同比',
                '地方财政支出:累计同比',
                '产量:挖掘机:当月同比',
                '产量:起重机:当月同比',
                '产量:内燃叉车:当月同比',
                '产量:混凝土机械:当月同比',
                '产量:水泥:累计同比',
                '产量:石油沥青:当月同比',
                '江淮汽车:产量:重卡:当月值:同比',
                '地方政府债务余额:专项债务:同比',
                '全国政府性基金支出:累计同比',
                '库存:主要钢材品种:合计:月:同比',
                '水泥价格指数:全国:月:同比',
                '中国玻璃价格指数:月:同比',
                '期货收盘价(连续):螺纹钢:月:同比']

mdata = data[(data.index > pd.to_datetime('2010-01-01')) & (data.index < pd.to_datetime('2021-11-01'))]
missing_stats = pd.DataFrame(mdata.isnull().mean(), columns=['missing_rate'])
mdata = mdata.interpolate(method='linear', limit_direction='forward')
to_remove_cols = missing_stats.query('missing_rate >= 0.3').index.tolist()
mdata = mdata.drop(columns=to_remove_cols, axis=1)

mdata = mdata[mdata.index >= pd.to_datetime('2013-01-01')]

# standardization 
scaler.fit(mdata)
mdata_scaled = scaler.transform(mdata)

chi_square_value, p_value = calculate_bartlett_sphericity(mdata_scaled)
print('chi_square_value is: ', round(chi_square_value,2), 'and p value is :', round(p_value, 4))
if p_value < 0.01:
    print("Barlett's Test Passed. ")

from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all, kmo_model = calculate_kmo(mdata_scaled)
print(round(kmo_model, 4))
if kmo_model > 0.6:
    print("KMO Test Passed. ")

fa = FactorAnalyzer(11, rotation=None)
fa.fit(mdata_scaled)
ev, v = fa.get_eigenvalues()

# 可视化
# plot 横轴是指标个数，纵轴是 ev 值
# scatter横轴是指标个数，纵轴是 ev 值
plt.scatter(range(1, mdata.shape[1]+1), ev)
plt.plot(range(1, mdata.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

fa = FactorAnalyzer(4, rotation="varimax")
fa.fit(mdata)

fa.loadings_

df_cm = pd.DataFrame(np.abs(fa.loadings_),index=mdata.columns)

fig,ax = plt.subplots(figsize=(5, 12))
sns.heatmap(df_cm, annot=True, cmap=cmap_blue_red, ax=ax)
# 设置y轴字体的大小
ax.tick_params(axis='x',labelsize=15)
ax.set_title("Factor Analysis",fontsize=12)
ax.set_ylabel("")

transformed_data = pd.DataFrame(fa.transform(mdata_scaled))



