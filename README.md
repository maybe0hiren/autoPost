# autoPost
Automated journaling agent using AI...


## Project Description

autoPost is an AI-driven automation system designed to generate personalized social media captions using a fine-tuned GPT-2 model and automatically post them to platforms like Instagram. It includes a Telegram bot interface for remote control and notifications, enabling seamless automation of content creation and publishing workflows without manual intervention.

Key features include:  
- Fine-tuned GPT-2 with LoRA for efficient caption generation.  
- Automated Instagram Business API integration for image carousel posting.  
- Schedule-based automation for timed daily posting.  
- Telegram bot integration for monitoring, messaging, and commands.  
- Modular, maintainable codebase organized for extension and customization.

---

## Project Structure

autoPost/  
├── aiModel/  
│ ├── init.py  
│ ├── aiInterface.py  
│ ├── captionGeneration.py  
│ └── jsonToDataset.py  
├── Telegram/  
│ ├── init.py  
│ ├── telegramInterface.py  
│ └── contentExtractor.py  
└── README.md # Project documentation

## Packages

transformers   
torch 
peft 
telebot 
schedule 
requests


## Telegram Bot

1. Create a Telegram Bot via BotFather
What is BotFather?
BotFather is the official Telegram bot used to create and manage bots on the Telegram platform.
How to create your bot:
Open the Telegram app and search for @BotFather.
Start a chat with BotFather by clicking Start.
Send the /newbot command to create a new bot.
Follow BotFather’s prompts to name your bot and give it a unique username ending with bot (e.g., AutoPostBot).
Upon completion, BotFather will provide you with an API token. This token allows your code to control the bot.

2. Add the Bot Token to Your Project in contentExtractor.py at "TOKEN"

3. Obtain Your Chat ID
What is chat ID?
The chat ID is a unique identifier for the chat where messages are sent or received, such as your personal chat or a group.
How to get it:
Run your Telegram bot script (telegramInterface.py) with a handler that listens to messages and replies with the chat ID.
Send a message to your bot in Telegram.
The bot will reply to you with the chat ID.

4. Running the Telegram Bot Interface
Execute the bot script to start your bot’s long polling and message handling.
The bot listens for messages or commands and responds or triggers actions accordingly.
You can extend or customize handlers in telegramInterface.py to control what the bot does.

5. Integration with Other Project Components
Your Telegram bot can send you notifications or interface with the AI caption generation module (aiInterface.py).
You can send commands via Telegram to start caption generation, request status updates, or trigger social media posting.
This enables remote control and monitoring of your automated social media system.
