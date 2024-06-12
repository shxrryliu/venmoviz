import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from data import data

# Parse and create edges directly from the data
edges = []
nodes = set()
for line in data.strip().split("\n"):
    if line.startswith("Added"):
        parts = line.split()
        friend = parts[1]
        source = parts[-1].strip('.')
        edges.append((source, friend))
        nodes.update([source, friend])

# Create graph and add edges
G = nx.Graph()
G.add_edges_from(edges)

# Remove isolated nodes
isolated = list(nx.isolates(G))
G.remove_nodes_from(isolated)

# Improved visualization
pos = nx.spring_layout(G, scale=2)
plt.figure(figsize=(20, 10))  # Increase figure size to improve readability
nx.draw(G, pos, node_color='lightblue', with_labels=True, node_size=30, font_size=6)
plt.title("Political Connections Network")
plt.show()
