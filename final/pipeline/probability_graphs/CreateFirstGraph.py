import json
import networkx as nx
from networkx.readwrite import json_graph
import time
import GraphLoader
import random
import numpy as np

G = GraphLoader.load_page_subgraph()

for current in G.nodes:
    edges = G.edges(current, data=True)
    edges = [(u,v,d) for (u,v,d) in edges if u != v]
    views = {current : G.nodes[current]['attr_data']['page_views']}
    total = G.nodes[current]['attr_data']['page_views'] + sum([G.nodes[neighbour]['attr_data']['page_views'] for (_, neighbour, _) in edges])

    [attributes.update({'p': G.nodes[neighbour]['attr_data']['page_views']/total}) for (_, neighbour, attributes) in edges]
    G.nodes[current]['attr_data']['p_exit'] = G.nodes[current]['attr_data']['page_views']/total

print(G.edges(data=True))




# rands = np.random.rand(len(edges) + 1)
# probs = (rands / np.sum(rands)).tolist()
# [d.update({'p':probs.pop()}) for (u,v,d) in edges]
# G.nodes[n]['attr_data']['p_exit'] = probs.pop()

