import networkx as nx
import numpy as np
graph = nx.karate_club_graph()     # load the graph

#print(G.number_of_nodes() )           # how many nodes
#print(G.number_of_edges() )           # how many edges
#print(list(G.edges()) )               # all edges as a list of tuples
#print(list(G.edges())[:5]  )          # first 5 edges only
#print(G.nodes[0]["club"] )            # which group node 0 joined
#print(G.nodes[33]["club"] )    




# function to make a adjacency matrix
def to_adjacency_matrix(graph):
    n=graph.number_of_nodes()
    edges=list(graph.edges())
    A=np.zeros((n,n))
    for i,j in edges:
        A[i,j]=1
        A[j,i]=1
    return A      




A=to_adjacency_matrix(graph)
print(A)
#checks
print(A.shape)            # (34, 34)
print(A.sum())            # 156.0
print((A == A.T).all())   # True