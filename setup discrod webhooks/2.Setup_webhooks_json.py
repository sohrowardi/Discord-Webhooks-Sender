# 2.Setup_webhooks_json.py
import json

def setup_webhooks(input_file="1.Input_Webhook_Name_&_URL.txt", output_file="webhooks.json"):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    webhooks = {}
    for line in lines:
        print(f"Processing line: {line.strip()}")
        try:
            name, url = line.strip().split(': ')
            webhooks[name] = url
        except ValueError:
            print(f"Error processing line: {line.strip()}")

    with open(output_file, 'w') as json_file:
        json.dump(webhooks, json_file, indent=2)

if __name__ == "__main__":
    setup_webhooks()
    print("Webhooks setup completed. Check webhooks.json.")
