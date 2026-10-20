import numpy as np
graph={
    0:[1,2],
    1:[0,2],
    2:[0,1,3],
    3:[2,4],
    4:[3,5],
    5:[4]
}

print(f"neighbors of 2 are {graph[2]}")


# function to make a adjacency matrix
def to_adjacency_matrix(graph):
    n=len(graph)
    A=np.zeros((n,n))
    for i,list_of_i in graph.items():
       for j in list_of_i:
           A[i,j]=1
    return A      

final_matrix=to_adjacency_matrix(graph)
print(final_matrix)


# function to make a degree matrix 
def to_degree_matrix(A):
    n=len(A)
    D=np.zeros((n,n))
    for i in range(n):
        D[i,i]=np.sum(A[i])
    return D


degree_matrix=to_degree_matrix(final_matrix)
print(degree_matrix)


def aggregate_neighbours(A):
    n=len(A)
    X=np.zeros((n,2))
    for i in range(n):
        X[i,0]=i
        X[i,1]=1

    multiplex_matrix=A@X
    return multiplex_matrix



aggregated=aggregate_neighbours(final_matrix)    
print(aggregated)
