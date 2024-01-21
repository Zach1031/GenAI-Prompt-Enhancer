import discord
from config import api_key

import query 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$imagine'):
        await message.channel.send(query.create_query(message.content[1:]))


client.run(api_key)

