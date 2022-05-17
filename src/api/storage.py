from pymongo import MongoClient

# Creating a client
client = MongoClient('mongodb://127.0.0.1:27017/')
 
# Creating a database name GFG
db = client["bot"]
print("Database is created !!")


print(client.list_database_names())
 
# if "GFG" in list_of_db:
    # print("Exists !!")