import fbchat
import os
import matplotlib.pyplot as plt
from computeResponse import computeResponse

def summarizeResults(userAtimes, userBtimes, friendName):
    friendFirstName = friendName.split(" ")[0]
	# might want to check divide by zero error if lists are empty
	f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
	ax1.hist(userBtimes)
	textLocation = (300, ax1.get_ylim()[1] * 0.8)
	ax1.set_title(friendFirstName + "'s reponse time to you")
	ax1.set_ylabel("Count")
	ax1.set_xlabel("Response time in seconds")
	ax1.text(textLocation[0], textLocation[1], "Average: " + 
		str(sum(userBtimes) / len(userBtimes)))
	ax2.hist(userAtimes)
	ax2.text(textLocation[0], textLocation[1], "Average: " + 
		str(sum(userAtimes) / len(userAtimes)))
   ax2.set_title("Your reponse time to " + friendFirstName)
	ax2.set_xlabel("Count")
	plt.show()

def main():
	# Need to export facebook ID and password 
	# Find facebook ID here: http://findmyfbid.com/
	client = fbchat.Client(os.environ['ID'], os.environ['PASSWORD'])
	friendName = raw_input("Friend's name: ")
	(userAtimes, userBtimes) = computeResponse(friendName, client)
	summarizeResults(userAtimes, userBtimes, friendName)

if __name__ == "__main__":
	main()