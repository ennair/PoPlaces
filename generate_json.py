import facebook
import json
from collections import Counter


# Create a connection to the Graph API with your access token
g = facebook.GraphAPI('')


friends = g.get_connections("me", "friends")['data']


locations = { friend['name'] : g.get_connections(friend['id'], "locations")['data']
        for friend in friends }


json.dump(locations, open('locations.json','w'))