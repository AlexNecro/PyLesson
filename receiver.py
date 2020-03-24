import requests
import time
from datetime import datetime


def get_messages(after):
    params = {"after": after}
    response = requests.get("http://127.0.0.1:5000/messages", params={"after": after})
    data = response.json()
    return data["messages"]


def print_message(message):
    msg_time = datetime.fromtimestamp(message["time"])
    print(msg_time.strftime("%H:%M:%S"), message["username"]);
    print(message["text"])
    print()


after = 0
while True:
    messages = get_messages(after)
    for message in messages:
        print_message(message)
        if message["time"] > after:
            after = message["time"]

    time.sleep(1)

