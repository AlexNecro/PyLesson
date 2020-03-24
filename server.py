from flask import Flask, request
import time

app = Flask(__name__)

messages = [
    {"username": "Nick", "text": "Hello", "time": time.time()}
]


@app.route("/")
def hello():
    return "Hello"


@app.route("/status")
def status():
    return {"status": True, "name": "Сервер Алексея", "time": time.ctime()}


@app.route("/send", methods=["POST"])
def send():
    username = request.json["username"]
    text = request.json["text"]
    curtime = time.time()
    messages.append({"username": username, "text": curtime, "time": time.time()})
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
