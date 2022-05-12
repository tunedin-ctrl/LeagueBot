"""
Base class for discord bot
Future implementations will be creating subclasses on top of this bot using design patterns
"""
from discord.ext import commands

# Bot class
class BotClient(commands.Bot):
    #Init bot
    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')

