from pymongo import MongoClient
import re

# Creating a client
client = MongoClient('mongodb://127.0.0.1:27017/')
# db cur
db = client.bot
loldb = db.loldb

def save(user, cmd):
    _id = find_user_by_id(user)
    if _id:
        loldb.update({"{_id": _id}, {"user": user}, {'$push': {"cmd": cmd}})
    else:
        loldb.insert_one({"user": user}, {"cmd": cmd})

def find_user_by_id(user):
    document = (loldb.find_one({"user": user}))
    alist = str(document.values())
    x = alist.split(', ')[0]
    return (x[13:])


