from src.apis import api_lol

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
    
def test_decision_tree():
    name= "MiliterryNasus"
    api_lol.lolAnalysis(name)