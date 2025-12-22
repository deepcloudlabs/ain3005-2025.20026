from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017')
denizbank = mongo_client['denizbank']
accounts_collection = denizbank['accounts']

result = accounts_collection.delete_many(
    {"status": {"$in": ["BLOCKED", "CLOSED"]}}
)

print(f"{result.deleted_count} documents deleted!")