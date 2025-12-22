'''
DAY - 4
'''

# one sample t test
import numpy as np
from scipy import stats
''''
Null Hypothesis: The mean of the sample is equal to the known population mean
Alternative Hypothesis: The mean of the sample is not equal to the known population mean
'''
samples = np.array([2,5,7,9,10,11,14,17,19,21,24,27])
t_test, p_test = stats.ttest_1samp(samples, popmean  = 15)
print(f"t test value: {t_test} and p value : {p_test}")
alpha = 0.05
if (p_test < alpha):
    print("Accept Alternative Hypothesis")
else:
    print("Accept Null Hypothesis")



# Two sample t test
'''
Null Hypothesis: The mean of two samples are equal 
ALternative Hypothesis:- The mean of the two samples are not equal
'''

teaching_methodA = np.array([30,40,50,60,70,80,35,38,49,59])
teaching_methodB = np.array([65,78,79,46,38,21,13,80,80,90])
t_tesr, p_value = stats.ttest_ind(teaching_methodA, teaching_methodB, equal_var = True)
alpha = 0.05
print(f"t_test value is: {t_test} and p_value is: {p_value}")
if (p_value < alpha):
    print("Accept Alternative Hypothesis...")
else:
    print("Accept Null Hypothesis...")
