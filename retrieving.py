import time
import random
import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
from collections import defaultdict, deque
from tokens import client  # Make sure this import is correct based on your file structure

def check_political_figure(name):
    formatted_name = name.replace(' ', '_')
    url = f"https://en.wikipedia.org/wiki/{formatted_name}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text().lower()
        political_keywords = ['politician', 'White House', 'senator', 'congress', 'political party', 'election', 'ambassador', 'legislature', 'government', 'Obama', 'cabinet', 'public policy']
        return any(keyword in text_content for keyword in political_keywords)
    return False

def crawl_friends_with_priority(client, starting_users, max_depth, max_friends_per_user):
    G = nx.Graph()
    visited = set()
    queue = deque([(user, 0) for user in starting_users])  # Manage the crawl

    while queue:
        current_user, current_depth = queue.popleft()
        if current_depth < max_depth:
            time.sleep(10)  # Sleep to manage API call rate
            friends = client.user.get_user_friends_list(user_id=current_user)
            # Filter for politically relevant friends
            political_friends = [f for f in friends if check_political_figure(f.display_name)]

            # Randomly select up to max_friends_per_user from the politically relevant friends
            selected_friends = random.sample(political_friends, min(len(political_friends), max_friends_per_user))

            for friend in selected_friends:
                friend_id = friend.username
                if friend_id not in visited:
                    visited.add(friend_id)
                    G.add_node(friend_id, label=friend.display_name)
                    G.add_edge(current_user, friend_id)
                    if current_depth + 1 < max_depth:
                        queue.append((friend_id, current_depth + 1))
                    print(f"Added {friend_id} ({friend.display_name}) as a politically relevant friend connected to {current_user}.")
    return G

# Parameters
max_friends_per_user = 5
crawl_depth = 4
starting_users = ['Valerie-Jarrett-2']

# Begin crawling from the starting users
social_network_graph = crawl_friends_with_priority(client, starting_users, crawl_depth, max_friends_per_user)

# Draw the graph
pos = nx.spring_layout(social_network_graph)
nx.draw(social_network_graph, pos, with_labels=True, node_size=50, font_size=9)
plt.show()
