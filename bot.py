api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE_NUMBER')

client = TelegramClient('user', api_id, api_hash)

async def main():
    await client.start(phone)
    print("Logged in as user!")

@client.on(events.NewMessage(chats=SOURCE_CHAT_ID))
async def forward_message(event):
    await client.send_message(DEST_CHAT_ID, event.message)

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
