from one_friend import social_network_graph
import networkx as nx

# Output statistics about the graph
print("Number of nodes:", social_network_graph.number_of_nodes())
print("Number of edges:", social_network_graph.number_of_edges())
print("Average degree of connectivity:", sum(dict(social_network_graph.degree()).values()) / float(social_network_graph.number_of_nodes()))
# print("Density:", nx.density(social_network_graph))
# print("Centrality:", nx.degree_centrality(social_network_graph))
# print("Betweeness Centrality:", nx.betweenness_centrality(social_network_graph))
# print("Closeness centrality:", nx.closeness_centrality(social_network_graph))