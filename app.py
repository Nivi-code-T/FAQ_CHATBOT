#import flask
from flask import Flask, request
app=Flask(__name__)

faq={
    "hello": "Hi there",
    "price": "Plans starts at rs.499",
    "refund": "Refunds are processed in 5 days"
}

@app.route("/chat")
def chat():
    user_input = request.args.get("msg").lower()
    for key in faq:
        if key in user_input:
            return faq[key]
    return "Sorry, I don't understand."

app.run(debug=True)