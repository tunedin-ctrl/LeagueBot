import json
import os
import requests
import pandas
from dotenv import load_dotenv
from src.error_handler import api_error

load_dotenv()
api_key = os.environ.get('API_KEY')


def lolAnalysis(name):
    """
    Input: summoner Id
    Output: Match history
    """
    summoner_info = get_summoner_info(name)
    puuid = summoner_info["puuid"]
    match_ids = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count=2&api_key={api_key}')
    if match_ids.status_code == 200:
        matchId = json.loads(match_ids.text)
        
        json_array = {
            f'{name}': []
        }
        for match_id in matchId:
            match = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}')
            if match.status_code == 200:
                match_det = json.loads(match.text)
                for sumName in match_det['info']['participants']:
                    del sumName['perks']
                    del sumName['summonerId']
                    del sumName['summonerLevel']
                    del sumName['puuid']
                    del sumName['profileIcon']

                    if sumName['summonerName'] == name:
                        json_array[name].append(sumName)
                        del sumName['summonerName']

        with open('lol_db.json', 'w') as match_file:
            json.dump(json_array, match_file, indent=4, separators=(',',': '))
            match_file.write('\n')
        
        with open('lol_db.json', encoding='utf-8') as inputfile:
            df = pandas.read_json(inputfile)
        df.to_csv('csvfile.csv', encoding='utf-8', index=False)

    else:
        return api_error.AccessError(description=f"Something went wrong! Please try again") 

def get_summoner_info(name):
    '''
    input: name:str, api_key:riot key
    output: summoner_info: dict
    '''
    try:
        response = requests.get(f"https://oc1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}")
        if response.status_code == 200:
            summoner_info = json.loads(response.text)
            return summoner_info
    except Exception as e:
        raise api_error.AccessError(e)      


def helper_decision_tree():
    ''' 
    once all operations are done, then delete data
    later stored in mongodb if enough space
    '''

    pass
    