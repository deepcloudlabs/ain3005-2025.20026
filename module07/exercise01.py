from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017")
for db_name in mongo_client.list_database_names():
    print(db_name)

for db in mongo_client.list_databases():
    #print(db)
    print(f"{db['name']}: size={db['sizeOnDisk']//1024} KiB")
    for collection_name in mongo_client[db['name']].list_collection_names():
        print(collection_name)
    for coll in mongo_client[db['name']].list_collections():
        print(coll)