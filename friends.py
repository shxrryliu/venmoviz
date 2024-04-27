# used venmo_api with the below example (in untracked file called tokens)
# from venmo_api import Client
# client = Client.get_access_token(username='', password='', device_id="-")
# access_token = '-'
# client = Client(access_token=access_token)

from tokens import client
import networkx as nx

# create graph 
G = nx.Graph()

starting_user = 'Malia-Ann'
G.add_node(starting_user, first_name='Malia', last_name='Ann')

# get a friends list
users = client.user.get_user_friends_list(user_id=starting_user)
for user in users:
    print(f"Username: {user.username}, First Name: {user.first_name}, Last Name: {user.last_name}")