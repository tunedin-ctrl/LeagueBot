from pymongo import MongoClient
import os
from pathlib import Path
from dotenv import load_dotenv


# Creating a client
dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
DB_UR_PASS = os.getenv('DB_UR_PASS')
# client = MongoClient("mongodb://127.0.0.1:27017/")
client = MongoClient(f"mongodb+srv://{DB_UR_PASS}/?retryWrites=true&w=majority")
db = client.loldb

# db cur
# db = client.bot
col = db.lol

def save(user, cmd):
    print("here1")
    print(user)
    _id = find_user_by_id(user)
    if _id:
        print("here3")
        print(_id, cmd)
        col.update_one(
            {"user": user},
            {'$push': {"cmd": cmd}}
        )
    else:
        print("here2")

        col.insert_one(
            {
                "user": f"{user}",
                "cmd": [f"{cmd}"]
            }
        )

def find_user_by_id(user):
    # print(client.list_database_names())
    document = col.find_one({"user": user})
    if document:
        alist = str(document.values())
        x = alist.split(', ', maxsplit=1)[0]
        return (x[13:])
    else:
        return None

