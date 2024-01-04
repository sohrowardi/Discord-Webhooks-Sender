# webhook_sender.py
import json
import os
import requests

def find_webhooks_file(starting_path="."):
    for root, dirs, files in os.walk(starting_path):
        if "webhooks.json" in files:
            return os.path.join(root, "webhooks.json")
    return None

def load_webhooks(file="webhooks.json"):
    found_file = find_webhooks_file()
    if found_file:
        with open(found_file, 'r') as json_file:
            webhooks = json.load(json_file)
        return webhooks
    else:
        print("Error: webhooks.json not found.")
        return {}

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
