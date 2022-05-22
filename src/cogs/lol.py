import discord
from src.apis import api_lol

class Lol(discord.ext.commands.Cog, name='Lol module'):

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="Analysis")
    async def match_analysis(self, ctx, arg):
        name = str(arg).strip()
        response = api_lol.lolAnalysis(name)
            
        await ctx.send(response)