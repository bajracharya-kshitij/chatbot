#Import the random module
import random

#Define variables
name = "Kshitij"
weather = "cloudy"

#Define a dictionary containing a list of reponses for each message
responses = {
	"what's your name?": [
		"My name is {0}".format(name),
		"They call me {0}".format(name),
		"I go by {0}".format(name)
	],
	"what's today's weather?": [
		"The weather is {0}".format(weather),
		"It's {0} today".format(weather)
	],
	"default": ["default message"]
}

#Use random.choice() to choose a matching response
def respond(message):
	#Check if the message is in the responses
	if message in responses:
		#Return a random matching response
		bot_message = random.choice(responses[message])
	else:
		#Return a random "default" response
		bot_message = random.choice(responses["default"])
	return bot_message


if __name__ == "__main__":
	question = input("Your question: ")
	response = respond(question)
	print(response)