import time
import discord
from src.apis import api_lol

counter = 1
start = time.time()
class Lol(discord.ext.commands.Cog, name='Lol module'):

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="Analysis")
    async def match_analysis(self, ctx, arg):
        global counter
       
        if counter >= 3:
            stop = time.time()
            elapsed_time = stop - start
            if elapsed_time == 120:
                time.sleep(120)
                counter = 0                
                await ctx.send("Command on cooldown: 2min")
        counter = counter + 1
        await ctx.send("This may take a while...")
        name = str(arg).strip()
        path = api_lol.lolAnalysis(name)
        with open(path, 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

    