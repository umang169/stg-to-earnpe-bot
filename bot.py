from telethon import TelegramClient, events
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_BOT_ID = "@YourBotUsername"  # Replace with your bot's username
CHANNEL_USERNAME = "@ChannelUsername"  # Replace with the channel username

client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=CHANNEL_USERNAME))
async def forward_to_bot(event):
    await client.send_message(TARGET_BOT_ID, event.message)

client.start()
print("Userbot is running...")
client.run_until_disconnected()
