import fbchat
import os

def computeResponse(friendName, client):
	friendList = client.getUsers(friendName)
	if len(friendList) == 0:
		return ([], [])
	else: 
		friend = friendList[0]

	# Useful properties of message: timestamp, author, is_unread
	last_messages = client.getThreadInfo(friend.uid,0,20000) # 10000 should cover all messages?
	last_messages.reverse()  # messages come in reversed order

	# define IDs of userA (you) and userB (your friend)
	userA = os.environ['ID']
	userB = friend.uid

	first = True
	userAtimes = [] # list of times for A to respond to B
	userBtimes = [] # list of times for B to respond to A
	
	for message in last_messages:
			if not first:
				# find response time, convert to seconds
				timeDiff = (message.timestamp - lastMessage.timestamp) / 1000
				# assume responses after 10min are a different conversation
				if timeDiff < 600:
					if lastMessage.author != message.author:
						if lastMessage.author.split(":")[1] == str(userB):
							userAtimes.append(timeDiff)
						else: # lastMessage.author.split(":")[1] == userA
							userBtimes.append(timeDiff)
			first = False
			lastMessage = message
	return (userAtimes, userBtimes)