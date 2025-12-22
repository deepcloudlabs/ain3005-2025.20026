from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
denizbank = mongo_client["denizbank"]
accounts_collection = denizbank["accounts"]
for account in accounts_collection.find({
    "$and": [
        {"status": {"$in": ["CLOSED", "BLOCKED"]}},
        {"balance": {"$gt": 3_000_000}}
    ]    }):
    print(account)