# import module 
import networkx as nx 
import matplotlib.pyplot as plt 

# graph created 
res = nx.barbell_graph(4, 2) 
nx.draw_networkx(res)
