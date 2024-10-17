def get_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but thanks for asking!",
        "what is your name": "I'm HelperBot, your personal assistant.",
    }

    default_response = "I'm sorry, I didn't understand that."

    for key in responses:
        if key in user_input:
            return responses[key]

    return default_response
