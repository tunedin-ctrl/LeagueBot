import discord
import requests
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from src.error_handler import api_error

class Lol(discord.ext.commands.Cog, name='Lol module'):

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="Matches")
    async def match_Hist(self, ctx, arg):
        dotenv_path = Path('.env')
        load_dotenv(dotenv_path=dotenv_path)
        api_key = os.getenv('API_KEY')
        """
        Input: summoner Id
        Output: Match history
        """
        name = str(arg).strip()
        # use your own token
        response = requests.get(f"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}")
        # print(response.)
        if response.status_code == 200:
            summoner_info = json.loads(response.text)
            puuid = summoner_info["puuid"]
            match_ids = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=5&api_key=RGAPI-077d0358-b6a2-4501-8739-700d1a9da7dd')
            matchId = json.loads(match_ids.text)
            for match_id in matchId:
                match = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key=RGAPI-077d0358-b6a2-4501-8739-700d1a9da7dd')
                print(match.text)

        else:
            message = api_error.AccessError(description=f"Summoner name {name} you have provided does not exist")                
            raise api_error.AccessError(description=f"Summoner name {name} you have provided does not exist")

            
        await ctx.send(match_ids)