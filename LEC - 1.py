'''
DAY - 1
'''

# Numpy : Numerical Python
import numpy as np


# Creating an one dimensional Array
one_darray = [1,2,3,4] # List of array
print(type(one_darray))

numpy_one_darray = np.array(one_darray) # converting list into numpy array
print(type(numpy_one_darray)) # type of numpyarray

print(numpy_one_darray.ndim) # shows dimensions
print(numpy_one_darray.shape) # shows the shape of the numpyarray
print(numpy_one_darray.size)

numpy_two_darray = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(numpy_two_darray.ndim)
print(numpy_two_darray.shape)
numpy_two_darray

numpy_three_darray = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(type(numpy_three_darray))
print(numpy_three_darray.ndim)
print(numpy_three_darray.shape)
numpy_three_darray

np.ones(6,dtype = int)

np.ones((3,3),dtype = int) # identity matrix

np.zeros(5, dtype = int)

np.zeros((3,3), dtype = int) # we change it to INTEGER because the by default datatype is FLOAT

# Multiplication of two metrices
a = np.array([[2,2],[4,2]])
b = np.array([[4,4],[2,2]])
answer_two_darray = a * b
print(answer_two_darray)

# Multiplication of Three Metrices
c = np.array([[3,4,5],[5,4,3]])
d = np.array([[6,7,8],[8,7,6]])
ans = c * d
print(ans)

b.transpose()
print(answer_two_darray.transpose())
# numpy is vectorized form of array built on the top of the list which fastens the computational operations

# ARRANGE
num = np.arange(1,100)
print(num)

# ARRANGE (start, stop, step)
nums1 = np.arange(1, 100, 2)
print(nums1)

#linspace (start, stop, division of step)
num1 = np.linspace(1,100,100, dtype = int)
print(num1)
