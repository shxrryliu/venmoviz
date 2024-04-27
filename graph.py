from friends import G
import networkx as nx
import matplotlib.pyplot as plt

# for user in users:
    # print(f"Username: {user.username}, First Name: {user.first_name}, Last Name: {user.last_name}")
    # G.add_node(user.username, first_name=user.first_name, last_name=user.last_name)
    # G.add_edge(starting_user, user)
    


# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=1)
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.axis('off')  # Turn off the axis
plt.show()  # Display the graph