import discord
import requests
import json
from src.error_handler import api_error

class Lol(discord.ext.commands.Cog, name='Lol module'):

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="Matches")
    async def match_Hist(self, ctx, arg):
        """
        Input: summoner Id
        Output: Match history
        """
        name = str(arg).strip()
        # use your own token
        response = requests.get(f"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key=RGAPI-f32bc481-2d67-4b84-bc82-9cdfa2d16358")
        if response == 200:
            message = json.loads(response.text)
            print(message)
        else:
            raise api_error.AccessError(description=f"Summoner name {name} you have provided does not exist")
            # log into tmp storage to indicate that this id is flagged
            # later on use nosql to store data

        await ctx.send(f'Hey {message}')