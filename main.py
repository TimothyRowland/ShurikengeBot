import os
import discord
from discord import client
from dotenv import load_dotenv

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

client.run(TOKEN)
















#Everything below this is a test

# # bot.py
# import os

# import discord
# from discord import client
# from dotenv import load_dotenv

# intents = discord.Intents.all()
# intents.members = True

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client(intents=intents)


# @client.event
# async def on_ready():
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

# client.run(TOKEN)