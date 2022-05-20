from pymongo import MongoClient
import os
from pathlib import Path
from dotenv import load_dotenv


# Creating a client
def init():
    dotenv_path = Path()
    load_dotenv(dotenv_path=dotenv_path)
    DB_UR_PASS = os.environ.get('DB_UR_PASS')
    # client = MongoClient("mongodb://127.0.0.1:27017/")
    client = MongoClient(f"mongodb+srv://{DB_UR_PASS}/?retryWrites=true&w=majority")
    db = client.loldb
    col = db.lol
    return col

def save(user, data):
    col = init()
    _id = find_user_by_id(user)
    if _id:
        col.update_one(
            {"user": user},
            {'$push': {"cmd": data}}
        )
    else:
        col.insert_one(
            {
                "user": f"{user}",
                "cmd": [f"{data}"]
            }
        )

def find_user_by_id(user):
    document = find_user(user)
    if document:
        alist = str(document.values())
        x = alist.split(', ', maxsplit=1)[0]
        return (x[13:])
    else:
        return None

def find_user(user):
    col = init()
    return col.find_one({"user": user})

def delete_user(user):
    col = init()
    col.delete_one({"user": user})
