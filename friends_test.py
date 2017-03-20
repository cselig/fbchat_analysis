import facebook

graph = facebook.GraphAPI(access_token)
friends = graph.get_object("me/friends")
for friend in friends['data']:
    print "{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id'])