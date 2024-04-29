# used venmo_api with the below example (in untracked file called tokens)
# from venmo_api import Client

# client = Client.get_access_token(username='', password='', device_id="-")
# access_token = '-'
# client = Client(access_token=access_token)

import time

import scipy
from tokens import client
import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from collections import defaultdict, deque

def check_political_figure(name):
    formatted_name = name.replace(' ', '_')
    url = f"https://en.wikipedia.org/wiki/{formatted_name}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract main text from the Wikipedia page
        text_content = soup.get_text().lower()
        # List of political keywords to look for
        political_keywords = ['politician', 'White House', 'senator', 'congress', 'political party', 'election', 'ambassador', 'legislature', 'government', 'Obama', 'cabinet', 'public policy']
        # Check if any of the political keywords are in the page content
        if any(keyword in text_content for keyword in political_keywords):
            return True
    return False

def crawl_friends_with_priority(client, starting_users, max_depth):
    G = nx.Graph()
    visited = set()
    queue = deque([(user, 0) for user in starting_users])  # Queue to manage the crawl
    friend_connections = defaultdict(set)

    while queue:
        current_user, current_depth = queue.popleft()
        if current_depth < max_depth:
            time.sleep(60)  # Sleep to adhere to rate limiting
            friends = client.user.get_user_friends_list(user_id=current_user)
            for friend in friends:
                friend_id = friend.username
                friend_connections[friend_id].add(current_user)  # Track connections
                if friend_id not in visited and check_political_figure(friend.display_name):
                    visited.add(friend_id)
                    G.add_node(friend_id, label=friend.display_name)
                    for connected_user in friend_connections[friend_id]:
                        G.add_edge(connected_user, friend_id)  # Add edge from each connected user
                    queue.append((friend_id, current_depth + 1))  # Recurse if this is a new political figure
                    print(f"Added {friend_id}, {friend.display_name} as a political figure connected to {', '.join(friend_connections[friend_id])}.")

    return G

# Parameters
max_friends_per_user = 5  # Not used directly in this snippet, but can be used to limit API responses
crawl_depth = 2
starting_users = ['Valerie-Jarrett-2']

# Begin crawling from the starting users
social_network_graph = crawl_friends_with_priority(client, starting_users, crawl_depth)

# print("Number of nodes:", social_network_graph.number_of_nodes())
# print("Number of edges:", social_network_graph.number_of_edges())

# Draw the graph
pos = nx.spring_layout(social_network_graph)
nx.draw(social_network_graph, pos, with_labels=True, node_size=50, font_size=9)
plt.show()