import json
import os
import requests
from dotenv import load_dotenv
from src.error_handler import api_error

def lolAnalysis(name):
    """
    Input: summoner Id
    Output: Match history
    """
    load_dotenv()
    api_key = os.environ.get('API_KEY')

    response = requests.get(f"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}")
    if response.status_code == 200:
        summoner_info = json.loads(response.text)
        puuid = summoner_info["puuid"]
        match_ids = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count=2&api_key={api_key}')
        if match_ids.status_code == 200:
            matchId = json.loads(match_ids.text)
            # match_files = dict()
            for match_id in matchId:
                match = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}')
                if match.status_code == 200:
                    match_det = json.loads(match.text)
                    for sumName in match_det['info']['participants']:
                        if sumName['summonerName'] == name:
                            with open('lol_db.json', 'w') as match_file:
                                json.dumps(sumName, match_file,
                                         indent = 4)
    else:
        return api_error.AccessError(description=f"API key has expired!")                


def helper_decision_tree():
        pass
    