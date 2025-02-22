import os
from telethon.sync import TelegramClient

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def main():
    print("Bot Started!")

with client:
    client.loop.run_until_complete(main())
