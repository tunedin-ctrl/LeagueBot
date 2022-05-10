import discord

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

client.run('your secret discord token')