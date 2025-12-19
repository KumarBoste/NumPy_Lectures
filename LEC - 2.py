'''
DAY - 2
'''
for i in range(1, 10, 1):
    print(i, end = " ")

[i for i in range(1, 10, 1)]

# numpy > list comprehension > for loop

# Identical Matrix
np.eye((3), dtype = int)

# create a matrix of 3,5
matrix = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
matrix.shape

matrix.sum(axis = 0) # sum of all the columns i.e 5

matrix.sum(axis = 1) # sum of all the rows i.e 3

'''
1. random.seed() is used for the stopping of the random integer
2. random.random() is used for the genration of random numbers
'''
np.random.seed(7) # reducibility
np.random.random((3,5))


# 7 rows and 9 columns
matrix = np.random.random((7,9))
matrix.reshape(1,63) # changing the shape of the array

matrix1 = np.random.random((1920, 1080))
matrix1.reshape(1920, 1080)


matrix2 = np.random.randint((4)) # it will generate any random number in between the given range
matrix2

import matplotlib.pyplot as plt
plt.figure(figsize = (5,5))
matrix3 = np.random.randint(0,256,(1920,1080,3)) # it will generate any random number
plt.imshow(matrix3[:,:,0])
plt.title("Image generation using numpy")
plt.tight_layout()
plt.show

# Generating normal distribution matrix
matrix4 = np.random.normal(loc = 0, scale = 1, size = (10,10))
matrix4

# Generating UNIFORM distribution matrix
matrix5 = np.random.uniform(low = 0, high = 1, size = (10,10))
matrix5



