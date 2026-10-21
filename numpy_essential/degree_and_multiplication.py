import numpy as np

# Edges as list of tuples
edges=[(0,1),(0,3),(1,2),(1,3),(3,4)]
n = max(max(u, v) for u, v in edges) + 1
matrix= np.zeros((n,n))
for u,v in edges:
    matrix[u,v]=1
    matrix[v,u]=1

print(matrix)

degree_vector=matrix.sum(axis=1)  
degree_matrix_one_line=np.diag(degree_vector) # vector → matrix with it on the diagonal



def multiplication_of_matrix(matrix):
    multiplex=matrix@matrix
    return multiplex

def degree_matrix(matrix):
    n=len(matrix)
    degree=np.zeros((n,n))
    for i in range(n):
        degree[i,i]=np.sum(matrix[i])

    return degree




print(degree_matrix(matrix))
print((degree_matrix_one_line==degree_matrix(matrix)).all())
print(multiplication_of_matrix(matrix))