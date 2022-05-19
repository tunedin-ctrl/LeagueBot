import discord
from src.api_storage import helper

class Log(discord.ext.commands.Cog, name='Logs'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if "LeagueBot#2540" not in str(message.author) and '$' in str(message.content):
            # helper.find_user_by_id("yes#123")
            helper.save(str(message.author), str(message.content))   