# Webhook Sender

Webhook Sender is a simple Python script that allows you to set up and send messages through Discord webhooks effortlessly.

## Setup

### 1. Input Webhook Name & URL

In the "setup_discord_webhooks" folder, you'll find a file named `1.Input_Webhook_Name_&_URL.txt`. Open this file and add your Discord webhook names and URLs in the following format:

```plaintext
webhook1: https://example.com/webhook1
webhook2: https://example.com/webhook2
webhook3: https://example.com/webhook3

### 2. Setup Webhooks JSON

In the same folder, run the 2.Setup_webhooks_json.py script. This script will process the input file and create a webhooks.json file, containing the configured webhooks.

```plaintext
python 2.Setup_webhooks_json.py

### Usage
Now that your webhooks are set up, you can use the webhook_sender.py script to send messages.


python webhook_sender.py
Select the webhook you want to use.
Enter your message.
The message will be sent to the chosen Discord channel through the selected webhook.

Troubleshooting
### If you encounter issues, make sure the webhooks.json file is properly generated in the "setup_discord_webhooks" folder.

### Contributing
If you'd like to contribute to this project, feel free to open an issue or submit a pull request.