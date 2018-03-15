import random

bot_template = "BOT: {0}"

responses = {
	"question": [
		"I don't know :(",
		"You tell me!"
	],
	"statement": [
		"Tell me more!",
		"Why do you think that?",
		"How long have you felt this way?",
		"I find the extremely interesting",
		"Can you back that up?",
		"Oh wow!",
		":)"
	]
}

def respond(message):
	#Check for a question mark
	if message.endswith("?"):
		#Return a random question:
		return random.choice(responses["question"])
	else:
		#Return a random statement
		return random.choice(responses["statement"])
	return bot_message

def send_message(message):
	response = respond(message)
	print(bot_template.format(response))

if __name__ == "__main__":
	question = input("USER: ")
	send_message(question)