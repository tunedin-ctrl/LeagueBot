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
            await ctx.send(file=picture)
    
    # log command usage. if $Analysis <name> used three times within 2min, then freeze command for 2min
    @discord.ext.commands.Cog.listener()
    async def on_analysis(self, message:discord.Message):
        '''
        if used in two min, raise error
        '''
        pass

    