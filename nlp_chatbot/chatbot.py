import json

with open("intents.json") as file:
    data = json.load(file)

def get_response(user_input):

    user_input = user_input.lower()

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            if pattern.lower() in user_input:
                return intent["responses"][0]

    return "I don't understand"