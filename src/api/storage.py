from pymongo import MongoClient

# Creating a client
client = MongoClient('mongodb://127.0.0.1:27017/')
 
# init db
db = client["bot"]



print(client.list_database_names())
 
# if "GFG" in list_of_db:
    # print("Exists !!")
