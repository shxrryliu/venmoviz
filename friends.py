# used venmo_api with the below example (in untracked file called tokens)
# from venmo_api import Client
# client = Client.get_access_token(username='', password='', device_id="-")
# access_token = '-'
# client = Client(access_token=access_token)

from tokens import client

# Get a user's friend's list
users = client.user.get_user_friends_list(user_id='shxrryliu')
for user in users:
    print(user)