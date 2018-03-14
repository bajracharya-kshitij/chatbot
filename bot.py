bot_template = "BOT: {0}"
user_template = "USER: {0}"

def respond(messaage):
	bot_message = "I can hear you! You said: " + messaage
	return bot_message

def send_message(message):
	print(user_template.format(message))
	response = respond(message)
	print(bot_template.format(response))

if __name__ == "__main__":
	send_message("Hello!")