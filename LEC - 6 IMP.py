'''
DAY - 6 :
'''


# Descriptive Stats

import pandas as pd   # Data Manipulation Library
import numpy as np    # Numerical computation Library

Data = pd.DataFrame({
    "Name":["Raj","Rahul","Jyoti","John","Rita"],
    "Age":[20,21,22,23,24],
    "Salary":[10000,20000,30000,40000,70000],
    "Region":["North","South","East","West","North"]
})

Data

# Method - 1 : Descriptive Stats

Data.describe(include = "all").T



# Method - 2 : Descriptive Stats

from collections import OrderedDict

Numerical_col = Data.select_dtypes(exclude = "object").columns
Catagorical_col = Data.select_dtypes(include = "object").columns

stats =[]

for i in Numerical_col :
  Numerical_stats = OrderedDict({
      "Feature": i,
      "Count": Data[i].count(),
      "Mean": Data[i].mean(),
      "Std": Data[i].std(),
      "Maximum": Data[i].max(),
      "Minimum": Data[i].min(),
      "Range" : Data[i].max() - Data[i].min(),
      "Q1": Data[i].quantile(0.25),
      "Q2": Data[i].quantile(0.50),
      "Q3": Data[i].quantile(0.75),
      "IQR": Data[i].quantile(0.75) - Data[i].quantile(0.25),
      "Variance": Data[i].var(),
      "Skewness": Data[i].skew(),
      "Kurtosis" : Data[i].kurtosis()
  })
  
  stats.append(Numerical_stats)
  report = pd.DataFrame(stats)

report


# One way Anova Technique : Single Factor Analysis
'''
Null Hypothesis : There is No Significant diffrence in mean of the experimental Sample
Alternative Hypothesis : There is a Significant difference in the mean of experimental Sample
'''

test_A = np.array([8,6,5,4,3,2,5,5,10,3])
test_B = np.array([6,7,8,5,3,6,7,7,4,3])
test_C = np.array([10,9,6,3,5,6,6,7,7,3])

from scipy.stats import f_oneway

f_value,p_value = f_oneway(test_A,test_B,test_C)

print(f"f value: {f_value} and p value: {p_value}")

if (p_value < 0.05 ):
  print("Reject Null Hypothesis")
else:
  print("Accpet Null Hypothesis")



# Installing Researchpy Library
!pip install Researchpy
