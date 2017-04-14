import fbchat
import os
import operator
from computeResponse import computeResponse

# Note!!! Add the following lines to client.py in the fbchat package at line 544
# if not 'actions' in j['payload']:
#    return []

def main():
	# Need to export facebook ID and password as envinronment variables
	# Find facebook ID here: http://findmyfbid.com/
	client = fbchat.Client(os.environ['ID'], os.environ['PASSWORD'])

	friendsFile = open("mattsFriends.txt", "r")
	# average response times 
	timesAtoB = {}
	timesBtoA = {}
	for line in friendsFile:
		split = line.split(" ")
		friendName = split[0] + " " + split[1]
		(userAtimes, userBtimes) = computeResponse(friendName, client)
		print("\n" + friendName)
		print(userAtimes)
		print(userBtimes)
		if len(userAtimes) > 50: # make sure that there's enough data
			timesAtoB[friendName] = sum(userAtimes) / len(userAtimes)
			print(timesAtoB[friendName])
		if len(userBtimes) > 50:
			timesBtoA[friendName] = sum(userBtimes) / len(userBtimes)
			print(timesBtoA[friendName])

	sortedAtoB = sorted(timesAtoB.items(), key=operator.itemgetter(1))
	sortedBtoA = sorted(timesBtoA.items(), key=operator.itemgetter(1))

	numRank = 10 # number of friends to display
	print("Top " + str(numRank) + " fastest responding friends: ")
	for i in range(0, numRank):
		print(str(i + 1) + ") " + sortedBtoA[i][0])
	print("")
	print("Top 5 friends you respond to fastest: ")
	for i in range(0, numRank):
		print(str(i + 1) + ") " + sortedAtoB[i][0])	

if __name__ == "__main__":
	main()
