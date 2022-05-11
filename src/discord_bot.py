"""
Basic code for discordBot
"""
from pathlib import Path
import os
from dotenv import load_dotenv
import discord


# Token contained in local environment
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

client = discord.Client()

@client.event
async def on_ready():
    """
    Initialise bot
    """
    print(f'{client.user} bot user is ready to rumble!')

@client.event
async def on_message(message):
    """ Input:  Message:str
        Output: command:str
    """
    if client.user == message.author:
        return

    if message.content == "hello":
        await message.channel.send('hello right back at you!')

client.run(os.getenv('TOKEN'))
