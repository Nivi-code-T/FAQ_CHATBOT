from flask import Flask, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/chat")
def chat():

    msg = request.args.get("msg")

    return get_response(msg)

app.run(debug=True)