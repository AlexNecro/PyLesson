import requests


def send_message(username, text):
    message = {"username": username, "text": text}
    response = requests.post("http://127.0.0.1:5000/send", json=message)
    return response.status_code == 200


username = input("Введите имя: ")


while True:
    text = input("Введите сообщение: ")
    result = send_message(username, text)
    if not result:
        print("Error")

