import json
import os
import requests
import pandas
import pydotplus
from dotenv import load_dotenv
from src.error_handler import api_error
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
import category_encoders as ce

# visualising dataset
from six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz

load_dotenv()
api_key = os.environ.get('API_KEY')


def lolAnalysis(name):
    """
    Input: summoner Id
    Output: Match history
    """
    summoner_info = get_summoner_info(name)
    puuid = summoner_info["puuid"]
    
    matchId = get_match_ids(name)
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
                del sumName['challenges']
                del sumName['championId']
                del sumName['lane']
                del sumName['role']
                del sumName['riotIdName']
                del sumName['riotIdTagline']
                
                if sumName['summonerName'] == name:
                    json_array[name].append(sumName)
                    del sumName['summonerName']

    with open('lol_db.json', 'w') as match_file:
        json.dump(json_array, match_file, indent=4, separators=(',',': '))
        match_file.write('\n')
    
    df = pandas.DataFrame.from_dict(json_array[name])
    df.to_csv('csvfile.csv', encoding='utf-8', index=False, header=1)
    # Create tree
    helper_decision_tree(name)
    # return path
    return f'{name}_win.png'


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

def get_match_ids(name):
    '''
    get match id
    '''
    try:
        match_ids = requests.get(f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count=30&api_key={api_key}')
        if match_ids.status_code == 200:
            matchId = json.loads(match_ids.text)
            return matchId
    except Exception as e:
        raise api_error.AccessError(e)      



# inspiration from: https://www.datacamp.com/tutorial/decision-tree-classification-python
def helper_decision_tree(name):
    ''' 
    once all operations are done, then delete data
    later stored in mongodb if enough space
    '''
    #col used
    col_names = ['assists','baronkills','bountyLevel', 'champExperience', 'champLevel', 'championName', 'championTransform', 'consumablesPurchased', 'damageDealtToBuildings', 'damageDealtToObjectives', 'damageDealtToTurrets', 'damageSelfMitigated', 'deaths', 'detectorWardsPlaced', 'doubleKills', 'dragonKills', 'eligibleForProgression', 'firstBloodAssist', 'firstBloodKill', 'firstTowerAssist', 'firstTowerKill', 'gameEndedInEarlySurrender', 'gameEndedInSurrender', 'goldEarned', 'goldSpent', 'individualPosition', 'inhibitorKills', 'inhibitorTakedowns', 'inhibitorsLost', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'itemsPurchased', 'killingSprees', 'kills', 'largestCriticalStrike', 'largestKillingSpree', 'largestMultiKill', 'longestTimeSpentLiving', 'magicDamageDealt', 'magicDamageDealtToChampions', 'magicDamageTaken', 'neutralMinionsKilled', 'nexusKills', 'nexusLost', 'nexusTakedowns', 'objectivesStolen', 'objectivesStolenAssists', 'participantId', 'pentaKills', 'physicalDamageDealt', 'physicalDamageDealtToChampions', 'physicalDamageTaken', 'quadraKills', 'sightWardsBoughtInGame', 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts', 'summoner1Casts', 'summoner1Id', 'summoner2Casts', 'summoner2Id', 'teamEarlySurrendered', 'teamId', 'teamPosition', 'timeCCingOthers', 'timePlayed', 'totalDamageDealt', 'totalDamageDealtToChampions', 'totalDamageShieldedOnTeammates', 'totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'totalMinionsKilled', 'totalTimeCCDealt', 'totalTimeSpentDead', 'totalUnitsHealed', 'tripleKills', 'trueDamageDealt', 'trueDamageDealtToChampions', 'trueDamageTaken', 'turretKills', 'turretTakedowns', 'turretsLost', 'unrealKills', 'visionScore', 'visionWardsBoughtInGame', 'wardsKilled', 'wardsPlaced', 'win']
    feature_cols = ['assists','baronkills','bountyLevel', 'champExperience', 'champLevel', 'championName', 'championTransform', 'consumablesPurchased', 'damageDealtToBuildings', 'damageDealtToObjectives', 'damageDealtToTurrets', 'damageSelfMitigated', 'deaths', 'detectorWardsPlaced', 'doubleKills', 'dragonKills', 'eligibleForProgression', 'firstBloodAssist', 'firstBloodKill', 'firstTowerAssist', 'firstTowerKill', 'gameEndedInEarlySurrender', 'gameEndedInSurrender', 'goldEarned', 'goldSpent', 'individualPosition', 'inhibitorKills', 'inhibitorTakedowns', 'inhibitorsLost', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'itemsPurchased', 'killingSprees', 'kills', 'largestCriticalStrike', 'largestKillingSpree', 'largestMultiKill', 'longestTimeSpentLiving', 'magicDamageDealt', 'magicDamageDealtToChampions', 'magicDamageTaken', 'neutralMinionsKilled', 'nexusKills', 'nexusLost', 'nexusTakedowns', 'objectivesStolen', 'objectivesStolenAssists', 'participantId', 'pentaKills', 'physicalDamageDealt', 'physicalDamageDealtToChampions', 'physicalDamageTaken', 'quadraKills', 'sightWardsBoughtInGame', 'spell1Casts', 'spell2Casts', 'spell3Casts', 'spell4Casts', 'summoner1Casts', 'summoner1Id', 'summoner2Casts', 'summoner2Id', 'teamEarlySurrendered', 'teamId', 'teamPosition', 'timeCCingOthers', 'timePlayed', 'totalDamageDealt', 'totalDamageDealtToChampions', 'totalDamageShieldedOnTeammates', 'totalDamageTaken', 'totalHeal', 'totalHealsOnTeammates', 'totalMinionsKilled', 'totalTimeCCDealt', 'totalTimeSpentDead', 'totalUnitsHealed', 'tripleKills', 'trueDamageDealt', 'trueDamageDealtToChampions', 'trueDamageTaken', 'turretKills', 'turretTakedowns', 'turretsLost', 'unrealKills', 'visionScore', 'visionWardsBoughtInGame', 'wardsKilled', 'wardsPlaced']
    # load csv file
    df = pandas.read_csv("csvfile.csv")
    df.columns = col_names
    # specify target and normal col
    X = df[feature_cols]
    y = df['win']
    # Training set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)
    # Encode feature_cols
    encoder = ce.OrdinalEncoder(cols=feature_cols)
    X_train = encoder.fit_transform(X_train)
    X_test = encoder.transform(X_test)
    #Create tree inst
    clf = DecisionTreeClassifier()
    #Predict and train the response for test dataset
    clf.fit(X_train, y_train)                                                        
    y_pred = clf.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    # Print tree out
    dot_data = StringIO()
    export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['lose','win'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png(f'{name}_win.png')
    Image(graph.create_png())

