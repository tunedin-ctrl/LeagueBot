from src.apis import api_lol
import os

def test_user_details():
    '''
    user does not exist when inserting
    '''
    name= "MiliterryNasus"
    name2= "tunein"
    output = (api_lol.get_summoner_info(name))
    output2 = (api_lol.get_summoner_info(name2))
    assert output['name'] == name
    assert output2['name'] == name2

def test_get_match_ids():
    name= "MiliterryNasus"
    name2= "tunein"
    summoner_info = (api_lol.get_summoner_info(name))
    summoner_info2 = (api_lol.get_summoner_info(name2))
    puuid = summoner_info["puuid"]
    puuid2 = summoner_info2["puuid"]
    output = api_lol.get_match_ids(puuid)
    output2 = (api_lol.get_summoner_info(puuid2))
    output = ''.join(str(x) for x in output)
    output2 = ''.join(str(x) for x in output2)
    assert "OC1" in output
    assert "OC" in output2


def test_decision_tree():
    name= "MiliterryNasus"
    api_lol.helper_decision_tree(name)
    assert os.path.isfile(f"{name}_win.png")
