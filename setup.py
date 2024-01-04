import json

def setup_webhooks():
    webhooks = []

    while True:
        name = input("Enter webhook name (or type 'exit' to finish): ")
        if name.lower() == 'exit':
            break

        url = input("Enter webhook URL: ")

        webhook = {"name": name, "url": url}
        webhooks.append(webhook)

    with open('webhooks.json', 'w') as file:
        json.dump({"webhooks": webhooks}, file)

if __name__ == "__main__":
    setup_webhooks()
