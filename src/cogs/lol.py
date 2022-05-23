import discord
from src.apis import api_lol

class Lol(discord.ext.commands.Cog, name='Lol module'):

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="Analysis")
    async def match_analysis(self, ctx, arg):
        await ctx.send("This may take a while...")
        name = str(arg).strip()
        path = api_lol.lolAnalysis(name)
        with open(path, 'rb') as f:
            picture = discord.File(f)
            await ctx.send(picture)