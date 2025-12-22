from pymongo import MongoClient
accounts = [
    {"_id": "BE62557728181161", "balance": 1_000_000, "status": "ACTIVE"},
    {"_id": "BE13549886475839", "balance": 2_000_000, "status": "CLOSED"},
    {"_id": "BE42131139281554", "balance": 3_000_000, "status": "BLOCKED"},
    {"_id": "BE32953183352702", "balance": 4_000_000, "status": "ACTIVE"},
    {"_id": "BE27817995458973", "balance": 5_000_000, "status": "CLOSED"},
    {"_id": "BE95897317372358", "balance": 6_000_000, "status": "BLOCKED"}
]
mongo_client = MongoClient('localhost', 27017)
denizbank = mongo_client["denizbank"]
accounts_collection = denizbank["accounts"]
with mongo_client.start_session() as session:
    def insert_accounts(a_session):
        global accounts
        global accounts_collection
        for account in accounts:
            accounts_collection.insert_one(account,session=a_session)
    session.with_transaction(insert_accounts)
