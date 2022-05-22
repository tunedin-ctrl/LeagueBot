import json
from src.apis import api_lol

def test_user_details():
    '''
    user does not exist when inserting
    '''
    name="MiliterryNasus"
    api_lol.lolAnalysis(name)
        