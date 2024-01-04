# webhook_sender.py
import json
import requests

def load_webhooks(file="webhooks.json"):
    with open(file, 'r') as json_file:
        webhooks = json.load(json_file)
    return webhooks

def select_channel(webhooks):
    print("Available Webhooks:")
    for i, (name, _) in enumerate(webhooks.items()):
        print(f"{i + 1}. {name}")

    index = int(input("Enter the index of the webhook you want to use: ")) - 1
    selected_webhook = list(webhooks.values())[index]
    return selected_webhook

def send_message(webhook_url, message):
    payload = {"content": message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=payload, headers=headers)
    print(f"Message sent. Response: {response.status_code}")

if __name__ == "__main__":
    webhooks = load_webhooks()
    selected_webhook = select_channel(webhooks)

    message = input("Enter your message: ")
    send_message(selected_webhook, message)
