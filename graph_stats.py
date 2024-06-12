import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict
from data import data

# Parse and create edges directly from the data
edges = []
node_labels = {}  # Store labels for display
for line in data.strip().split("\n"):
    if line.startswith("Added"):
        parts = line.split()
        friend_username = parts[1]
        friend_display_name = parts[2].strip('()') + " " + parts[3].strip('()')
        connected_to_username = parts[-1].strip('.')
        edges.append((connected_to_username, friend_username))
        # Also gather display names for later usage
        node_labels[friend_username] = friend_display_name
        node_labels[connected_to_username] = connected_to_username  # Replace with actual display name if available

# Create the graph
G = nx.Graph()
G.add_edges_from(edges)

# Compute basic stats
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Find the node with the maximum degree
max_degree_node = max(G.degree, key=lambda x: x[1])
max_degree_node_name = node_labels[max_degree_node[0]]
max_degree = max_degree_node[1]

print(f"Total number of nodes: {num_nodes}")
print(f"Total number of edges: {num_edges}")
print(f"Node with the most connections: {max_degree_node_name} with {max_degree} connections")

# Choose a root node for layer calculation
root_node = 'Valerie-Jarrett-2' 

# Calculate the shortest path lengths from root_node to all other nodes
layer_counts = nx.single_source_shortest_path_length(G, root_node)

# Count the number of nodes in each layer
layer_distribution = {}
for node, layer in layer_counts.items():
    if layer in layer_distribution:
        layer_distribution[layer] += 1
    else:
        layer_distribution[layer] = 1

# Output the number of nodes per layer
for layer, count in sorted(layer_distribution.items()):
    print(f"Layer {layer}: {count} nodes")
