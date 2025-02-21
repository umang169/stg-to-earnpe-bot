from telethon import TelegramClient, events
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_BOT_ID = "@YourBotUsername"
CHANNEL_USERNAME = "@ChannelUsername"

client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def forward_to_bot(event):
    await client.send_message(TARGET_BOT_ID, event.message)

client.start()
print("Userbot is running...")
client.run_until_disconnected()

