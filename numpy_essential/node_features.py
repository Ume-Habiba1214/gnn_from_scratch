import numpy as np
edges = [(0,1), (0,3), (1,2), (1,3), (3,4)]
# adjancy matrix
n=max(max(u,v) for u,v in edges )+1
print(n)
A=np.zeros((n,n))
for u,v in edges:
    A[u,v]=1
    A[v,u]=1  # as it is symmetric matric and has un directed edges
print(A)



#  feature matrix
X=np.array( [[1,0],
                [0,1],
                [1,1],
                [2,0],
                [0,2]
                ])

H=A@X
print(H)


# Normalization
# Connect every node to itself. Then each node includes its own features in the sum
# Sums aren’t fair to compare. Divide by degree → take the average instead of the sum.
I=np.eye(n)
A_hat=A+I
H_self=A_hat@X  # self loop

deg = A_hat.sum(axis=1)        # degrees including self
print(deg)
D_inv = np.diag(1 / deg)       # 1/degree on the diagonal
print(D_inv)
H_mean=D_inv @ A_hat @ X              # average of node + neighbors

print(H_self)
print(H_mean)
D_inv_sqrt = np.diag(1 / np.sqrt(deg))
A_norm = D_inv_sqrt @ A_hat @ D_inv_sqrt
print(A_norm)
print(np.allclose(A_norm, A_norm.T))
