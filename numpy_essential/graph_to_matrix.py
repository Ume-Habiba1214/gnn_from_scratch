""" undirected graph with 5 edges
0 - 1
0 - 3
1 - 2
1 - 3
3 - 4 """
import numpy as np


dictionary_of_graph={
    0:[1,3],
    1:[0,2,3],
    2:[1],
    3:[0,1,4],
    4:[3]
}
print(dictionary_of_graph)


matrix_of_graph=np.zeros((5,5))
matrix_of_graph[0,1]=1
matrix_of_graph[1,0]=1
matrix_of_graph[0,3]=1
matrix_of_graph[3,0]=1
matrix_of_graph[1,2]=1
matrix_of_graph[2,1]=1
matrix_of_graph[1,3]=1
matrix_of_graph[3,1]=1
matrix_of_graph[3,4]=1
matrix_of_graph[4,3]=1
print(matrix_of_graph)
size=matrix_of_graph.shape
print(size)


# Edges as list of tuples
edges=[(0,1),(0,3),(1,2),(1,3),(3,4)]
n = max(max(u, v) for u, v in edges) + 1
tuples_to_matrix=np.zeros((n,n))
for u,v in edges:
    tuples_to_matrix[u,v]=1
    tuples_to_matrix[v,u]=1

print(tuples_to_matrix)


# Matrix from dictionary
m=len(dictionary_of_graph)
dict_to_matrix=np.zeros((m,m))
for nodes, neighbours in dictionary_of_graph.items():
    for neighbour in neighbours:
        dict_to_matrix[nodes,neighbour]=1


print(dict_to_matrix)

#Undirected graph: A[u,v] = A[v,u] = 1, so the matrix is symmetric (A == A.T).
symmetry=(dict_to_matrix == dict_to_matrix.T).all() 
print(symmetry)