from __future__ import division
import discord
import requests
import json
import os
import roman
from pathlib import Path
from dotenv import load_dotenv
from src.error_handler import api_error
 
class elo_rating(discord.ext.commands.Cog, name='Lol module'):

    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="Elo")
    async def calculate_elo(self, ctx, arg):
        dotenv_path = Path('.env')
        load_dotenv(dotenv_path=dotenv_path)
        api_key = os.getenv('API_KEY')
        name = str(arg).strip()
        total_elo = 0
        summoner = requests.get(f"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}")
        if summoner.status_code == 200:
            message = json.loads(summoner.text)
            summoner_puuid = message["puuid"]
            message = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_puuid}/ids?start=0&count=20")
            recent_matches = json.loads(message.text)
            for match in recent_matches:
                message = requests.get(f"https://americas.api.riotgames.com/lol/match/v5/matches/{match}")
                match_details = json.loads(message.text)
                match_participants = match_details["metadata"]["participants"]
                for participant in match_participants:
                    message = requests.get(f"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{participant}")
                    summoner_details = json.loads(message.text)         
                    summoner_id = summoner_details[id]
                    message = requests.get(f"https://oc1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}")
                    extra_summoner_details = json.loads(message.text) 
                    summoner_elo = self.calculate_elo((extra_summoner_details["tier"], extra_summoner_details["division"]))
                    total_elo = total_elo + summoner_elo

        else:
            message = api_error.AccessError(description=f"Summoner name {name} you have provided does not exist")                
            raise api_error.AccessError(description=f"Summoner name {name} you have provided does not exist")

        await ctx.send(total_elo/200)

    def calculate_elo(rank):
        elo = 0
        tier, division = rank
        if tier == "IRON":
            elo = elo + 1000
        elif tier == "BRONZE":
            elo = elo + 1200
        elif tier == "SILVER":
            elo = elo + 1400
        elif tier == "GOLD":
            elo = elo + 1600
        elif tier == "PLATINUM":
            elo = elo + 1800
        elif tier == "DIAMOND":
            elo = elo + 2000
        else:
            elo = elo + 2200
        elo = elo + 50*(4-roman.fromroman(division))
        return elo
        