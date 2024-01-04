# Discord Webhooks Sender

This simple Python script allows you to easily set up and send messages to Discord webhooks. Follow the steps below to get started.

## Setup

### Step 1: Input Webhook Names and URLs

Open the file `1.Input_Webhook_Name_&_URL.txt` inside the "setup_discord_webhooks" folder. In this file, write each webhook's name and URL in the format `webhook_name: webhook_url` on separate lines. For example:

```plaintext
webhook1: https://example.com/webhook1
webhook2: https://example.com/webhook2
webhook3: https://example.com/webhook3
Step 2: Run Setup Script
Execute the script 2.Setup_webhooks_json.py by navigating to the "setup_discord_webhooks" folder in your command prompt and running:

bash
Copy code
python 2.Setup_webhooks_json.py
This script reads the input file and creates a webhooks.json file with the webhook names and URLs.

Sending Messages
Step 3: Run Webhook Sender Script
Execute the webhook_sender.py script by running:

bash
Copy code
python webhook_sender.py
The script will prompt you to select a webhook by index and enter the message you want to send.

Important Notes
Make sure you have Python installed on your system.

Ensure that the requests library is installed. If not, install it by running:

bash
Copy code
pip install requests
If you encounter any issues, double-check the input file format and paths.

Now you're ready to efficiently send messages to your Discord channels using webhooks!