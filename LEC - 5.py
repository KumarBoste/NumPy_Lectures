'''
DAY - 5 :
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)
data = np.random.normal(loc=0, scale=5, size=10)

df = pd.DataFrame(data)

sns.kdeplot(df)
plt.axvline(0, linestyle='--', color='orange')
plt.show()


from scipy import stats
data = np.array([2,4,6,8,10,12,14,16,18,20,90])
# z = ( x - mean ) / std
mean = data.mean()
std = data.std()

print(f'mean of data is {mean} and standard deviation is {std}') 

print(stats.zscore(data))


# Detect Outliear using Z score
# Zscore value  > 3 then the data point is considered as Outlier

data[np.abs(stats.zscore(data )) > 3 ]


# Q . 
data1 =np.array ([100,200,400,60,700,600,300,500,900,1400,1900])

data1[stats.zscore(data1) > 3] 

