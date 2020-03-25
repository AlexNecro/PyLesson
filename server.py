from flask import Flask, request
import time

app = Flask(__name__)

users = []
messages = []


@app.route("/")
def hello():
    return "Hello"


@app.route("/status")
def status():
    msgsQty = len(messages)
    usersQty = len(users);
    return {"status": True, "name": "Сервер Алексея", "time": time.ctime(), "users": usersQty, "messages": msgsQty}


@app.route("/send", methods=["POST"])
def send():
    username = request.json["username"]
    text = request.json["text"]
    curtime = time.time()

    if users.count(username) == 0:
        users.append(username)
    messages.append({"username": username, "text": text, "time": curtime})
    print(request.json)
    return {"ok": True}


@app.route("/messages", methods=["GET"])
def messages_view():
    after = float(request.args.get("after"))
    filtered_messages = []
    for message in messages:
        if message["time"] > after:
            filtered_messages.append(message)
    return {"messages": filtered_messages}


app.run()
