import discord
from src.api_storage import helper

class Log(discord.ext.commands.Cog, name='Logs'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author != "LeagueBot#2540":
            helper.save(message.author, message.content)   