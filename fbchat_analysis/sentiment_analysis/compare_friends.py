import fbchat
import os
from pull_messages import pull_messages
from classify import Classifier

client = fbchat.Client(os.environ['ID'], os.environ['PASSWORD'])
friends_file = open('../friends/friends_short.txt', 'r')

c = Classifier()

from_lengths = {}
to_lengths = {}
from_sentiments = {}
to_sentiments = {}

friends = []


for l in friends_file:
    tokenized = l.split(' ')
    friend_name = tokenized[0] + ' ' + tokenized[1]
    friends.append(friend_name)

for friend_name in friends:
    print(friend_name)

    print('pulling messages')
    (you_messages, friend_messages) = pull_messages(client, friend_name)
    from_lengths[friend_name] = len(friend_messages)
    to_lengths[friend_name] = len(you_messages)

    print('classifing')
    (you_sentiments, friend_sentiments) = c.classify_from_lists(you_messages, friend_messages)
    from_sentiments[friend_name] = friend_sentiments
    to_sentiments[friend_name] = you_sentiments

    print()