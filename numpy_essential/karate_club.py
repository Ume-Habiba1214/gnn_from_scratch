import networkx as nx
G = nx.karate_club_graph()     # load the graph

print(G.number_of_nodes() )           # how many nodes
print(G.number_of_edges() )           # how many edges
print(list(G.edges()) )               # all edges as a list of tuples
print(list(G.edges())[:5]  )          # first 5 edges only
print(G.nodes[0]["club"] )            # which group node 0 joined
print(G.nodes[33]["club"] )     