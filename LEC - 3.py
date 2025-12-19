'''
DAY - 3
'''

# Create Matrix of 6,5
matrix6 = np.random.random((6,5))
matrix7 = matrix6.T    # Transpose of Matrix6
matrix7

# Example of Slicing 
# Create a matrix a of shape 4,5
a = np.array([[1,2,3,4,5],
             [6,7,8,9,10],
             [11,12,13,14,15],
             [16,17,18,19,20]])


a[1:3,1:4]
a[2:,3:]


# Using Aggrgate Function

print(matrix6.sum())
print(matrix6.max())
print(matrix6.min())
print(matrix6.mean())
print(matrix6.flatten())  # Converting 2D into 1D


# converting 3D numpy array to 1D numpy array 

b = np.random.random((1,3,3))
b.flatten()  # converting 3D into 1D


# Assignment Problems  website : scipy documentation
# Resource Allocation using Scipy



