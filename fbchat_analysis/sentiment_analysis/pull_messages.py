import fbchat
import os

def pull_messages(client, friend_name):
    friendList = client.getUsers(friend_name)
    if len(friendList) == 0:
        return []
    else: 
        friend = friendList[0]

    try:
        last_messages = client.getThreadInfo(friend.uid, 10000) # 10000 should cover all messages?
        last_messages.reverse()  # messages come in reversed order
    except KeyError:
        return []

    you_messages = []
    friend_messages = []

    for message in last_messages:
        if hasattr(message, 'body') and message.body:
            if message.author.split(':')[1] == str(os.environ['ID']):
                you_messages.append(message.body)
            else:
                friend_messages.append(message.body)

    return (you_messages, friend_messages)