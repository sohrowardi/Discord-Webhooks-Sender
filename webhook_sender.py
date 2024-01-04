import requests
import json

config_file = "webhooks.json"

def load_webhooks():
    try:
        with open(config_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_webhooks(webhooks):
    with open(config_file, "w") as file:
        json.dump(webhooks, file, indent=2)

def send_webhook_message(webhook_url, message):
    data = {
        "content": message
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print("Failed to send message. Error:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred while sending the message:", str(e))

# Display available webhook options
print("Available Webhooks:")
webhooks = load_webhooks()
for key, value in webhooks.items():
    print(f"{key}. {value['name']}")

while True:
    webhook_option = input("Enter the webhook option number (or 0 to quit): ")

    if webhook_option == '0':
        print("Goodbye!")
        break

    if webhook_option.isdigit():
        webhook_option = int(webhook_option)
        webhook = webhooks.get(webhook_option)

        if webhook:
            webhook_name = webhook["name"]
            webhook_url = webhook["url"]

            message = input(f"Enter your message for {webhook_name}: ")
            send_webhook_message(webhook_url, message)
        else:
            print("Invalid webhook option. Please try again.")
    else:
        print("Invalid input. Please enter a number.")

# Save the webhooks for future use
save_webhooks(webhooks)
