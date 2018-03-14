bot_template = "BOT: {0}"
user_template = "USER: {0}"

def respond(messaage):
	bot_message = "I can hear you! You said: " + messaage
	return bot_message

if __name__ == "__main__":
	bot_response = respond("Hello!")
	print(bot_response)