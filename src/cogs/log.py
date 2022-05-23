import discord
from src.apis import log_helper

class Log(discord.ext.commands.Cog, name='Logs'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if "LeagueBot#2540" not in str(message.author) and '$' in str(message.content):
            # helper.find_user_by_id("yes#123")
            log_helper.save(str(message.author), str(message.content))   

    # log command usage. if $Analysis <name> used three times within 2min, then freeze command for 2min