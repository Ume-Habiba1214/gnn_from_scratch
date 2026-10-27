import numpy as np

M=np.array([[1,2,3],
            [4,5,6],
            [7,3,4],
            [2,3,4]])

print(M)
print(M.shape)


matrix=np.zeros((6,2)) # create 2d array with zeros and np.empty((r,c)) creats 2d array with random values from the memory.
n=len(matrix)
print(n)
for i in range(n):
    matrix[i]=[i,1]

print(matrix)
print(matrix.shape)